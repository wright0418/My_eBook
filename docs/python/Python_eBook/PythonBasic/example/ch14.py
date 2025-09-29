# 簡單範例
numbers = [1, 2, 3, 4, 5, 6]

# 過濾出所有偶數
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # 輸出: [2, 4, 6]

# D&D RPG 範例
characters = [
    {"name": "Gandalf", "class": "Wizard", "level": 12, "hp": 60},
    {"name": "Aragorn", "class": "Fighter", "level": 10, "hp": 80},
    {"name": "Legolas", "class": "Ranger", "level": 8, "hp": 70},
    {"name": "Gimli", "class": "Fighter", "level": 10, "hp": 90},
]

# 篩選出所有等級大於等於 10 的角色
high_level_characters = list(filter(lambda character: character["level"] >= 10, characters))

print("高等級角色:")
for character in high_level_characters:
    print(character["name"], character["class"], character["level"], character["hp"])

# 篩選出所有生命值大於 75 的角色
high_hp_characters = list(filter(lambda character: character["hp"] > 75, characters))

print("\n高生命值角色:")
for character in high_hp_characters:
    print(character["name"], character["class"], character["level"], character["hp"])
