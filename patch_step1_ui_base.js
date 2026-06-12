const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf8');

content = content.replace(
    /const aoeDmg = val\('aoeDmg'\) \+ eqStats\.aoeDmg;\n\s*const projectileDmg = val\('projectileDmg'\) \+ eqStats\.projectileDmg;\n\s*const basicAttackDamagePct = val\('basicAttackDamagePct'\) \+ eqStats\.basicAttackDamagePct;\n\s*const skillAttackDamagePct = val\('skillAttackDamagePct'\) \+ eqStats\.skillAttackDamagePct \+ val\('artifact_10'\);/,
    "const aoeDmg = ((1 + val('aoeDmg') / 100) * eqStats.aoeDmgMulti - 1) * 100;\n            const projectileDmg = ((1 + val('projectileDmg') / 100) * eqStats.projectileDmgMulti - 1) * 100;\n            const basicAttackDamagePct = ((1 + val('basicAttackDamagePct') / 100) * eqStats.basicAttackDamageMulti - 1) * 100;\n            const skillAttackDamagePct = ((1 + val('skillAttackDamagePct') / 100) * (1 + val('artifact_10') / 100) * eqStats.skillAttackDamageMulti - 1) * 100;"
);

// We also need to fix allDmg, normalMonsterDmg, bossMonsterDmg ?
// The user request stated "피해량류는 전부 곱연산" which meant "Damage percent type are all multiplicative". Wait, the prompt says "예: (리스 30% × 토벤용사의 아케인세이버 350% × 불의눈 150% × 혼테일의 비늘 70% = 2,486.25% 증가)" and リ스 is basic attack damage pct. So those 4 are damage pct type. What about others like '일반 몬스터 데미지%', '보스 몬스터 데미지%', '모든 데미지%' ? They are "데미지%" not "피해량%". The user specifically distinguished them in the formula:
// × (일반 몬스터 데미지% 또는 보스 몬스터 데미지%) [신야]
// × (모든 데미지% + 스킬 데미지% 또는 기본공격 데미지%)
// × (범위 피해량% 또는 발사체 피해량%) [영사증]
// × (적이 받는 피해량 증가%) [돌파:도미펜]
// × (스킬 계수 또는 기본공격 계수%)
// [스킬 공격 시] × (스킬 피해량%) [핑크빈용사동상]
// [기본 공격 시] × (기본공격 피해량%) [리스]
// [타수 보정 그룹] × (타수 당 피해량%) [빅토리]

// Ok, so allDmg and class damages etc are NOT Multiplicative. The user says "피해량류는 전부 곱연산" meaning "Damage Pct category are multiplicative". I've only changed 피해량%. Let's check how UI elements for allDmg are printed.
fs.writeFileSync('index.html', content);
