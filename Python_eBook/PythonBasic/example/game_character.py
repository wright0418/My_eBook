# 角色模組：包含角色創建和屬性管理

def create_warrior(name):
    warrior = {
        "name": name,
        "type": "warrior",
        "hp": 100,
        "strength": 15,
        "weapon": None
    }
    print(f"創建了戰士 {name}")
    return warrior

def create_mage(name):
    mage = {
        "name": name,
        "type": "mage",
        "hp": 70,
        "magic": 15,
        "weapon": None
    }
    print(f"創建了法師 {name}")
    return mage
