import sys
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 1024})
    page.goto('http://localhost:8000')

    # Inject CSS
    page.add_style_tag(content="""
        @media (min-width: 768px) {
            input[type="number"], select {
                max-width: 200px;
            }
        }
    """)
    page.screenshot(path='screenshot_after_css_test2.png')

    page.evaluate("document.getElementById('artifactSection').style.display = 'grid'")
    page.screenshot(path='screenshot_after_css_test3.png')

    page.evaluate("document.getElementById('manualStatsSection').style.display = 'block'")
    page.screenshot(path='screenshot_after_css_test4.png')
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
