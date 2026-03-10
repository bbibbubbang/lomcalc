from playwright.sync_api import sync_playwright

def test_reece_pet():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:8000')

        # Equip '리스' in pet slot 1
        page.evaluate("document.getElementById('equipPet1Type').value = '리스'")
        page.evaluate("document.getElementById('equipPet1Type').dispatchEvent(new Event('change'))")

        # Wait a bit
        page.wait_for_timeout(500)

        # Check basicAttackDamagePct
        real_basic_dmg_pct = page.inner_text('#realBasicAttackDamagePct')
        assert '30.0%' in real_basic_dmg_pct, f"Expected 30.0% in realBasicAttackDamagePct but got {real_basic_dmg_pct}"

        # Check basicTypeDmg
        real_basic_attack_dmg = page.inner_text('#realBasicAttackDmg')
        assert '10.0%' in real_basic_attack_dmg, f"Expected 10.0% in realBasicAttackDmg but got {real_basic_attack_dmg}"

        print("Reece pet test passed!")
        browser.close()

if __name__ == '__main__':
    test_reece_pet()