from playwright.sync_api import sync_playwright

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('http://localhost:8000/index.html')

        # Test 1: Artifact 9 (Sugar's Maple Tree) not affected by max unique button
        # Set a manual value first
        page.fill('#artifact_9', '5')
        page.click('text="유니크 이하 최대레벨 설정"')
        assert page.input_value('#artifact_9') == '5', "Artifact 9 should not be affected by max button"

        # Test 2: Attack Speed minimum
        # It's initially 1
        assert page.input_value('#atkSpeed') == '1', "Attack speed default should be 1"
        # Enter 0 and trigger calculate
        page.fill('#atkSpeed', '0')
        page.evaluate("calculate()")
        assert page.input_value('#atkSpeed') == '1', "Attack speed should correct to 1"

        # Test 3: Labels changed
        content = page.content()
        assert "기본공격 또는 스킬 계수 (%)" in content
        assert "노크리 기본공격" in content
        assert "크리 기본공격" in content

        # Test 4: Toggle hides buttons
        assert page.is_visible('#equipBtnGroup'), "Equip button group initially visible"
        page.click('#equipArrow') # Toggle off
        assert not page.is_visible('#equipBtnGroup'), "Equip button group should be hidden"

        page.screenshot(path="screenshot.png", full_page=True)
        browser.close()
        print("All tests passed.")

if __name__ == '__main__':
    test()
