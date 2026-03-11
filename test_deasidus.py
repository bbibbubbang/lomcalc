from playwright.sync_api import sync_playwright

def test_deasidus_dps():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:8000', wait_until='domcontentloaded')

        # set basic values
        page.evaluate("document.getElementById('manualStatsSection').style.display = 'block'")
        page.fill('#finalAttack', '1000')
        page.fill('#dpsTime', '35')

        # equip Dea Sidus in equipEarringType
        page.evaluate("""() => {
            const select = document.getElementById('equipEarringType');
            select.value = '데아 시두스 이어링';
            select.dispatchEvent(new Event('change'));
        }""")

        page.wait_for_timeout(500)

        res = page.locator('#resTotalDmg').inner_text()
        print(f"Total Dmg with Dea Sidus (35s): {res}")

        browser.close()

if __name__ == '__main__':
    test_deasidus_dps()
