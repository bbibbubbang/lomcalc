from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto('http://localhost:8000')
    page.wait_for_selector('h1')

    # Equip some items to trigger buffs
    page.evaluate("document.getElementById('equipWeaponType').value = '고대신의 지팡이'; document.getElementById('equipWeaponType').dispatchEvent(new Event('change'));")
    page.evaluate("document.getElementById('equipWeaponGrade').value = '3'; document.getElementById('equipWeaponGrade').dispatchEvent(new Event('change'));")

    # Scroll slightly above the results section to make sure list is in view
    page.evaluate("document.getElementById('showBuffItems').scrollIntoView({block: 'center'});")

    page.screenshot(path='screenshot_before_check.png')

    # Check the box
    page.check('#showBuffItems')
    page.screenshot(path='screenshot_after_check.png')

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
