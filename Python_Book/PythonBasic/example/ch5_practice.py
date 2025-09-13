# 第五章課後挑戰參考解答 - RPG管理系統

# 1. 角色屬性系統
def manage_character(character):
    while True:
        print("\n=== 角色管理 ===")
        print("1. 查看屬性")
        print("2. 提升屬性")
        print("3. 返回")
        
        choice = input("選擇操作：")
        if choice == "1":
            print("\n角色屬性：")
            for key in character:
                print(f"{key}: {character[key]}")
        elif choice == "2":
            stat = input("要提升哪個屬性？")
            if stat in character and stat != "name":
                value = int(character[stat]) + 10
                character[stat] = value
                print(f"{stat}提升至{value}")
        elif choice == "3":
            break
    return character

# 2. 道具管理系統
def manage_items(inventory):
    while True:
        print("\n=== 道具管理 ===")
        print("1. 查看道具")
        print("2. 添加道具")
        print("3. 使用道具")
        print("4. 返回")
        
        choice = input("選擇操作：")
        if choice == "1":
            print("\n道具列表：")
            for item in inventory:
                print(f"- {item['name']}：{item['effect']} ({item['value']})")
        elif choice == "2":
            name = input("道具名稱：")
            effect = input("效果說明：")
            value = input("效果數值：")
            inventory.append({
                "name": name,
                "effect": effect,
                "value": value
            })
            print(f"添加了{name}")
        elif choice == "3":
            if len(inventory) > 0:
                print("\n可用道具：")
                for i, item in enumerate(inventory):
                    print(f"{i+1}. {item['name']}")
                idx = int(input("使用第幾個道具？")) - 1
                if idx >= 0 and idx < len(inventory):
                    used = inventory.pop(idx)
                    print(f"使用了{used['name']}，{used['effect']}")
        elif choice == "4":
            break
    return inventory

# 3. 技能系統
def manage_skills(skills):
    while True:
        print("\n=== 技能管理 ===")
        print("1. 查看技能")
        print("2. 學習技能")
        print("3. 升級技能")
        print("4. 返回")
        
        choice = input("選擇操作：")
        if choice == "1":
            print("\n技能列表：")
            for skill in skills:
                print(f"- {skill['name']} Lv.{skill['level']}: {skill['effect']}")
        elif choice == "2":
            name = input("技能名稱：")
            effect = input("技能效果：")
            skills.append({
                "name": name,
                "level": 1,
                "effect": effect
            })
            print(f"學會了{name}")
        elif choice == "3":
            if len(skills) > 0:
                print("\n可升級技能：")
                for i, skill in enumerate(skills):
                    print(f"{i+1}. {skill['name']} Lv.{skill['level']}")
                idx = int(input("升級第幾個技能？")) - 1
                if idx >= 0 and idx < len(skills):
                    skills[idx]['level'] += 1
                    print(f"{skills[idx]['name']}升級到{skills[idx]['level']}等")
        elif choice == "4":
            break
    return skills

# 4. 任務追蹤系統
def manage_quests(quests):
    while True:
        print("\n=== 任務管理 ===")
        print("1. 查看任務")
        print("2. 接受任務")
        print("3. 更新進度")
        print("4. 返回")
        
        choice = input("選擇操作：")
        if choice == "1":
            print("\n任務列表：")
            for quest in quests:
                print(f"- {quest['name']}：{quest['progress']}/{quest['target']}")
        elif choice == "2":
            name = input("任務名稱：")
            target = int(input("目標數量："))
            quests.append({
                "name": name,
                "progress": 0,
                "target": target
            })
            print(f"接受了任務：{name}")
        elif choice == "3":
            if len(quests) > 0:
                print("\n進行中的任務：")
                for i, quest in enumerate(quests):
                    print(f"{i+1}. {quest['name']} ({quest['progress']}/{quest['target']})")
                idx = int(input("更新第幾個任務？")) - 1
                if idx >= 0 and idx < len(quests):
                    progress = int(input("當前進度："))
                    quests[idx]['progress'] = progress
                    if progress >= quests[idx]['target']:
                        completed = quests.pop(idx)
                        print(f"完成任務：{completed['name']}")
                    else:
                        print(f"更新進度：{progress}/{quests[idx]['target']}")
        elif choice == "4":
            break
    return quests

# 主系統
def main():
    print("===== RPG管理系統 =====")
    player_name = input("請輸入角色名稱：")
    
    # 初始化各系統資料
    character = {
        "name": player_name,
        "hp": 100,
        "mp": 50,
        "str": 10,
        "int": 10
    }
    
    inventory = [
        {"name": "治療藥水", "effect": "回復50生命", "value": "50"},
        {"name": "魔力藥水", "effect": "回復30魔力", "value": "30"}
    ]
    
    skills = [
        {"name": "基本攻擊", "level": 1, "effect": "造成10點傷害"}
    ]
    
    quests = [
        {"name": "收集草藥", "progress": 0, "target": 5}
    ]
    
    # 主選單
    while True:
        print(f"\n歡迎，{player_name}！")
        print("1. 角色屬性")
        print("2. 道具管理")
        print("3. 技能系統")
        print("4. 任務追蹤")
        print("5. 結束遊戲")
        
        choice = input("選擇要管理的系統：")
        if choice == "1":
            character = manage_character(character)
        elif choice == "2":
            inventory = manage_items(inventory)
        elif choice == "3":
            skills = manage_skills(skills)
        elif choice == "4":
            quests = manage_quests(quests)
        elif choice == "5":
            print("遊戲結束！")
            break

if __name__ == "__main__":
    main()
