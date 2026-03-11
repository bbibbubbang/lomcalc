import sys
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 1024})
    page.goto('http://localhost:8000')

    # Inject CSS
    page.add_style_tag(content="""
        @media (min-width: 768px) {
            .form-group:not(.w-24) input[type="number"],
            .form-group:not(.w-24) select {
                max-width: 250px;
            }
        }
    """)
    page.evaluate("document.getElementById('artifactSection').style.display = 'grid'")
    page.evaluate("document.getElementById('manualStatsSection').style.display = 'block'")
    page.screenshot(path='screenshot_after_css_test_full.png', full_page=True)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
