from playwright.sync_api import sync_playwright

def test_victory_pet_dps():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:8000', wait_until='domcontentloaded')

        # set basic values
        page.fill('#finalAttack', '1000')

        # equip Victory pet in equipPet1Type
        # The option is hidden because the section might be closed, so just evaluate
        page.evaluate("""() => {
            const select = document.getElementById('equipPet1Type');
            select.value = '빅토리';
            select.dispatchEvent(new Event('change'));
        }""")

        # Give JS time to calculate
        page.wait_for_timeout(500)

        res = page.locator('#resTotalDmg').inner_text()
        print(f"Total Dmg with Victory pet: {res}")
        assert not res.startswith('-'), f"Total Damage is negative! {res}"

        browser.close()

if __name__ == '__main__':
    test_victory_pet_dps()
    print("Test passed successfully.")
