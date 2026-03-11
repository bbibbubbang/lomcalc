from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.goto('http://localhost:8000')
        page.evaluate("document.getElementById('equipSection').style.display = 'grid'")
        page.evaluate("document.getElementById('artifactSection').style.display = 'grid'")
        page.evaluate("document.getElementById('manualStatsSection').style.display = 'block'")
        page.wait_for_timeout(1000)
        page.screenshot(path='screenshot_before.png', full_page=True)
        browser.close()

if __name__ == '__main__':
    run()
