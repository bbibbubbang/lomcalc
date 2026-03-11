from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.set_viewport_size({"width": 1280, "height": 1080})
    page.goto('http://localhost:8000/index.html', wait_until='networkidle')

    # Apply CSS
    page.add_style_tag(content="""
        @media (min-width: 768px) {
            input[type="number"],
            input[type="text"],
            select {
                max-width: 250px;
            }
        }
    """)

    # Open Equipment Settings (it's closed by default)
    page.evaluate("document.getElementById('equipSection').style.display = 'block'")

    page.screenshot(path='screenshot_equip_css.png', full_page=True)
    browser.close()
