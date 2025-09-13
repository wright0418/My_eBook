# 第七章：Python檔案處理技巧 - 龍與地下城冒險存檔
# 教學重點：檔案讀寫、存檔功能實作

print("==========================================")
print("|                                        |")
print("|  歡迎來到 Python 與龍與地下城冒險！    |")
print("|  第七章：檔案處理技巧                 |")
print("|                                        |")
print("==========================================")

# 1. 基本檔案寫入
def save_character(character_name, level, hp, mp):
    file = open("game_save.txt", "w")
    file.write(f"角色名稱：{character_name}\n")
    file.write(f"等級：{level}\n")
    file.write(f"生命值：{hp}\n")
    file.write(f"魔力值：{mp}\n")
    file.close()
    print("角色資料已儲存！")

# 2. 基本檔案讀取
def load_character():
    try:
        file = open("game_save.txt", "r")
        data = file.readlines()
        file.close()
        print("\n讀取角色資料：")
        for line in data:
            print(line.strip())
        return True
    except:
        print("找不到存檔資料！")
        return False

# 3. 追加寫入
def add_item_to_inventory(item):
    file = open("inventory.txt", "a")
    file.write(f"{item}\n")
    file.close()
    print(f"已將 {item} 加入背包記錄")

# 4. 讀取背包內容
def show_inventory():
    try:
        file = open("inventory.txt", "r")
        items = file.readlines()
        file.close()
        print("\n背包內容：")
        for i, item in enumerate(items):
            print(f"{i+1}. {item.strip()}")
    except:
        print("背包是空的！")

# 主程式展示
def game_demo():
    while True:
        print("\n=== 遊戲選單 ===")
        print("1. 建立新角色")
        print("2. 讀取角色")
        print("3. 添加物品")
        print("4. 查看背包")
        print("5. 結束遊戲")
        
        choice = input("選擇操作：")
        
        if choice == "1":
            name = input("角色名稱：")
            level = 1
            hp = 100
            mp = 50
            save_character(name, level, hp, mp)
            
        elif choice == "2":
            load_character()
            
        elif choice == "3":
            item = input("要添加什麼物品？")
            add_item_to_inventory(item)
            
        elif choice == "4":
            show_inventory()
            
        elif choice == "5":
            print("遊戲結束！")
            break

if __name__ == "__main__":
    game_demo()
    print("\n==========================================")
    print("|                                        |")
    print("|       第七章完成！恭喜你！             |")
    print("|    你已經掌握了Python檔案處理技巧！    |")
    print("|                                        |")
    print("==========================================")
