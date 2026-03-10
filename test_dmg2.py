from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000")

        # Set to 기본공격
        page.select_option("#attackType", "기본공격")

        # Base settings
        page.fill("#finalAttack", "1000")
        page.fill("#skillDmg", "50") # 스킬 데미지 추가

        page.evaluate("calculate()")
        dmg1 = page.locator("#resBasicNoCritDmg").inner_text()
        print(f"기본공격, 스킬데미지50%: {dmg1}")

        page.select_option("#attackType", "스킬")
        page.evaluate("calculate()")
        dmg2 = page.locator("#resSkillNoCritDmg").inner_text()
        print(f"스킬, 스킬데미지50%: {dmg2}")

run()
