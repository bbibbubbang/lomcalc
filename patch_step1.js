const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf8');

// Update adv + auto to additive before multi
content = content.replace(
    /const buffedA = originalAttack \* \(1 \+ \(townAttackPct \+ attackPct\) \/ 100\) \* \(1 \+ advAttackPct \/ 100\) \* \(1 \+ autoAttackPct \/ 100\);/g,
    'const buffedA = originalAttack * (1 + (townAttackPct + attackPct) / 100) * (1 + (advAttackPct + autoAttackPct) / 100);'
);

content = content.replace(
    /const buffedD = originalDefense \* \(1 \+ \(townDefensePct \+ defensePct\) \/ 100\) \* \(1 \+ advDefensePct \/ 100\) \* \(1 \+ autoDefensePct \/ 100\);/g,
    'const buffedD = originalDefense * (1 + (townDefensePct + defensePct) / 100) * (1 + (advDefensePct + autoDefensePct) / 100);'
);

content = content.replace(
    /const buffedH = originalHP \* \(1 \+ \(townHpPct \+ hpPct\) \/ 100\) \* \(1 \+ advHpPct \/ 100\) \* \(1 \+ autoHpPct \/ 100\);/g,
    'const buffedH = originalHP * (1 + (townHpPct + hpPct) / 100) * (1 + (advHpPct + autoHpPct) / 100);'
);

content = content.replace(
    /const basicBuffedA = originalAttack \* \(1 \+ \(townAttackPct \+ attackPct\) \/ 100\) \* \(1 \+ basicAdvAttackPct \/ 100\) \* \(1 \+ autoAttackPct \/ 100\);/g,
    'const basicBuffedA = originalAttack * (1 + (townAttackPct + attackPct) / 100) * (1 + (basicAdvAttackPct + autoAttackPct) / 100);'
);

content = content.replace(
    /const iBuffedA = originalAttack \* \(1 \+ \(townAttackPct \+ iAttackPct\) \/ 100\) \* \(1 \+ iAdvAttackPct \/ 100\) \* \(1 \+ iAutoAttackPct \/ 100\);/g,
    'const iBuffedA = originalAttack * (1 + (townAttackPct + iAttackPct) / 100) * (1 + (iAdvAttackPct + iAutoAttackPct) / 100);'
);

content = content.replace(
    /const iBuffedD = originalDefense \* \(1 \+ \(townDefensePct \+ iDefensePct\) \/ 100\) \* \(1 \+ iAdvDefensePct \/ 100\) \* \(1 \+ iAutoDefensePct \/ 100\);/g,
    'const iBuffedD = originalDefense * (1 + (townDefensePct + iDefensePct) / 100) * (1 + (iAdvDefensePct + iAutoDefensePct) / 100);'
);

content = content.replace(
    /const iBuffedH = originalHP \* \(1 \+ \(townHpPct \+ hpPct\) \/ 100\) \* \(1 \+ iAdvHpPct \/ 100\) \* \(1 \+ iAutoHpPct \/ 100\);/g,
    'const iBuffedH = originalHP * (1 + (townHpPct + hpPct) / 100) * (1 + (iAdvHpPct + iAutoHpPct) / 100);'
);

content = content.replace(
    /const iBasicBuffedA = originalAttack \* \(1 \+ \(townAttackPct \+ iAttackPct\) \/ 100\) \* \(1 \+ iBasicAdvAttackPct \/ 100\) \* \(1 \+ iAutoAttackPct \/ 100\);/g,
    'const iBasicBuffedA = originalAttack * (1 + (townAttackPct + iAttackPct) / 100) * (1 + (iBasicAdvAttackPct + iAutoAttackPct) / 100);'
);

// Switch aoeDmg, projectileDmg, basicAttackDamagePct, skillAttackDamagePct to multiplicative.
// First in eqStats init
content = content.replace(
    /aoeDmg: 0,\n\s*projectileDmg: 0,\n\s*allClassDmg: 0,\n\s*basicAttackDmg: 0,\n\s*skillDmg: 0,\n\s*basicAttackDamagePct: 0,\n\s*skillAttackDamagePct: 0,/,
    'aoeDmgMulti: 1,\n                projectileDmgMulti: 1,\n                allClassDmg: 0,\n                basicAttackDmg: 0,\n                skillDmg: 0,\n                basicAttackDamageMulti: 1,\n                skillAttackDamageMulti: 1,'
);

