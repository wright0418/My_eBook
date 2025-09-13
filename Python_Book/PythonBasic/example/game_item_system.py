def create_item(name, item_type, value):
    item = {
        "name": name,
        "type": item_type,
        "value": value
    }
    return item

def use_item(item, character):
    if item["type"] == "potion":
        character["hp"] += item["value"]
        print(f"{character['name']} 使用 {item['name']}")
        print(f"恢復 {item['value']} 點生命值")
    elif item["type"] == "mana":
        character["mp"] += item["value"]
        print(f"{character['name']} 使用 {item['name']}")
        print(f"恢復 {item['value']} 點魔力值")
    
    return character
