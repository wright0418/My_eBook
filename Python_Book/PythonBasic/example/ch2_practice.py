# 第二章課後挑戰參考解答 - 簡單冒險遊戲

# 遊戲初始化
print("===== Python RPG 冒險遊戲 =====")
player_name = input("請輸入你的名字：")
hp = 100
gold = 0
current_room = 1
game_running = True

# 主遊戲迴圈
while game_running:
    # 顯示當前狀態
    print(f"\n{'-'*30}")
    print(f"位置：第 {current_room} 號房間")
    print(f"生命值：{hp}")
    print(f"金幣：{gold}")
    print(f"{'-'*30}")
    
    # 玩家選項
    print("\n你要：")
    print("1. 探索房間")
    print("2. 進入戰鬥")
    print("3. 休息恢復")
    print("4. 儲存進度")
    print("5. 結束遊戲")
    choice = input("請選擇行動(1-5)：")

    # 處理玩家選擇
    if choice == "1":  # 探索房間
        print("\n開始探索房間...")
        for i in range(3):
            print(f"搜索中...({i+1}/3)")
        found_gold = current_room * 5
        gold += found_gold
        print(f"你發現了 {found_gold} 金幣！")
        
        # 移動到下一個房間
        next_room = input("\n要前往下一個房間嗎？(是/否)：")
        if next_room == "是":
            current_room += 1
            print(f"你進入了第 {current_room} 號房間")

    elif choice == "2":  # 戰鬥系統
        print("\n遭遇怪物！")
        monster_hp = 50
        while monster_hp > 0 and hp > 0:
            print(f"\n怪物血量：{monster_hp}")
            print(f"你的血量：{hp}")
            action = input("選擇：1.攻擊 2.逃跑：")
            
            if action == "1":
                damage = 20
                monster_hp -= damage
                print(f"你造成 {damage} 點傷害！")
                if monster_hp > 0:
                    hp -= 10
                    print("怪物反擊，你失去10點生命！")
            else:
                print("你成功逃脫了！")
                break
                
        if monster_hp <= 0:
            print("你打敗了怪物！")
            gold += 30

    elif choice == "3":  # 休息恢復
        if gold >= 10:
            gold -= 10
            hp = 100
            print("你在旅店休息，恢復了所有生命值！")
        else:
            print("你沒有足夠的金幣支付住宿費...")

    elif choice == "4":  # 儲存進度
        print("\n=== 儲存進度 ===")
        print(f"玩家：{player_name}")
        print(f"目前位置：第 {current_room} 號房間")
        print(f"生命值：{hp}")
        print(f"金幣：{gold}")
        print("進度已儲存！")

    elif choice == "5":  # 結束遊戲
        print(f"\n遊戲結束！")
        print(f"最終狀態：")
        print(f"探索到第 {current_room} 號房間")
        print(f"收集了 {gold} 金幣")
        game_running = False

    # 檢查遊戲結束條件
    if hp <= 0:
        print("\n你的生命值耗盡了...")
        print("遊戲結束！")
        game_running = False
