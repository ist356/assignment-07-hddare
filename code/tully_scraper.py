import re
from playwright.sync_api import Playwright, sync_playwright
from menuitemextractor import extract_menu_item
from menuitem import MenuItem
import pandas as pd

def tullyscraper(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tullysgoodtimes.com/menus/")
    page.wait_for_selector("div.foodmenu__menu-item", timeout=5000)
    extracted_menu_items = []

    for title in page.query_selector_all("h3.foodmenu__menu-section-title"):
        title_text = title.inner_text()
        print(title_text)
        row = title.query_selector("~ *").query_selector("~ *")
        for item in row.query_selector_all("div.foodmenu__menu-item"):
            item_text = item.inner_text()
            extracted_menu_item = extract_menu_item(title_text, item_text)
            print(f"  Menu item: {extracted_menu_item.name}")
            extracted_menu_items.append(extracted_menu_item.to_dict())
    menu_items = pd.DataFrame(extracted_menu_items)
    menu_items.to_csv("cache/tullys_menu.csv", index=False)
    print(f"Extracted {len(extracted_menu_items)} menu items.")
    print(f"Title: {title.inner_text()}")
    row = title.query_selector("~ *").query_selector("~ *")
    if not row:
        print(f"No row found for title: {title.inner_text()}")


    context.close()
    browser.close()


with sync_playwright() as playwright:
    tullyscraper(playwright)
