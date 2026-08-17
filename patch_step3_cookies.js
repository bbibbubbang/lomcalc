const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf8');

// Update saveSettings
content = content.replace(
    /function saveSettings\(\) \{\n\s*const data = \{\};\n\s*inputs\.forEach\(input => \{\n\s*if \(input\.type === 'checkbox'\) \{\n\s*data\[input\.id\] = input\.checked;\n\s*\} else \{\n\s*data\[input\.id\] = input\.value;\n\s*\}\n\s*\}\);\n\s*setCookie\('mapleCalcData', JSON\.stringify\(data\), 30\); \/\/ Save for 30 days\n\s*\}/,
    `function saveSettings() {
            const data = {};
            inputs.forEach(input => {
                // Skip dynamically generated calc-inputs from saving in the default loop
                if (input.id && input.id.startsWith('customDmg')) return;

                if (input.type === 'checkbox') {
                    data[input.id] = input.checked;
                } else {
                    data[input.id] = input.value;
                }
            });

            // Save custom damage rows
            const customDmgRows = [];
            document.querySelectorAll('.custom-dmg-row').forEach(row => {
                const id = row.id.split('_')[1];
                const name = document.getElementById('customDmgName_' + id).value;
                const sign = document.getElementById('customDmgSign_' + id).value;
                const val = document.getElementById('customDmgVal_' + id).value;
                customDmgRows.push({ name, sign, val });
            });
            data['customDmgRowsData'] = customDmgRows;

            setCookie('mapleCalcData', JSON.stringify(data), 30); // Save for 30 days
        }`
);

// Update loadSettings
content = content.replace(
    /const data = JSON\.parse\(savedData\);\n\s*inputs\.forEach\(input => \{\n\s*if \(data\[input\.id\] \!== undefined\) \{/,
    `const data = JSON.parse(savedData);

                    if (data['customDmgRowsData'] && data['customDmgRowsData'].length > 0) {
                        data['customDmgRowsData'].forEach(row => {
                            addCustomDmgRow(row.name, row.val, row.sign);
                        });
                    } else {
                        // fallback default row
                        addCustomDmgRow('피해량1', 0, 1);
                    }

                    inputs.forEach(input => {
                        if (input.id && input.id.startsWith('customDmg')) return;
                        if (data[input.id] !== undefined) {`
);

// also ensure addCustomDmgRow('피해량1', 0, 1) is called if no cookie
content = content.replace(
    /if \(savedData\) \{/,
    `if (savedData) {` // keep as is
);

// We need to find the fallback where there is NO cookie loaded, to initialize the default row.
content = content.replace(
    /if \(\!savedData\) \{/g, // it's not checked explicitly usually. Let's see how loadSettings handles the initial state
    ''
);

fs.writeFileSync('index.html', content);
