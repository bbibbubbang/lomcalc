const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf8');

content = content.replace(
    /const allDmg = val\('allDmg'\) \+ eqStats\.allDmg;\n\s*const basicAttackDamagePct = val\('basicAttackDamagePct'\) \+ eqStats\.basicAttackDamagePct;\n\s*const skillAttackDamagePct = val\('skillAttackDamagePct'\) \+ eqStats\.skillAttackDamagePct \+ val\('artifact_10'\);/,
    "const allDmg = val('allDmg') + eqStats.allDmg;\n            const basicAttackDamagePct = ((1 + val('basicAttackDamagePct') / 100) * eqStats.basicAttackDamageMulti - 1) * 100;\n            const skillAttackDamagePct = ((1 + val('skillAttackDamagePct') / 100) * (1 + val('artifact_10') / 100) * eqStats.skillAttackDamageMulti - 1) * 100;"
);

// We need to also fix aoeDmg and projectileDmg in UI
content = content.replace(
    /document\.getElementById\('realAoeDmg'\)\.innerText = \(val\('aoeDmg'\) \+ eqStats\.aoeDmg\)\.toFixed\(1\) \+ '%';\n\s*document\.getElementById\('realProjectileDmg'\)\.innerText = \(val\('projectileDmg'\) \+ eqStats\.projectileDmg\)\.toFixed\(1\) \+ '%';/,
    "document.getElementById('realAoeDmg').innerText = (((1 + val('aoeDmg') / 100) * eqStats.aoeDmgMulti - 1) * 100).toFixed(1) + '%';\n            document.getElementById('realProjectileDmg').innerText = (((1 + val('projectileDmg') / 100) * eqStats.projectileDmgMulti - 1) * 100).toFixed(1) + '%';"
);

fs.writeFileSync('index.html', content);
