from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000")

        # Set to 기본공격
        page.evaluate("document.getElementById('manualStatsSection').style.display = 'block'")
        page.select_option("#attackType", "기본공격")

        # Base settings to get a simple damage
        page.fill("#finalAttack", "1000")

        page.evaluate("calculate()")
        dmg1 = page.locator("#resBasicNoCritDmg").inner_text()
        print(f"기본공격 + 일반: {dmg1}")

        # Change hitType to 범위
        page.select_option("#hitType", "범위")
        page.fill("#aoeDmg", "50")
        page.evaluate("calculate()")
        dmg2 = page.locator("#resBasicNoCritDmg").inner_text()
        print(f"기본공격 + 범위 + 범위피해량50%: {dmg2}")

run()
