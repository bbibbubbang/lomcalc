const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf8');

content = content.replace(
    /const parsed = JSON\.parse\(savedData\);\n\s*inputs\.forEach\(input => \{\n\s*if \(parsed\[input\.id\] !== undefined\) \{/g,
    `const parsed = JSON.parse(savedData);

                    if (parsed['customDmgRowsData'] && parsed['customDmgRowsData'].length > 0) {
                        parsed['customDmgRowsData'].forEach(row => {
                            addCustomDmgRow(row.name, row.val, row.sign);
                        });
                    } else {
                        addCustomDmgRow('피해량1', 0, 1);
                    }

                    inputs.forEach(input => {
                        if (input.id && input.id.startsWith('customDmg')) return;
                        if (parsed[input.id] !== undefined) {`
);

content = content.replace(
    /function loadSettings\(\) \{\n\s*const savedData = getCookie\('mapleCalcData'\);\n\s*if \(savedData\) \{/g,
    `function loadSettings() {
            const savedData = getCookie('mapleCalcData');
            if (!savedData || !savedData.includes('customDmgRowsData')) {
                // If no saved data or missing customDmg, initialize default
                addCustomDmgRow('피해량1', 0, 1);
            }
            if (savedData) {`
);

fs.writeFileSync('index.html', content);
