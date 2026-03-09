from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto('http://localhost:8000')
    page.wait_for_selector('h1')
    page.click('button:has-text("설정")')
    page.screenshot(path='screenshot_settings.png')
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
