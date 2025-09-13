# 第六章課後挑戰參考解答 - 完整角色系統

# 基礎裝備類別
class Equipment:
    def __init__(self, name, stat_type, value):
        self.name = name
        self.stat_type = stat_type  # "attack" 或 "defense"
        self.value = value
        
    def show_info(self):
        print(f"{self.name}: {self.stat_type} +{self.value}")

# 基礎技能類別
class Skill:
    def __init__(self, name, damage, mp_cost):
        self.name = name
        self.damage = damage
        self.mp_cost = mp_cost
        self.level = 1
    
    def level_up(self):
        self.level += 1
        self.damage += 5
        self.mp_cost += 2

# 基礎角色類別
class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 100
        self.mp = 50
        self.strength = 10
        self.intelligence = 10
        self.skills = []
        self.equipment = {"weapon": None, "armor": None}
        
    def show_status(self):
        print(f"\n=== {self.name} (Lv.{self.level}) ===")
        print(f"HP: {self.hp}")
        print(f"MP: {self.mp}")
        print(f"力量: {self.strength}")
        print(f"智力: {self.intelligence}")
        print("\n裝備:")
        for slot, item in self.equipment.items():
            if item:
                print(f"{slot}: ", end="")
                item.show_info()
            else:
                print(f"{slot}: 無")
                
    def level_up(self):
        self.level += 1
        self.hp += 20
        self.mp += 10
        print(f"\n{self.name} 升級到 {self.level} 級！")
        
    def equip(self, item, slot):
        self.equipment[slot] = item
        print(f"\n{self.name} 裝備了 {item.name}")
        
    def show_skills(self):
        print(f"\n=== {self.name} 的技能 ===")
        for i, skill in enumerate(self.skills):
            print(f"{i+1}. {skill.name} Lv.{skill.level} (傷害:{skill.damage}, MP消耗:{skill.mp_cost})")

# 職業類別：戰士
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 150
        self.strength = 15
        # 戰士初始技能
        self.skills.append(Skill("橫斬", 20, 10))
        
    def attack(self, target):
        weapon_bonus = self.equipment["weapon"].value if self.equipment["weapon"] else 0
        damage = self.strength + weapon_bonus
        print(f"\n{self.name} 攻擊 {target}，造成 {damage} 點傷害！")

# 職業類別：法師
class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 80
        self.mp = 120
        self.intelligence = 15
        # 法師初始技能
        self.skills.append(Skill("火球術", 25, 15))
        
    def cast_spell(self, skill_index, target):
        if skill_index < len(self.skills):
            skill = self.skills[skill_index]
            if self.mp >= skill.mp_cost:
                self.mp -= skill.mp_cost
                damage = skill.damage + self.intelligence
                print(f"\n{self.name} 對 {target} 施放 {skill.name}，造成 {damage} 點傷害！")
            else:
                print("\nMP不足！")

# 職業類別：盜賊
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 100
        self.strength = 12
        # 盜賊初始技能
        self.skills.append(Skill("背刺", 30, 20))
        
    def stealth_attack(self, target):
        weapon_bonus = self.equipment["weapon"].value if self.equipment["weapon"] else 0
        damage = (self.strength + weapon_bonus) * 1.5
        print(f"\n{self.name} 從背後襲擊 {target}，造成 {damage} 點傷害！")

# 遊戲系統展示
def demo_game():
    print("=== 角色系統展示 ===")
    
    # 創建角色
    name = input("輸入角色名稱：")
    print("\n選擇職業：")
    print("1. 戰士")
    print("2. 法師")
    print("3. 盜賊")
    choice = input("你的選擇：")
    
    if choice == "1":
        player = Warrior(name)
    elif choice == "2":
        player = Mage(name)
    else:
        player = Rogue(name)
    
    # 創建一些裝備
    sword = Equipment("鐵劍", "attack", 10)
    staff = Equipment("法杖", "attack", 8)
    armor = Equipment("皮甲", "defense", 5)
    
    # 主選單
    while True:
        print("\n=== 選單 ===")
        print("1. 查看狀態")
        print("2. 升級")
        print("3. 裝備武器")
        print("4. 裝備防具")
        print("5. 查看技能")
        print("6. 升級技能")
        print("7. 結束")
        
        choice = input("選擇操作：")
        
        if choice == "1":
            player.show_status()
        elif choice == "2":
            player.level_up()
        elif choice == "3":
            if isinstance(player, Mage):
                player.equip(staff, "weapon")
            else:
                player.equip(sword, "weapon")
        elif choice == "4":
            player.equip(armor, "armor")
        elif choice == "5":
            player.show_skills()
        elif choice == "6":
            player.show_skills()
            skill_idx = int(input("升級哪個技能？(輸入編號)：")) - 1
            if skill_idx >= 0 and skill_idx < len(player.skills):
                player.skills[skill_idx].level_up()
                print("技能升級成功！")
        elif choice == "7":
            break

if __name__ == "__main__":
    demo_game()