// In applyItemStat
content = content.replace(
    /else if \(statName === '범위 피해량%' \|\| statName === '공격범위\/피해량%'\) eqStats\.aoeDmg \+= effectiveValue;/g,
    "else if (statName === '범위 피해량%' || statName === '공격범위/피해량%') eqStats.aoeDmgMulti *= (1 + effectiveValue / 100);"
);

content = content.replace(
    /else if \(statName === '발사체 피해량%'\) eqStats\.projectileDmg \+= effectiveValue;/g,
    "else if (statName === '발사체 피해량%') eqStats.projectileDmgMulti *= (1 + effectiveValue / 100);"
);

content = content.replace(
    /else if \(statName === '기본공격 피해량%'\) eqStats\.basicAttackDamagePct \+= effectiveValue;/g,
    "else if (statName === '기본공격 피해량%') eqStats.basicAttackDamageMulti *= (1 + effectiveValue / 100);"
);

content = content.replace(
    /else if \(statName === '스킬 피해량%' \|\| statName === '공격스킬 피해량%'\) eqStats\.skillAttackDamagePct \+= effectiveValue;/g,
    "else if (statName === '스킬 피해량%' || statName === '공격스킬 피해량%') eqStats.skillAttackDamageMulti *= (1 + effectiveValue / 100);"
);

// In computeIntervalDamage
content = content.replace(
    /else if \(statName === '범위 피해량%' \|\| statName === '공격범위\/피해량%'\) intervalEqStats\.aoeDmg \+= effectiveValue;/g,
    "else if (statName === '범위 피해량%' || statName === '공격범위/피해량%') intervalEqStats.aoeDmgMulti *= (1 + effectiveValue / 100);"
);

content = content.replace(
    /else if \(statName === '발사체 피해량%'\) intervalEqStats\.projectileDmg \+= effectiveValue;/g,
    "else if (statName === '발사체 피해량%') intervalEqStats.projectileDmgMulti *= (1 + effectiveValue / 100);"
);

content = content.replace(
    /else if \(statName === '기본공격 피해량%'\) intervalEqStats\.basicAttackDamagePct \+= effectiveValue;/g,
    "else if (statName === '기본공격 피해량%') intervalEqStats.basicAttackDamageMulti *= (1 + effectiveValue / 100);"
);

content = content.replace(
    /else if \(statName === '스킬 피해량%' \|\| statName === '공격스킬 피해량%'\) intervalEqStats\.skillAttackDamagePct \+= effectiveValue;/g,
    "else if (statName === '스킬 피해량%' || statName === '공격스킬 피해량%') intervalEqStats.skillAttackDamageMulti *= (1 + effectiveValue / 100);"
);

// Calculate Multipliers
content = content.replace(
    /const iBasicAttackDamagePct = val\('basicAttackDamagePct'\) \+ intervalEqStats\.basicAttackDamagePct;\n\s*const iSkillAttackDamagePct = val\('skillAttackDamagePct'\) \+ intervalEqStats\.skillAttackDamagePct \+ val\('artifact_10'\);/,
    "const iBasicAttackDamageMulti = (1 + val('basicAttackDamagePct') / 100) * intervalEqStats.basicAttackDamageMulti;\n                const iSkillAttackDamageMulti = (1 + val('skillAttackDamagePct') / 100) * (1 + val('artifact_10') / 100) * intervalEqStats.skillAttackDamageMulti;"
);

content = content.replace(
    /let iHitTypeDmgMultiplier = 1;\n\s*if\(hitType === '범위'\) iHitTypeDmgMultiplier = 1 \+ \(val\('aoeDmg'\) \+ intervalEqStats\.aoeDmg\) \/ 100;\n\s*if\(hitType === '발사체'\) iHitTypeDmgMultiplier = 1 \+ \(val\('projectileDmg'\) \+ intervalEqStats\.projectileDmg\) \/ 100;/,
    "let iHitTypeDmgMultiplier = 1;\n                if(hitType === '범위') iHitTypeDmgMultiplier = (1 + val('aoeDmg') / 100) * intervalEqStats.aoeDmgMulti;\n                if(hitType === '발사체') iHitTypeDmgMultiplier = (1 + val('projectileDmg') / 100) * intervalEqStats.projectileDmgMulti;"
);

content = content.replace(
    /const iBasicExtraAttackDamageMultiplier = 1 \+ iBasicAttackDamagePct \/ 100;\n\s*const iSkillExtraAttackDamageMultiplier = 1 \+ iSkillAttackDamagePct \/ 100;/,
    "const iBasicExtraAttackDamageMultiplier = iBasicAttackDamageMulti;\n                const iSkillExtraAttackDamageMultiplier = iSkillAttackDamageMulti;"
);

fs.writeFileSync('index.html', content);
