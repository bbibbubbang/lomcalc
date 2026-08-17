const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf8');

// Include customDmgMulti in the base baseDamageMultiplier calculations inside calculate()
content = content.replace(
    /const iBasicBaseDamageMultiplier = iBasicFinalAttack\n\s*\* \(iSkillMultiplier \/ 100\)\n\s*\* \(1 \+ \(iMyClassDmg \+ iAllClassDmg\) \/ 100\)\n\s*\* \(1 \+ iMonsterDmgBase \/ 100\)\n\s*\* \(1 \+ \(iAllDmg \+ iBasicTypeDmg\) \/ 100\)\n\s*\* iDmgTakenMultiplier;/,
    "const customDmgMulti = getCustomDmgMulti();\n                const iBasicBaseDamageMultiplier = iBasicFinalAttack\n                                   * (iSkillMultiplier / 100)\n                                   * (1 + (iMyClassDmg + iAllClassDmg) / 100)\n                                   * (1 + iMonsterDmgBase / 100)\n                                   * (1 + (iAllDmg + iBasicTypeDmg) / 100)\n                                   * iDmgTakenMultiplier * customDmgMulti;"
);

content = content.replace(
    /const iSkillBaseDamageMultiplier = iFinalAttack\n\s*\* \(iSkillMultiplier \/ 100\)\n\s*\* \(1 \+ \(iMyClassDmg \+ iAllClassDmg\) \/ 100\)\n\s*\* \(1 \+ iMonsterDmgBase \/ 100\)\n\s*\* \(1 \+ \(iAllDmg \+ iSkillTypeDmg\) \/ 100\)\n\s*\* iDmgTakenMultiplier;/,
    "const iSkillBaseDamageMultiplier = iFinalAttack\n                                   * (iSkillMultiplier / 100)\n                                   * (1 + (iMyClassDmg + iAllClassDmg) / 100)\n                                   * (1 + iMonsterDmgBase / 100)\n                                   * (1 + (iAllDmg + iSkillTypeDmg) / 100)\n                                   * iDmgTakenMultiplier * customDmgMulti;"
);


fs.writeFileSync('index.html', content);
