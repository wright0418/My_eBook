# 第四章：Python List(列表)概念 - 龍與地下城冒險
# 教學重點：list建立、存取、修改、迴圈訪問

print("==========================================")
print("|                                        |")
print("|  歡迎來到 Python 與龍與地下城冒險！    |")
print("|  第四章：List(列表)概念               |")
print("|                                        |")
print("==========================================")

# 1. 基礎 List 建立和顯示
print("\n1. 創建角色背包")
backpack = ["木劍", "治療藥水", "皮革護甲"]
print("你的背包內容：")
print(f"第1個物品：{backpack[0]}")
print(f"第2個物品：{backpack[1]}")
print(f"第3個物品：{backpack[2]}")

# 2. 使用 for 迴圈遍歷列表
print("\n2. 背包物品檢查")
for i in range(len(backpack)):
    print(f"物品{i+1}: {backpack[i]}")

# 3. 新增和移除物品
print("\n3. 獲得新物品")
backpack.append("火把")
print("你獲得了一個火把！")
print("現在背包內有：")
for i in range(len(backpack)):
    print(f"物品{i+1}: {backpack[i]}")

# 4. 修改列表元素
print("\n4. 升級裝備")
backpack[0] = "鐵劍"
print("你的木劍升級成了鐵劍！")
for i in range(len(backpack)):
    print(f"物品{i+1}: {backpack[i]}")

# 5. 實作簡單背包管理系統
def show_backpack(items):
    print("\n=== 背包內容 ===")
    for i in range(len(items)):
        print(f"{i+1}. {items[i]}")

def add_item(items, new_item):
    items.append(new_item)
    print(f"\n添加了 {new_item} 到背包")
    return items

def remove_item(items, index):
    if index >= 0 and index < len(items):
        removed_item = items.pop(index)
        print(f"\n移除了 {removed_item}")
    return items

# 背包管理系統展示
inventory = ["地圖", "火把", "麵包"]
game_running = True

while game_running:
    print("\n=== 背包管理 ===")
    print("1. 查看背包")
    print("2. 添加物品")
    print("3. 丟棄物品")
    print("4. 結束")
    
    choice = input("請選擇操作：")
    
    if choice == "1":
        show_backpack(inventory)
    elif choice == "2":
        item = input("要添加什麼物品？")
        inventory = add_item(inventory, item)
    elif choice == "3":
        show_backpack(inventory)
        index = int(input("要丟棄第幾個物品？")) - 1
        inventory = remove_item(inventory, index)
    elif choice == "4":
        game_running = False

# 章節總結
print("\n==========================================")
print("|                                        |")
print("|       第四章完成！恭喜你！             |")
print("|    你已經掌握了Python列表的基礎！      |")
print("|                                        |")
print("==========================================")
print("\n在下一章中，我們將學習字典(Dictionary)的使用，")
print("讓你能夠更有效地管理遊戲中的資料！")
