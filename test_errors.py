from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.on("console", lambda msg: print(f"Console: {msg.type}: {msg.text}"))
    page.on("pageerror", lambda err: print(f"Page Error: {err}"))
    page.goto('http://localhost:8000', wait_until='networkidle')
    browser.close()
