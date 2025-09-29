# 安全的遊戲系統示範

def validate_input(prompt, valid_options):
    while True:
        try:
            choice = input(prompt)
            if choice in valid_options:
                return choice
            raise ValueError(f"無效的選擇！請輸入：{', '.join(valid_options)}")
        except ValueError as e:
            print(f"錯誤：{e}")

def safe_number_input(prompt, min_value=0, max_value=100):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            raise ValueError(f"數值必須在 {min_value} 到 {max_value} 之間！")
        except ValueError:
            print("錯誤：請輸入有效的數字！")

def safe_file_operation(filename, operation="r", default_value=None):
    try:
        with open(filename, operation) as file:
            if operation == "r":
                return file.read()
            elif operation == "w":
                file.write(str(default_value))
                return True
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 {filename}")
        return default_value
    except PermissionError:
        print(f"錯誤：沒有權限存取檔案 {filename}")
        return default_value
    except:
        print("錯誤：檔案操作時發生未知錯誤")
        return default_value

class GameLogicError(Exception):
    pass

def use_item(character, item):
    try:
        if character["hp"] <= 0:
            raise GameLogicError("角色已經倒下，無法使用物品！")
        if item["count"] <= 0:
            raise GameLogicError("物品數量不足！")
        
        if item["type"] == "potion":
            character["hp"] = min(character["hp"] + item["value"], character["max_hp"])
            item["count"] -= 1
            print(f"使用 {item['name']}，恢復 {item['value']} 點生命值")
        else:
            raise GameLogicError("無法使用此類型的物品！")
            
    except GameLogicError as e:
        print(f"錯誤：{e}")
    except KeyError as e:
        print(f"錯誤：物品或角色資料不完整！缺少 {e}")
    except:
        print("錯誤：使用物品時發生未知錯誤")

def game_demo():
    # 示範安全的遊戲系統
    print("=== 安全的遊戲系統展示 ===")
    
    # 1. 安全的選單系統
    print("\n1. 選單系統")
    choice = validate_input(
        "選擇行動 (1:戰鬥 2:物品 3:存檔 4:讀檔)：",
        ["1", "2", "3", "4"]
    )
    
    # 2. 安全的數值輸入
    print("\n2. 屬性設定")
    level = safe_number_input("輸入等級 (1-99)：", 1, 99)
    print(f"設定等級為：{level}")
    
    # 3. 安全的檔案操作
    print("\n3. 存檔系統")
    save_data = {"level": level, "exp": 100}
    if safe_file_operation("save.txt", "w", save_data):
        print("存檔成功！")
    
    loaded_data = safe_file_operation("save.txt", "r")
    print(f"讀取存檔：{loaded_data}")
    
    # 4. 安全的遊戲邏輯
    print("\n4. 物品系統")
    character = {
        "name": "勇者",
        "hp": 50,
        "max_hp": 100
    }
    
    potion = {
        "name": "治療藥水",
        "type": "potion",
        "value": 30,
        "count": 1
    }
    
    # 正常使用物品
    use_item(character, potion)
    # 嘗試使用已用完的物品
    use_item(character, potion)
    
    # 設定角色死亡狀態
    character["hp"] = 0
    use_item(character, potion)

if __name__ == "__main__":
    game_demo()
    print("\n遊戲系統展示完成！")
