if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price:str) -> float:
    price = price.replace("$", "")
    price = price.replace(",", "")
    return float(price)

def clean_scraped_text(scraped_text: str) -> list[str]:
    items = scraped_text.split("\n")
    cleaned = []
    for item in items:
        if item in ['GS',"V","S","P"]:
            continue
        if item.startswith("NEW"):
            continue
        if len(item.strip()) == 0:
            continue

        cleaned.append(item)

def extract_menu_item(title:str, scraped_text: str) -> MenuItem:
    cleaned = clean_scraped_text(scraped_text)
    item = MenuItem(category=title, name="", price=0.0, description="")
    item.name = cleaned[0]
    item.price = clean_price(cleaned[1])
    if len(cleaned) > 2:
        item.description = cleaned[2]
    else:
        item.description = "No description available."
    return item



if __name__=='__main__':
    pass
