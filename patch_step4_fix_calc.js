const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf8');

// The initialization of customDmgMulti was accidentally put after it was used! Let's fix that.
content = content.replace(
    /const iSkillBaseDamageMultiplier = iFinalAttack\n\s*\* \(iSkillMultiplier \/ 100\)\n\s*\* \(1 \+ \(iMyClassDmg \+ iAllClassDmg\) \/ 100\)\n\s*\* \(1 \+ iMonsterDmgBase \/ 100\)\n\s*\* \(1 \+ \(iAllDmg \+ iSkillTypeDmg\) \/ 100\)\n\s*\* iDmgTakenMultiplier \* customDmgMulti;\n\n\s*const customDmgMulti = getCustomDmgMulti\(\);\n\s*const iBasicBaseDamageMultiplier = iBasicFinalAttack\n\s*\* \(iSkillMultiplier \/ 100\)\n\s*\* \(1 \+ \(iMyClassDmg \+ iAllClassDmg\) \/ 100\)\n\s*\* \(1 \+ iMonsterDmgBase \/ 100\)\n\s*\* \(1 \+ \(iAllDmg \+ iBasicTypeDmg\) \/ 100\)\n\s*\* iDmgTakenMultiplier \* customDmgMulti;/,
    "const customDmgMulti = getCustomDmgMulti();\n                const iSkillBaseDamageMultiplier = iFinalAttack\n                                   * (iSkillMultiplier / 100)\n                                   * (1 + (iMyClassDmg + iAllClassDmg) / 100)\n                                   * (1 + iMonsterDmgBase / 100)\n                                   * (1 + (iAllDmg + iSkillTypeDmg) / 100)\n                                   * iDmgTakenMultiplier * customDmgMulti;\n\n                const iBasicBaseDamageMultiplier = iBasicFinalAttack\n                                   * (iSkillMultiplier / 100)\n                                   * (1 + (iMyClassDmg + iAllClassDmg) / 100)\n                                   * (1 + iMonsterDmgBase / 100)\n                                   * (1 + (iAllDmg + iBasicTypeDmg) / 100)\n                                   * iDmgTakenMultiplier * customDmgMulti;"
);

// We need to also fix where customDmgMulti is initialized globally outside interval loop, or inside? getCustomDmgMulti() scans the DOM each time.
// Calling getCustomDmgMulti() inside the interval loop `timePoints.length` times is inefficient. Let's do it outside.
// Wait, `computeIntervalDamage` runs many times.
// Let's modify index.html to fetch `getCustomDmgMulti()` outside `computeIntervalDamage`
content = content.replace(
    /const computeIntervalDamage = \(dt, t_mid\) => \{/,
    "const customDmgMulti = getCustomDmgMulti();\n            const computeIntervalDamage = (dt, t_mid) => {"
);

// And then remove it from inside
content = content.replace(
    /const customDmgMulti = getCustomDmgMulti\(\);\n\s*const iSkillBaseDamageMultiplier/,
    "const iSkillBaseDamageMultiplier"
);

// Also missing handleNumericInput in our custom string? wait, we used oninput="handleNumericInput(this)". Is it available globally? Let's check index.html for handleNumericInput
fs.writeFileSync('index.html', content);
