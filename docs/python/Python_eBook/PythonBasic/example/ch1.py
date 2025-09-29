# 第一章：Python 基礎入門 - 龍與地下城冒險
# 教學重點：input(), print() 和 f-string

# 歡迎訊息
print("==========================================")
print("|                                        |")
print("|  歡迎來到 Python 與龍與地下城冒險！    |")
print("|  讓我們開始你的程式設計與冒險之旅      |")
print("|                                        |")
print("==========================================")

# 基本輸出 - print() 函數
print("\n1. 基本輸出")
print("你眼前出現了一位神秘的法師...")
print("法師說：「歡迎來到Python的奇幻世界，勇敢的冒險者！」")
print("法師說：「在這個世界中，你將學習強大的程式魔法。」")

# 多行文字輸出
print("""
法師拿出一本古老的魔法書，上面寫著：
「Python是一種強大而靈活的程式語言，
 它簡單易學，卻能創造無窮的可能性。」
""")

# 基本輸入 - input() 函數
print("\n2. 基本輸入")
print("法師問道：「在我們開始冒險前，請告訴我你的名字。」")
player_name = input("請輸入你的名字：")
print("法師點頭說道：「啊，" + player_name + "，一個注定成為傳奇的名字！」")

# 創建角色
print("\n3. 創建你的角色")
print("法師說：「現在，讓我們創建你的冒險角色。」")

# 使用input()獲取更多玩家資訊
character_race = input("選擇你的種族 (人類/精靈/矮人/半獸人)：")
character_class = input("選擇你的職業 (戰士/法師/盜賊/牧師)：")

# 顯示角色資訊
print("\n角色創建完成！")
print("名稱：" + player_name)
print("種族：" + character_race)
print("職業：" + character_class)

# 使用 f-string 進行字串格式化
print("\n4. 使用f-string進行字串格式化")
print("法師手指輕點魔法書，一道光芒閃過...")

# 基本的f-string用法
print(f"法師說：「偉大的{character_race} {character_class}啊，歡迎你，{player_name}！」")

# 為角色設定一些初始屬性值
strength = 10
intelligence = 10
dexterity = 10
charisma = 10

# 根據職業調整屬性值
if character_class.lower() == "戰士":
    strength += 5
elif character_class.lower() == "法師":
    intelligence += 5
elif character_class.lower() == "盜賊":
    dexterity += 5
elif character_class.lower() == "牧師":
    charisma += 5

# 使用f-string顯示角色屬性
print("\n角色屬性：")
print(f"力量: {strength}")
print(f"智力: {intelligence}")
print(f"敏捷: {dexterity}")
print(f"魅力: {charisma}")

# f-string進階格式化 - 數值格式
health = 100
mana = 50
print(f"\n生命值: {health}/100 ({health}%)")
print(f"魔力值: {mana}/100 ({mana}%)")

# f-string進階格式化 - 對齊
print("\n角色屬性卡：")
print(f"{'屬性':<10}{'數值':>5}")
print(f"{'-'*15}")
print(f"{'力量':<10}{strength:>5}")
print(f"{'智力':<10}{intelligence:>5}")
print(f"{'敏捷':<10}{dexterity:>5}")
print(f"{'魅力':<10}{charisma:>5}")

# 使用f-string進行計算
level = 1
exp_needed = level * 100
print(f"\n當前等級: {level}")
print(f"升級所需經驗: {exp_needed}")

# 冒險開始
print("\n5. 你的冒險開始了")
first_quest = input("你接受法師的第一個任務嗎？(是/否)：")

if first_quest.lower() == "是":
    print(f"\n法師微笑著說：「太好了！勇敢的{player_name}，你的Python冒險之旅正式開始！」")
    print(f"「記住你學到的知識：print()可以輸出信息，input()可以獲取輸入，")
    print(f"而f-string可以讓你更優雅地格式化字符串。」")
    print("「這些將是你在Python世界冒險的基礎魔法。」")
else:
    print(f"\n法師看起來有些失望：「我理解，{player_name}。也許你需要時間考慮。")
    print("不過，你已經學會了基本的Python魔法：print(), input()和f-string。")
    print("希望不久後能再見到你。」")

# 章節總結
print("\n==========================================")
print("|                                        |")
print("|       第一章完成！恭喜你！             |")
print("|  你已經學會了Python的基礎輸入與輸出    |")
print("|                                        |")
print("==========================================")
print("\n在下一章中，我們將學習條件判斷與控制流程，讓你的冒險更加豐富多彩！")