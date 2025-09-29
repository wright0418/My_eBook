import random

print("==========================================")
print("|                                        |")
print("|  歡迎來到 Python 與龍與地下城冒險！    |")
print("|  第十章：隨機數的使用                 |")
print("|                                        |")
print("==========================================")

# 1. 基本隨機數生成
def roll_dice(sides):
    result = random.randint(1, sides)
    print(f"骰出了 {result} 點")
    return result

# 2. 隨機戰鬥傷害
def calculate_damage(base_damage):
    multiplier = random.uniform(0.8, 1.2)
    final_damage = int(base_damage * multiplier)
    print(f"基礎傷害 {base_damage} 造成了 {final_damage} 點傷害")
    return final_damage

# 3. 隨機掉落系統
def get_random_loot():
    items = ["治療藥水", "魔力藥水", "銀幣", "鐵劍", "皮革護甲"]
    item = random.choice(items)
    print(f"獲得了 {item}！")
    return item

# 4. 隨機事件系統
def random_encounter():
    events = [
        "遇到商人",
        "遭遇怪物",
        "發現寶箱",
        "找到休息處",
        "什麼都沒發生"
    ]
    event = random.choice(events)
    print(f"發生了：{event}")
    return event

# 展示隨機數功能
def game_demo():
    print("\n=== 擲骰子 ===")
    roll_dice(6)   # 一般骰子
    roll_dice(20)  # D20骰子
    
    print("\n=== 戰鬥傷害 ===")
    calculate_damage(50)
    calculate_damage(100)
    
    print("\n=== 尋寶系統 ===")
    for _ in range(3):
        get_random_loot()
    
    print("\n=== 隨機探索 ===")
    for _ in range(3):
        random_encounter()

if __name__ == "__main__":
    game_demo()
    print("\n==========================================")
    print("|                                        |")
    print("|       第十章完成！恭喜你！             |")
    print("|    你已經掌握了Python隨機數的使用！    |")
    print("|                                        |")
    print("==========================================")
