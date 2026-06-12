from playwright.sync_api import sync_playwright
import time

def test_errors():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        errors = []
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: errors.append(err.message))

        page.route("https://cdn.tailwindcss.com", lambda route: route.abort())
        page.goto('http://localhost:8000', wait_until='domcontentloaded')

        page.evaluate("document.getElementById('manualStatsSection').style.display = 'block'")

        time.sleep(1)

        # Print all customDmgVal ids to see what exists
        ids = page.evaluate("Array.from(document.querySelectorAll('input[id^=\"customDmgVal\"]')).map(el => el.id)")
        print(f"Available input IDs: {ids}")

        if "customDmgVal_1" in ids:
            page.evaluate("document.getElementById('customDmgVal_1').value = '10'; document.getElementById('customDmgVal_1').dispatchEvent(new Event('input'))")

        time.sleep(1)

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
