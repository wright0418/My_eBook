# 第九章：Python例外處理 - 龍與地下城冒險
# 教學重點：try-except使用、例外處理

print("==========================================")
print("|                                        |")
print("|  歡迎來到 Python 與龍與地下城冒險！    |")
print("|  第九章：例外處理                     |")
print("|                                        |")
print("==========================================")

# 1. 基本例外處理
def use_potion(character, amount):
    try:
        if character["hp"] <= 0:
            raise ValueError("角色已經倒下，無法使用藥水！")
        character["hp"] += amount
        print(f"恢復了 {amount} 點生命值")
    except ValueError as e:
        print(f"錯誤：{e}")
    except:
        print("發生未知錯誤！")

# 2. 檔案操作例外處理
def load_game_data(filename):
    try:
        file = open(filename, "r")
        data = file.read()
        file.close()
        print("讀取成功！")
        return data
    except FileNotFoundError:
        print("找不到存檔檔案！")
        return None
    except:
        print("讀取檔案時發生錯誤！")
        return None

# 3. 數值轉換例外處理
def calculate_damage(base_damage, multiplier):
    try:
        final_damage = int(base_damage) * float(multiplier)
        print(f"計算傷害：{final_damage}")
        return final_damage
    except ValueError:
        print("傷害計算錯誤：請確認輸入的是數字！")
        return 0

# 展示例外處理
def demo_game():
    # 建立測試角色
    player = {"name": "勇者", "hp": 100}
    
    print("\n1. 測試藥水使用")
    use_potion(player, 20)
    player["hp"] = 0
    use_potion(player, 20)
    
    print("\n2. 測試存檔讀取")
    load_game_data("not_exist.txt")
    
    print("\n3. 測試傷害計算")
    calculate_damage(10, 1.5)
    calculate_damage("十", 1.5)

if __name__ == "__main__":
    demo_game()
    print("\n==========================================")
    print("|                                        |")
    print("|       第九章完成！恭喜你！             |")
    print("|    你已經掌握了Python例外處理！        |")
    print("|                                        |")
    print("==========================================")
    print("\n在下一章中，我們將學習更多Python進階技巧，")
    print("讓你的程式設計能力更上一層樓！")
