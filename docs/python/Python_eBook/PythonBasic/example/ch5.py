# 第五章：Python字典(Dictionary)概念 - 龍與地下城冒險
# 教學重點：dict建立、存取、修改、遍歷

print("==========================================")
print("|                                        |")
print("|  歡迎來到 Python 與龍與地下城冒險！    |")
print("|  第五章：字典(Dictionary)概念         |")
print("|                                        |")
print("==========================================")

# 1. 基礎字典建立和顯示
print("\n1. 創建角色屬性")
player = {
    "name": "勇者",
    "hp": 100,
    "mp": 50,
    "level": 1
}

print("角色資料：")
print(f"名稱：{player['name']}")
print(f"生命值：{player['hp']}")
print(f"魔力值：{player['mp']}")
print(f"等級：{player['level']}")

# 2. 修改字典內容
print("\n2. 升級角色")
player['level'] = 2
player['hp'] = 150
print(f"角色升級！現在等級是 {player['level']}")
print(f"生命值提升到 {player['hp']}")

# 3. 新增字典項目
print("\n3. 學習新技能")
player['skill'] = "火球術"
print(f"學會了新技能：{player['skill']}")

# 4. 使用if檢查key是否存在
print("\n4. 檢查角色狀態")
if 'skill' in player:
    print(f"已學會技能：{player['skill']}")
else:
    print("尚未學會任何技能")

# 5. 實作簡單角色管理系統
def show_status(char):
    print("\n=== 角色狀態 ===")
    for key in char:
        print(f"{key}: {char[key]}")

def update_status(char, key, value):
    char[key] = value
    print(f"\n更新了 {key} 為 {value}")
    return char

# 角色管理系統展示
character = {
    "name": "新手冒險者",
    "hp": 100,
    "mp": 50
}

game_running = True
while game_running:
    print("\n=== 角色管理 ===")
    print("1. 查看狀態")
    print("2. 更新屬性")
    print("3. 結束")
    
    choice = input("請選擇操作：")
    
    if choice == "1":
        show_status(character)
    elif choice == "2":
        key = input("要更新什麼屬性？")
        if key in character:
            value = input(f"將 {key} 更新為？")
            character = update_status(character, key, value)
        else:
            print("找不到這個屬性！")
    elif choice == "3":
        game_running = False

# 章節總結
print("\n==========================================")
print("|                                        |")
print("|       第五章完成！恭喜你！             |")
print("|    你已經掌握了Python字典的基礎！      |")
print("|                                        |")
print("==========================================")
print("\n在下一章中，我們將學習類別(Class)的概念，")
print("讓你能夠創建更完整的遊戲角色系統！")
