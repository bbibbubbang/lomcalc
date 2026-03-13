import re
from playwright.sync_api import sync_playwright

def test_desc():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('http://localhost:8000', wait_until='domcontentloaded')

        # check description box isn't shown originally
        display = page.evaluate("document.getElementById('equipWeaponDesc').style.display")
        assert display == 'none' or display == ''

        # turn on checkbox
        page.evaluate("document.getElementById('settingsSection').style.display = 'block'")
        page.check("#showItemDesc")

        # Select weapon
        page.evaluate("document.getElementById('equipSection').style.display = 'block'")
        page.evaluate("document.getElementById('equipWeaponType').value = '냉동참치(돌파)'")
        page.evaluate("document.getElementById('equipWeaponType').dispatchEvent(new Event('change'))")

        # Grade = 2
        page.evaluate("document.getElementById('equipWeaponGrade').value = '2'")
        page.evaluate("document.getElementById('equipWeaponGrade').dispatchEvent(new Event('change'))")

        desc = page.evaluate("document.getElementById('equipWeaponDesc').textContent")
        display = page.evaluate("document.getElementById('equipWeaponDesc').style.display")

        print("Description:", repr(desc))
        print("Display:", display)
        assert display == 'block'
        assert "기본공격 데미지%" in desc

        browser.close()

test_desc()
