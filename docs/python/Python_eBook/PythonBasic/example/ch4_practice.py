# 第四章課後挑戰參考解答 - 冒險者管理系統

# 1. 背包系統
def show_inventory(backpack):
    print("\n=== 背包內容 ===")
    for i in range(len(backpack)):
        print(f"{i+1}. {backpack[i]}")

def manage_inventory(backpack):
    while True:
        print("\n背包管理")
        print("1. 查看物品")
        print("2. 添加物品")
        print("3. 使用物品")
        print("4. 返回")
        
        choice = input("選擇操作：")
        if choice == "1":
            show_inventory(backpack)
        elif choice == "2":
            item = input("要添加什麼物品？")
            backpack.append(item)
            print(f"添加了 {item}")
        elif choice == "3":
            if len(backpack) > 0:
                show_inventory(backpack)
                idx = int(input("使用第幾個物品？")) - 1
                if idx >= 0 and idx < len(backpack):
                    used_item = backpack.pop(idx)
                    print(f"使用了 {used_item}")
            else:
                print("背包是空的！")
        elif choice == "4":
            break

# 2. 技能系統
def manage_skills(skills):
    while True:
        print("\n技能管理")
        print("1. 查看技能")
        print("2. 學習技能")
        print("3. 返回")
        
        choice = input("選擇操作：")
        if choice == "1":
            print("\n=== 已學技能 ===")
            for i in range(len(skills)):
                print(f"{i+1}. {skills[i]}")
        elif choice == "2":
            skill = input("要學習什麼技能？")
            skills.append(skill)
            print(f"學會了 {skill}")
        elif choice == "3":
            break

# 3. 隊伍系統
def manage_party(party):
    while True:
        print("\n隊伍管理")
        print("1. 查看隊伍")
        print("2. 添加成員")
        print("3. 移除成員")
        print("4. 返回")
        
        choice = input("選擇操作：")
        if choice == "1":
            print("\n=== 隊伍成員 ===")
            for i in range(len(party)):
                print(f"{i+1}. {party[i]}")
        elif choice == "2":
            member = input("輸入新成員名字：")
            party.append(member)
            print(f"{member} 加入了隊伍")
        elif choice == "3":
            if len(party) > 0:
                for i in range(len(party)):
                    print(f"{i+1}. {party[i]}")
                idx = int(input("移除哪位成員？")) - 1
                if idx >= 0 and idx < len(party):
                    removed = party.pop(idx)
                    print(f"{removed} 離開了隊伍")
        elif choice == "4":
            break

# 4. 任務系統
def manage_quests(quests):
    while True:
        print("\n任務管理")
        print("1. 查看任務")
        print("2. 接受任務")
        print("3. 完成任務")
        print("4. 返回")
        
        choice = input("選擇操作：")
        if choice == "1":
            print("\n=== 進行中的任務 ===")
            for i in range(len(quests)):
                print(f"{i+1}. {quests[i]}")
        elif choice == "2":
            quest = input("輸入新任務名稱：")
            quests.append(quest)
            print(f"接受了任務：{quest}")
        elif choice == "3":
            if len(quests) > 0:
                for i in range(len(quests)):
                    print(f"{i+1}. {quests[i]}")
                idx = int(input("完成了哪個任務？")) - 1
                if idx >= 0 and idx < len(quests):
                    completed = quests.pop(idx)
                    print(f"完成了任務：{completed}")
        elif choice == "4":
            break

# 主系統
def main():
    print("===== 冒險者管理系統 =====")
    player_name = input("請輸入冒險者名字：")
    
    backpack = ["木劍", "治療藥水"]
    skills = ["基本攻擊"]
    party = [player_name]
    quests = []
    
    while True:
        print(f"\n歡迎，{player_name}！")
        print("1. 背包管理")
        print("2. 技能管理")
        print("3. 隊伍管理")
        print("4. 任務管理")
        print("5. 結束遊戲")
        
        choice = input("選擇要管理的系統：")
        if choice == "1":
            manage_inventory(backpack)
        elif choice == "2":
            manage_skills(skills)
        elif choice == "3":
            manage_party(party)
        elif choice == "4":
            manage_quests(quests)
        elif choice == "5":
            print("遊戲結束！")
            break

if __name__ == "__main__":
    main()
