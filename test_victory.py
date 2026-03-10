from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000", wait_until='domcontentloaded')

        # Set basic stats
        page.fill("#finalAttack", "100")
        page.fill("#attackPct", "0")
        page.fill("#advAttackPct", "0")
        page.fill("#skillMultiplier", "100")

        # Select "빅토리" (or whatever item has "기본 타수(배)" and "타수 당 피해량%")
        # The item is "빅토리" (let's check item_data.json)
        # But wait, we can just set eqStats manually via evaluate if we want to test logic,
        # but the logic is inside calculate(). So let's just select the item.
        # First, find the item name.
