# 戰鬥模組：包含戰鬥相關功能

def calculate_damage(attacker):
    if attacker["type"] == "warrior":
        base_damage = attacker["strength"]
    else:
        base_damage = attacker["magic"]
    
    if attacker["weapon"]:
        base_damage += attacker["weapon"]["damage"]
    
    return base_damage

def battle(char1, char2):
    print(f"\n{char1['name']} VS {char2['name']}")
    print("戰鬥開始！")
    
    damage1 = calculate_damage(char1)
    damage2 = calculate_damage(char2)
    
    print(f"{char1['name']} 造成 {damage1} 點傷害")
    print(f"{char2['name']} 造成 {damage2} 點傷害")
