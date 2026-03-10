from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000")

        # Set to 기본공격, 범위, 핑크빈
        page.evaluate("document.getElementById('manualStatsSection').style.display = 'block'")
        page.select_option("#attackType", "기본공격")
        page.select_option("#hitType", "범위")
        page.fill("#finalAttack", "1000")
        page.fill("#artifact_10", "50") # 핑크빈 용사 동상 (범위, 발사 스킬 피해량 증가)

        page.evaluate("calculate()")
        dmg1 = page.locator("#resBasicNoCritDmg").inner_text()
        print(f"기본공격, 핑크빈동상(범위스킬피해) 50%: {dmg1}")

        page.evaluate("document.getElementById('manualStatsSection').style.display = 'block'")
        page.select_option("#attackType", "스킬")
        page.evaluate("calculate()")
        dmg2 = page.locator("#resSkillNoCritDmg").inner_text()
        print(f"스킬, 핑크빈동상(범위스킬피해) 50%: {dmg2}")

run()
