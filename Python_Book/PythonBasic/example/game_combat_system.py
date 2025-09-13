def calculate_damage(attacker):
    if attacker["role"] == "warrior":
        return attacker["strength"] * 2
    elif attacker["role"] == "mage":
        return attacker["magic"] * 3

def battle(char1, char2):
    print(f"\n=== 戰鬥開始 ===")
    print(f"{char1['name']} VS {char2['name']}")
    
    damage1 = calculate_damage(char1)
    damage2 = calculate_damage(char2)
    
    char2["hp"] -= damage1
    char1["hp"] -= damage2
    
    print(f"{char1['name']} 造成 {damage1} 點傷害")
    print(f"{char2['name']} 造成 {damage2} 點傷害")
    
    return char1, char2
