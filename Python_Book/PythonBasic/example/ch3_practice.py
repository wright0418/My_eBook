# 第三章課後挑戰參考解答

# 1. 戰鬥系統參考解答
def attack(player_name, monster_name, player_atk):
    print(f"\n{player_name}對{monster_name}發動攻擊！")
    final_damage = player_atk * 2
    print(f"造成了{final_damage}點傷害！")
    return final_damage

def defense(player_name, incoming_damage):
    print(f"\n{player_name}採取防禦姿態")
    reduced_damage = incoming_damage // 2
    print(f"傷害減少一半，受到{reduced_damage}點傷害！")
    return reduced_damage

def heal(player_name, current_hp):
    heal_amount = 30
    new_hp = current_hp + heal_amount
    if new_hp > 100:
        new_hp = 100
    print(f"\n{player_name}使用治療魔法")
    print(f"恢復了{heal_amount}點生命值！")
    return new_hp

def show_status(player_name, hp, mp):
    print("\n角色狀態")
    print("=" * 20)
    print(f"名稱：{player_name}")
    print(f"生命：{hp}/100")
    print(f"魔力：{mp}/50")
    print("=" * 20)

# 2. 對話系統參考解答
def npc_talk(npc_type, player_name):
    if npc_type == "商人":
        print("\n商人：「歡迎光臨！今天想買些什麼？」")
        choice = input("1.購物 2.詢問情報 3.離開：")
        if choice == "1":
            return "開始購物"
        elif choice == "2":
            return "獲得情報"
        else:
            return "離開商店"
            
    elif npc_type == "村長":
        print(f"\n村長：「啊，{player_name}，你終於來了！」")
        choice = input("1.接受任務 2.回報任務 3.閒聊：")
        return f"選擇了選項{choice}"

# 展示範例
def main():
    print("===== 歡迎來到 Python RPG =====")
    player_name = input("\n請輸入你的名字：")
    hp = 100
    mp = 50
    
    # 顯示初始狀態
    show_status(player_name, hp, mp)
    
    # 戰鬥展示
    print("\n遭遇哥布林！")
    monster_hp = 50
    
    while monster_hp > 0 and hp > 0:
        print("\n選擇行動：")
        action = input("1.攻擊 2.防禦 3.治療 4.查看狀態：")
        
        if action == "1":
            damage = attack(player_name, "哥布林", 10)
            monster_hp -= damage
        elif action == "2":
            defense(player_name, 15)
        elif action == "3":
            hp = heal(player_name, hp)
        elif action == "4":
            show_status(player_name, hp, mp)
        
        if monster_hp <= 0:
            print("\n哥布林被打敗了！")
            break
    
    # 對話展示
    print("\n戰鬥結束後，你回到村莊...")
    result = npc_talk("商人", player_name)
    print(f"對話結果：{result}")

# 執行展示
if __name__ == "__main__":
    main()
