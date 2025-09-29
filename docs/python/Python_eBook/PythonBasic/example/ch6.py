# 第六章：Python類別(Class)概念 - 龍與地下城冒險
# 教學重點：class定義、建立物件、方法使用

print("==========================================")
print("|                                        |")
print("|  歡迎來到 Python 與龍與地下城冒險！    |")
print("|  第六章：類別(Class)概念              |")
print("|                                        |")
print("==========================================")

# 1. 基本類別定義與建立物件
class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 50
        self.level = 1
        self.inventory = []
        
    def show_status(self):
        print(f"\n=== {self.name} 的狀態 ===")
        print(f"等級：{self.level}")
        print(f"生命：{self.hp}")
        print(f"魔力：{self.mp}")
        
    def level_up(self):
        self.level += 1
        self.hp += 20
        self.mp += 10
        print(f"\n{self.name} 升級了！")
        self.show_status()
        
    def add_item(self, item):
        self.inventory.append(item)
        print(f"\n獲得物品：{item}")
        
    def show_inventory(self):
        print(f"\n=== {self.name} 的背包 ===")
        if len(self.inventory) == 0:
            print("背包是空的")
        else:
            for i, item in enumerate(self.inventory):
                print(f"{i+1}. {item}")

# 2. 英雄職業類別
class Warrior(Character):
    def __init__(self, name):
        Character.__init__(self, name)
        self.hp = 150  # 戰士有更多生命值
        self.strength = 15
        
    def attack(self):
        damage = self.strength * self.level
        print(f"\n{self.name} 揮動武器，造成 {damage} 點傷害！")

class Mage(Character):
    def __init__(self, name):
        Character.__init__(self, name)
        self.mp = 100  # 法師有更多魔力值
        self.intelligence = 15
        
    def cast_spell(self):
        damage = self.intelligence * self.level
        print(f"\n{self.name} 施放魔法，造成 {damage} 點傷害！")

# 展示類別使用方式
def demo_game():
    print("\n=== 創建新角色 ===")
    role = input("選擇職業 (1:戰士 2:法師)：")
    name = input("輸入角色名稱：")
    
    if role == "1":
        player = Warrior(name)
        print("\n創建了一名戰士！")
    else:
        player = Mage(name)
        print("\n創建了一名法師！")
    
    # 角色操作展示
    while True:
        print("\n=== 角色操作 ===")
        print("1. 查看狀態")
        print("2. 升級")
        print("3. 戰鬥")
        print("4. 查看背包")
        print("5. 獲得物品")
        print("6. 結束")
        
        choice = input("\n選擇操作：")
        
        if choice == "1":
            player.show_status()
        elif choice == "2":
            player.level_up()
        elif choice == "3":
            if isinstance(player, Warrior):
                player.attack()
            else:
                player.cast_spell()
        elif choice == "4":
            player.show_inventory()
        elif choice == "5":
            item = input("獲得什麼物品？")
            player.add_item(item)
        elif choice == "6":
            break

# 執行遊戲展示
if __name__ == "__main__":
    demo_game()
    print("\n==========================================")
    print("|                                        |")
    print("|       第六章完成！恭喜你！             |")
    print("|    你已經掌握了Python類別的基礎！      |")
    print("|                                        |")
    print("==========================================")
    print("\n在下一章中，我們將學習檔案處理的技巧，")
    print("讓你能夠儲存遊戲進度！")
