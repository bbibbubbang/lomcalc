const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const itemDataJs = fs.readFileSync('item_data.js', 'utf8').replace('const itemDataList', 'var itemDataList');
const html = fs.readFileSync('index.html.fixed', 'utf8')
    .replace('<script src="item_data.js"></script>', `<script>${itemDataJs}</script>`)
    .replace('<script src="https://cdn.tailwindcss.com"></script>', '');

const dom = new JSDOM(html, {
    url: "http://localhost/",
    runScripts: "dangerously"
});

setTimeout(() => {
    const document = dom.window.document;

    // reset variables
    document.getElementById('finalAttack').value = "100";
    document.getElementById('skillMultiplier').value = "100";
    document.getElementById('attackPct').value = "0";
    document.getElementById('advAttackPct').value = "0";
    document.getElementById('critRate').value = "0";
    document.getElementById('dpsTime').value = "5";

    dom.window.eval(`
        itemDataList = [{
            "이름": "테스트무기",
            "분류": "무기",
            "장비분류": "무기",
            "공격력": 0,
            "부가스텟명1": null, "부가스텟1": null,
            "부가스텟명2": null, "부가스텟2": null,
            "버프스텟명1": "기본 타수(배)", "버프스텟1": 2.0,
            "버프스텟명2": "타수 당 피해량%", "버프스텟2": -40.0,
            "버프 지속시간(초)\\n// -1인 경우 무한": -1,
            "버프 쿨타임(초)\\n// -1:0초부터 1회만 발동": -1,
            "레전드리3 부가스텟명": null, "레전드리3 부가스텟": null,
            "레전드리5 버프스텟명": null, "레전드리5 버프스텟\\n// 버프스텟은 기존 효과에 추가 적용\\n// 버프 지속시간,쿨타임 영향 받음": -1,
            "레전드리10 부가스텟명": null, "레전드리10 부가스텟": null
        }];
        const equipWeaponType = document.getElementById('equipWeaponType');
        equipWeaponType.innerHTML = '<option value="없음">없음</option><option value="테스트무기">테스트무기</option>';
    `);

    dom.window.calculate();

    console.log("Without weapon:");
    console.log("No Crit Dmg:", document.getElementById('resBasicNoCritDmg').innerText);
    console.log("Avg Dmg:", document.getElementById('resAvgDmg').innerText);
    console.log("Avg DPS:", document.getElementById('resAvgDPS').innerText);
    console.log("Total Dmg:", document.getElementById('resTotalDmg').innerText);

    const equipWeaponType = document.getElementById('equipWeaponType');
    equipWeaponType.value = "테스트무기";
    const equipWeaponGrade = document.getElementById('equipWeaponGrade');
    equipWeaponGrade.value = "1"; // 레전드리
    const event = new dom.window.Event('change', { bubbles: true });
    equipWeaponType.dispatchEvent(event);
    equipWeaponGrade.dispatchEvent(event);

    dom.window.calculate();

    console.log("\nWith weapon:");
    console.log("No Crit Dmg:", document.getElementById('resBasicNoCritDmg').innerText);
    console.log("Avg Dmg:", document.getElementById('resAvgDmg').innerText);
    console.log("Avg DPS:", document.getElementById('resAvgDPS').innerText);
    console.log("Total Dmg:", document.getElementById('resTotalDmg').innerText);
}, 100);
