from playwright.sync_api import sync_playwright

def test_errors():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        errors = []
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: errors.append(err.message))

        page.route("https://cdn.tailwindcss.com", lambda route: route.abort())
        page.goto('http://localhost:8000', wait_until='domcontentloaded')

        # Section needs to be visible
        page.evaluate("document.getElementById('manualStatsSection').style.display = 'block'")

        # Click the new button
        page.evaluate("document.querySelector('button[onclick=\"addCustomDmgRow()\"]').click()")

        # Set some values and trigger calculation
        page.fill('#customDmgVal_2', '10')
        page.fill('#customDmgVal_1', '20')

        # Read final attack damage
        dmg = page.locator('#resOriginalAttack').text_content()
        print(f"Original Attack displayed: {dmg}")

        browser.close()

        if errors:
            print("Errors found:")
            for err in errors:
                print(err)
            raise Exception("Errors found in console")
        else:
            print("No errors found in console")

if __name__ == '__main__':
    test_errors()
