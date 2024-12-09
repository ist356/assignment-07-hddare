if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from menuitem import MenuItem


def clean_price(price: str) -> float:
    price = price.replace("$", "").replace(",", "").strip()
    return float(price) if price else 0.0

def clean_scraped_text(scraped_text: str) -> list[str]:
    items = scraped_text.split("\n")
    cleaned = []
    for item in items:
        if item in ['GS', "V", "S", "P"]:
            continue
        if item.startswith("NEW"):
            continue
        if len(item.strip()) == 0:
            continue
        cleaned.append(item.strip())
    return cleaned

def extract_menu_item(title: str, scraped_text: str) -> MenuItem:
    cleaned_items = clean_scraped_text(scraped_text)
    if not cleaned_items or len(cleaned_items) < 2:
        raise ValueError(f"Unexpected structure in scraped text: {scraped_text}")
    
    item = MenuItem(category=title, name="", price=0.0, description="")
    try:
        item.name = cleaned_items[0]
        item.price = clean_price(cleaned_items[1])
    except IndexError:
        item.name = cleaned_items[0] if cleaned_items else "Unknown Item"
        item.price = 0.0
        print(f"Missing price for item: {scraped_text}")

    if len(cleaned_items) > 2:
        item.description = cleaned_items[2]
    else:
        item.description = "No description available."
    return item




if __name__=='__main__':
    pass
