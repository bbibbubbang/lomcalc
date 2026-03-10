from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000")

        # Set to 기본공격
        page.evaluate("document.getElementById('manualStatsSection').style.display = 'block'")
        page.select_option("#attackType", "기본공격")

        # Base settings
        page.fill("#finalAttack", "1000")
        page.fill("#attackDamagePct", "50") # 일반/스킬 공격 피해량 추가

        page.evaluate("calculate()")
        dmg1 = page.locator("#resBasicNoCritDmg").inner_text()
        print(f"기본공격, 일반/스킬공격피해량50%: {dmg1}")

run()
