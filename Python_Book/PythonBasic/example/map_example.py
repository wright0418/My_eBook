# D&D RPG 範例：使用 Map 函數計算攻擊傷害

import random

# 角色攻擊力
attack_damage = [5, 10, 15, 20]

# 怪物防禦力
monster_armor = 2

# 使用亂數決定五次的比例
random_ratios = [random.uniform(0.5, 1.5) for _ in range(len(attack_damage))]

# 使用 map 函數計算每次攻擊造成的傷害，並考慮亂數比例
damage_dealt = map(lambda damage, ratio: max(0, int((damage * ratio) - monster_armor)), attack_damage, random_ratios)

# 輸出每次攻擊造成的傷害
print(list(damage_dealt))
