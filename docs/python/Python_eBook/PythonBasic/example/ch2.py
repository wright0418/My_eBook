# 第二章：Python條件判斷與控制流程 - 龍與地下城冒險續集
# 教學重點：if-elif-else, while迴圈, for迴圈

print("==========================================")
print("|                                        |")
print("|  歡迎回到 Python 與龍與地下城冒險！    |")
print("|  第二章：條件判斷與控制流程           |")
print("|                                        |")
print("==========================================")

# 載入冒險者資料
player_name = input("\n請輸入你的名字以繼續冒險：")
print(f"歡迎回來，{player_name}！")

# 1. if-elif-else 條件判斷示範
print("\n1. 遭遇戰鬥！")
print("你在森林中遇到了一隻哥布林！")
action = input("你要：1.戰鬥 2.逃跑 3.對話 (請輸入數字)：")

if action == "1":
    print("你拔出武器，準備戰鬥！")
elif action == "2":
    print("你轉身就跑，但是哥布林的動作更快...")
elif action == "3":
    print("出乎意料地，哥布林會說人類的語言！")
else:
    print("你猶豫不決，哥布林趁機發動攻擊！")

# 2. while迴圈示範
print("\n2. 逃出迷宮")
steps = 0
escape_steps = 5

print("你發現自己在一個迷宮中，需要找到出口...")
while steps < escape_steps:
    move = input(f"還需要{escape_steps - steps}步才能出去。要往前走嗎？(是/否)：")
    if move == "是":
        steps += 1
        print(f"你向前走了一步，已經走了{steps}步。")
    else:
        print("你原地踏步，沒有前進。")

print("恭喜你成功逃出迷宮！")

# 3. for迴圈示範
print("\n3. 探索洞窟")
print("你發現了一個神秘的洞窟，決定探索五個房間...")

for room in range(1, 6):
    print(f"\n正在探索第{room}號房間")
    explore = input("要仔細搜索這個房間嗎？(是/否)：")
    if explore == "是":
        print(f"你在第{room}號房間發現了一些寶物！")
    else:
        print("你快速地通過了這個房間。")

print("你完成了洞窟的探索！")

# 綜合練習
print("\n4. 最終挑戰")
print("你面前有三扇門，其中一扇通向寶藏！")

attempts = 3
found_treasure = False

while attempts > 0 and not found_treasure:
    door = input(f"\n選擇一扇門 (1/2/3)，還有{attempts}次機會：")
    
    if door == "2":
        print("恭喜你！你找到了寶藏！")
        found_treasure = True
    else:
        attempts -= 1
        if attempts > 0:
            print(f"這扇門後什麼都沒有，還有{attempts}次機會。")
        else:
            print("機會用完了，寶藏消失了...")

# 章節總結
print("\n==========================================")
print("|                                        |")
print("|       第二章完成！恭喜你！             |")
print("|    你已經掌握了條件判斷與控制流程！    |")
print("|                                        |")
print("==========================================")
print("\n在下一章中，我們將學習函數的定義與使用，讓你的冒險更加精彩！")
