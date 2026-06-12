const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf8');

const customDmgSectionHtml = `
                    <!-- Custom Damage Line Column -->
                    <div class="bg-white p-6 rounded-lg shadow-md border border-gray-200 col-span-1 md:col-span-3">
                        <h2 class="text-xl font-bold mb-4 text-purple-600 border-b pb-2">추가 피해량 (곱연산)</h2>
                        <div id="customDmgContainer" class="space-y-2">
                            <!-- Dynamic rows will be added here -->
                        </div>
                        <button onclick="addCustomDmgRow()" class="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 font-bold">+ 피해량 라인 추가</button>
                    </div>
`;

// Insert the new column before the end of the manualStatsSection grid
content = content.replace(
    /<!-- 하단 접기 버튼 -->/,
    customDmgSectionHtml + '\n                <!-- 하단 접기 버튼 -->'
);

// Add the JS functions for Custom Damage Rows
const jsFunctions = `
        let customDmgCount = 0;

        function addCustomDmgRow(name = '', value = 0, sign = 1) {
            customDmgCount++;
            const id = customDmgCount;
            const container = document.getElementById('customDmgContainer');

            const row = document.createElement('div');
            row.className = 'flex items-center space-x-2 custom-dmg-row';
            row.id = \`customDmgRow_\${id}\`;

            const defaultName = name || \`피해량\${id}\`;

            row.innerHTML = \`
                <input type="text" id="customDmgName_\${id}" class="calc-input border p-1 rounded flex-1" value="\${defaultName}" placeholder="항목 이름">
                <select id="customDmgSign_\${id}" class="calc-input border p-1 rounded">
                    <option value="1" \${sign == 1 ? 'selected' : ''}>+</option>
                    <option value="-1" \${sign == -1 ? 'selected' : ''}>-</option>
                </select>
                <input type="number" id="customDmgVal_\${id}" class="calc-input border p-1 rounded w-24" value="\${value}" step="0.1" onfocus="handleNumericFocus(this)" onblur="handleNumericBlur(this)" oninput="handleNumericInput(this)">
                <span class="text-gray-600">%</span>
                <button onclick="removeCustomDmgRow(\${id})" class="text-red-500 hover:text-red-700 font-bold px-2">X</button>
            \`;

            container.appendChild(row);

            // Trigger recalculation if necessary or setup listeners
            document.getElementById(\`customDmgName_\${id}\`).addEventListener('input', calculate);
            document.getElementById(\`customDmgSign_\${id}\`).addEventListener('change', calculate);
            document.getElementById(\`customDmgVal_\${id}\`).addEventListener('input', calculate);
        }

        function removeCustomDmgRow(id) {
            const row = document.getElementById(\`customDmgRow_\${id}\`);
            if (row) {
                row.remove();
                calculate();
            }
        }

        function getCustomDmgMulti() {
            let multi = 1;
            const rows = document.querySelectorAll('.custom-dmg-row');
            rows.forEach(row => {
                const id = row.id.split('_')[1];
                const sign = parseFloat(document.getElementById(\`customDmgSign_\${id}\`).value);
                const val = parseFloat(document.getElementById(\`customDmgVal_\${id}\`).value) || 0;

                if (val !== 0) {
                    multi *= (1 + (sign * val) / 100);
                }
            });
            return multi;
        }

        // Initialize with one default row
        window.addEventListener('DOMContentLoaded', () => {
            // We'll call this in init() or check if cookies loaded first
        });
`;

content = content.replace(
    /function toggleSection\(sectionId, arrowId, btnGroupId\) {/,
    jsFunctions + '\n        function toggleSection(sectionId, arrowId, btnGroupId) {'
);

fs.writeFileSync('index.html', content);
