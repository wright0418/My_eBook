def create_character(name, role):
    character = {
        "name": name,
        "role": role,
        "level": 1,
        "exp": 0,
        "hp": 100,
        "mp": 50
    }
    
    if role == "warrior":
        character["hp"] = 150
        character["strength"] = 15
    elif role == "mage":
        character["mp"] = 100
        character["magic"] = 15
    
    return character

def level_up(character):
    character["level"] += 1
    character["hp"] += 20
    character["mp"] += 10
    if character["role"] == "warrior":
        character["strength"] += 5
    elif character["role"] == "mage":
        character["magic"] += 5
    return character

def show_status(character):
    print(f"\n=== {character['name']} 狀態 ===")
    for key, value in character.items():
        print(f"{key}: {value}")
