from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 1024})
        page.goto("http://localhost:8000")

        # Add a simple CSS rule for max-width on all inputs/selects on desktop
        page.add_style_tag(content='''
        @media (min-width: 768px) {
            input[type="number"],
            input[type="text"],
            select {
                max-width: 250px;
            }
        }
        ''')

        page.evaluate("document.getElementById('equipArrow').click()")
        page.evaluate("document.getElementById('manualStatsArrow').click()")
        page.wait_for_timeout(500)

        page.screenshot(path="screenshot_simple_css.png", full_page=True)
        browser.close()

run()
