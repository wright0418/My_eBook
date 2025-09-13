# 第三章：Python函數的定義與使用 - 龍與地下城冒險
# 教學重點：def, return, 參數傳遞

print("==========================================")
print("|                                        |")
print("|  歡迎來到 Python 與龍與地下城冒險！    |")
print("|  第三章：函數的定義與使用             |")
print("|                                        |")
print("==========================================")

# 1. 基本函數定義與呼叫
def 顯示歡迎訊息():
    print("\n親愛的冒險者，歡迎來到魔法學院！")
    print("這裡是你學習函數魔法的起點。")

顯示歡迎訊息()

# 2. 帶參數的函數
def 施放魔法(spell_name):
    print(f"\n開始施放魔法：{spell_name}！")
    print("魔法光芒四射...")
    print(f"{spell_name}施放完成！")

施放魔法("火球術")

# 3. 帶返回值的函數
def 計算傷害值(base_damage):
    final_damage = base_damage * 2
    return final_damage

base_attack = 10
final_damage = 計算傷害值(base_attack)
print(f"\n基礎傷害：{base_attack}")
print(f"最終傷害：{final_damage}")

# 4. 多參數函數
def 進行戰鬥(player_name, monster_name):
    print(f"\n{player_name} VS {monster_name}")
    print("戰鬥開始！")
    
player_name = input("\n請輸入你的名字：")
進行戰鬥(player_name, "哥布林")

# 5. 綜合練習 - 冒險者休息站
def 休息站(player_name, current_hp):
    print(f"\n歡迎來到休息站，{player_name}")
    print(f"你目前的生命值是：{current_hp}")
    
    if current_hp < 50:
        print("你看起來狀態不太好，建議休息一下。")
        rest = input("要休息一下嗎？(是/否)：")
        if rest == "是":
            current_hp = 100
            print("休息後你恢復了全部生命值！")
    
    return current_hp

hp = 30
new_hp = 休息站(player_name, hp)
print(f"離開休息站時的生命值：{new_hp}")

# 章節總結
print("\n==========================================")
print("|                                        |")
print("|       第三章完成！恭喜你！             |")
print("|    你已經掌握了函數的定義與使用！      |")
print("|                                        |")
print("==========================================")

print("\n在下一章中，我們將學習Python的List(列表)概念，")
print("讓你能夠管理背包物品、儲存法術清單，以及創建更豐富的遊戲內容！")
