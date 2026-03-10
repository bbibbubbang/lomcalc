const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

const search1 = `
            const basicNoCritDamage = baseDamageMultiplier * (1 + basicTypeDmg / 100);
            const skillNoCritDamage = baseDamageMultiplier * (1 + skillTypeDmg / 100);`;
const replace1 = `
            let hitMulti = eqStats.baseHitMulti > 0 ? eqStats.baseHitMulti : 1;
            let hitDmgMulti = eqStats.hitDmgMulti;

            const basicNoCritDamage = baseDamageMultiplier * (1 + basicTypeDmg / 100) * hitMulti * hitDmgMulti;
            const skillNoCritDamage = baseDamageMultiplier * (1 + skillTypeDmg / 100) * hitMulti * hitDmgMulti;`;

html = html.replace(search1, replace1);

const search2 = `
            let hitMulti = eqStats.baseHitMulti > 0 ? eqStats.baseHitMulti : 1;
            let hitDmgMulti = eqStats.hitDmgMulti;
            const avgDPS = (avgDamage * hitDmgMulti) * (finalHitsPerSec * hitMulti);`;
const replace2 = `
            const avgDPS = avgDamage * finalHitsPerSec;`;

html = html.replace(search2, replace2);

fs.writeFileSync('index.html.fixed', html);
