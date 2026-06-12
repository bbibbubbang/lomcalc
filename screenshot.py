from playwright.sync_api import sync_playwright

def screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.route("https://cdn.tailwindcss.com", lambda route: route.abort())
        page.goto('http://localhost:8000', wait_until='domcontentloaded')

        # open manual stats section
        page.evaluate("document.getElementById('manualStatsSection').style.display = 'block'")

        # open real stats section
        page.evaluate("document.getElementById('realStatsSection').style.display = 'block'")

        # add couple of custom damages
        page.evaluate("document.querySelector('button[onclick=\"addCustomDmgRow()\"]').click()")

        page.evaluate("document.getElementById('customDmgVal_1').value = '10'; document.getElementById('customDmgVal_1').dispatchEvent(new Event('input'))")

        page.screenshot(path='screenshot.png', full_page=True)
        browser.close()

if __name__ == '__main__':
    screenshot()
