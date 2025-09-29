import random

# 1. 隨機戰鬥系統
def battle_system(player, monster):
    print(f"\n=== 戰鬥：{player['name']} vs {monster['name']} ===")
    
    # 計算傷害
    def calculate_damage(attacker):
        base_damage = attacker['attack']
        # 20%機率暴擊（1.5倍傷害）
        if random.random() < 0.2:
            print("暴擊！")
            return int(base_damage * 1.5)
        # 一般傷害（0.8-1.2倍浮動）
        return int(base_damage * random.uniform(0.8, 1.2))
    
    # 計算迴避
    def check_dodge(defender):
        return random.random() < defender['dodge']
    
    while player['hp'] > 0 and monster['hp'] > 0:
        # 玩家回合
        if not check_dodge(monster):
            damage = calculate_damage(player)
            monster['hp'] -= damage
            print(f"{player['name']}造成 {damage} 點傷害")
        else:
            print(f"{monster['name']}迴避了攻擊！")
            
        if monster['hp'] <= 0:
            print(f"\n{player['name']}獲勝！")
            return True
            
        # 怪物回合
        if not check_dodge(player):
            damage = calculate_damage(monster)
            player['hp'] -= damage
            print(f"{monster['name']}造成 {damage} 點傷害")
        else:
            print(f"{player['name']}迴避了攻擊！")
            
        if player['hp'] <= 0:
            print(f"\n{monster['name']}獲勝！")
            return False

# 2. 寶物掉落系統
def loot_system():
    def generate_item():
        # 決定物品稀有度
        rarity = weighted_random({
            "普通": 70,
            "稀有": 25,
            "傳說": 5
        })
        
        # 根據稀有度決定物品類型和屬性
        items = {
            "普通": ["木劍", "皮甲", "小藥水"],
            "稀有": ["鐵劍", "鋼甲", "大藥水"],
            "傳說": ["魔劍", "龍鱗甲", "全復藥"]
        }
        
        item_name = random.choice(items[rarity])
        bonus = random.randint(1, 5) if rarity == "稀有" else \
                random.randint(6, 10) if rarity == "傳說" else 0
                
        return {
            "name": item_name,
            "rarity": rarity,
            "bonus": bonus
        }
    
    return generate_item()

# 3. 隨機事件系統
def event_system():
    events = {
        "戰鬥": 40,    # 40%機率
        "寶箱": 30,    # 30%機率
        "商人": 20,    # 20%機率
        "空房間": 10   # 10%機率
    }
    
    event = weighted_random(events)
    print(f"\n進入了新的房間...")
    print(f"遭遇：{event}")
    return event

# 4. 隨機地圖產生器
def generate_map(size):
    map_data = []
    for y in range(size):
        row = []
        for x in range(size):
            # 決定地形：0=路, 1=牆, 2=寶箱, 3=怪物
            if x == 0 and y == 0:
                tile = 0  # 起點
            elif x == size-1 and y == size-1:
                tile = 0  # 終點
            else:
                weights = {0: 60, 1: 20, 2: 10, 3: 10}
                tile = int(weighted_random(weights))
            row.append(tile)
        map_data.append(row)
    return map_data

# 輔助函數：根據權重隨機選擇
def weighted_random(weights):
    items = list(weights.keys())
    weights = list(weights.values())
    total = sum(weights)
    r = random.randint(1, total)
    for i, w in enumerate(weights):
        r -= w
        if r <= 0:
            return items[i]

# 主程式展示
def main():
    # 創建玩家和怪物
    player = {
        "name": "勇者",
        "hp": 100,
        "attack": 20,
        "dodge": 0.2
    }
    
    monster = {
        "name": "哥布林",
        "hp": 80,
        "attack": 15,
        "dodge": 0.1
    }
    
    print("=== 隨機遊戲系統展示 ===")
    
    # 展示地圖生成
    print("\n1. 隨機地圖")
    map_data = generate_map(5)
    tiles = {0: "路", 1: "牆", 2: "寶", 3: "怪"}
    for row in map_data:
        print(" ".join(tiles[tile] for tile in row))
    
    # 展示隨機事件
    print("\n2. 隨機事件")
    for _ in range(3):
        event_system()
    
    # 展示戰鬥系統
    print("\n3. 戰鬥系統")
    battle_system(player, monster)
    
    # 展示寶物掉落
    print("\n4. 寶物掉落")
    for _ in range(3):
        item = loot_system()
        print(f"獲得：{item['rarity']} {item['name']} (+{item['bonus']})")

if __name__ == "__main__":
    main()
