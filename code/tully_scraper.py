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

    extracted_menu_items = []
    for title in page.query_selector_all("h3.foodmenu__menu-section-title"):
        title_text = title.inner_text()
        print(title_text)
        row = title.query_selector("~ *").query_selector("~ *")
        for item in title.query_selector_all("div.foodmenu__item"):
            item_text = item.inner_text()
            extracted_menu_items.append(extract_menu_item(title_text, item_text))
    menu_items = pd.DataFrame(extracted_menu_items)
    menu_items.to_csv("tullys_menu.csv", index=False)
    context.close()
    browser.close()


with sync_playwright() as playwright:
    tullyscraper(playwright)
