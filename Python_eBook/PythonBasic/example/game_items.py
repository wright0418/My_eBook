# 物品模組：包含物品創建和使用功能

def create_weapon(name, damage):
    weapon = {
        "name": name,
        "type": "weapon",
        "damage": damage
    }
    print(f"製作了武器：{name}")
    return weapon

def create_potion(name, heal):
    potion = {
        "name": name,
        "type": "potion",
        "heal": heal
    }
    print(f"製作了藥水：{name}")
    return potion

def use_item(item, character):
    if item["type"] == "potion":
        character["hp"] += item["heal"]
        print(f"{character['name']} 使用了 {item['name']}")
        print(f"生命值恢復 {item['heal']} 點")

def equip_weapon(weapon, character):
    character["weapon"] = weapon
    print(f"{character['name']} 裝備了 {weapon['name']}")
