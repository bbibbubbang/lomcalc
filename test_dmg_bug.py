from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.route("https://cdn.tailwindcss.com", lambda route: route.abort())

        # Load your specific page
        page.goto("http://localhost:8000/index.html", wait_until='domcontentloaded')

        # Expand sections
        page.evaluate("document.getElementById('townStatsSection').style.display = 'block'")

        # Fill inputs with some sample town values
        page.fill("#finalAttack", "1000")
        page.fill("#townAttackPct", "10")
        page.fill("#finalDefense", "500")
        page.fill("#townDefensePct", "5")
        page.fill("#finalHP", "2000")
        page.fill("#townHpPct", "2")

        # Give some maple leaf levels
        page.fill("#platinumMapleLeafDefLevel", "10")
        page.fill("#platinumMapleLeafAtkToDefLevel", "5")

        # Make sure applyMapleLeafToBase is checked
        page.check("#applyMapleLeafToBase")

        # Calculate
        page.evaluate("calculate()")

        # Read final stats (checked)
        # Grab specifically the pure base stat
        pure_a_checked = page.evaluate("document.getElementById('realOriginalAttack').innerText")
        print(f"Original Attack Base (Checked): {pure_a_checked}")

        final_atk_checked = page.evaluate("document.getElementById('realFinalAttack').innerText")
        print(f"Final Attack (Checked): {final_atk_checked}")

        # Uncheck applyMapleLeafToBase
        page.uncheck("#applyMapleLeafToBase")

        # Calculate again
        page.evaluate("calculate()")

        # Read final stats (unchecked)
        pure_a_unchecked = page.evaluate("document.getElementById('realOriginalAttack').innerText")
        print(f"Original Attack Base (Unchecked): {pure_a_unchecked}")

        final_atk_unchecked = page.evaluate("document.getElementById('realFinalAttack').innerText")
        print(f"Final Attack (Unchecked): {final_atk_unchecked}")

        browser.close()

if __name__ == '__main__':
    run()
