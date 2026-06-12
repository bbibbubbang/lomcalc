const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf8');

const customDmgHtml = `
                    <!-- Custom Damage Line Column -->
                    <div class="bg-white p-6 rounded-lg shadow-md border border-gray-200 col-span-1 md:col-span-3">
                        <h2 class="text-xl font-bold mb-4 text-purple-600 border-b pb-2">추가 피해량 (곱연산)</h2>
                        <div id="customDmgContainer" class="space-y-2">
                            <!-- Dynamic rows will be added here -->
                        </div>
                        <button onclick="addCustomDmgRow()" class="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 font-bold">+ 피해량 라인 추가</button>
                    </div>
`;

// Remove it from the wrong place
content = content.replace(customDmgHtml, '');

// And put it into manualStatsSection just before its '▲ 접기'
content = content.replace(
    /<!-- 하단 접기 버튼 -->\n\s*<div class="mt-4 text-center border-t pb-2 pt-4">\n\s*<button onclick="toggleSection\('manualStatsSection', 'manualStatsArrow'\)"/,
    customDmgHtml + '\n                <!-- 하단 접기 버튼 -->\n                <div class="mt-4 text-center border-t pb-2 pt-4">\n                    <button onclick="toggleSection(\'manualStatsSection\', \'manualStatsArrow\')"'
);

fs.writeFileSync('index.html', content);
