# 第八章：Python模組系統與import用法 - 龍與地下城冒險
# 教學重點：模組導入、使用模組功能

print("==========================================")
print("|                                        |")
print("|  歡迎來到 Python 與龍與地下城冒險！    |")
print("|  第八章：模組系統與import用法         |")
print("|                                        |")
print("==========================================")

# 1. 導入我們的遊戲模組
print("\n1. 導入角色模組")
import game_character
import game_items
import game_combat

# 2. 使用角色模組
print("\n2. 創建角色")
warrior = game_character.create_warrior("小明")
mage = game_character.create_mage("小華")

# 3. 使用物品模組
print("\n3. 使用物品")
sword = game_items.create_weapon("鐵劍", 10)
potion = game_items.create_potion("治療藥水", 50)

game_items.use_item(potion, warrior)
game_items.equip_weapon(sword, warrior)

# 4. 使用戰鬥模組
print("\n4. 進行戰鬥")
game_combat.battle(warrior, mage)

print("\n==========================================")
print("|                                        |")
print("|       第八章完成！恭喜你！             |")
print("|  你已經掌握了Python模組系統的基礎！    |")
print("|                                        |")
print("==========================================")
print("\n在下一章中，我們將學習Python例外處理，")
print("讓你的程式能夠更好地處理錯誤情況！")
