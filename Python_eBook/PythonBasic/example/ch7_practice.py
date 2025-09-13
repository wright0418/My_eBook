# 第七章課後挑戰參考解答 - 遊戲存檔系統

# 存檔處理函數
def save_game(slot, character, inventory, progress):
    # 建立存檔名稱
    filename = f"save_slot_{slot}.txt"
    
    try:
        file = open(filename, "w")
        # 寫入角色資料
        file.write("=== 角色資料 ===\n")
        for key, value in character.items():
            file.write(f"{key}：{value}\n")
            
        # 寫入背包資料
        file.write("\n=== 背包內容 ===\n")
        for item in inventory:
            file.write(f"{item}\n")
            
        # 寫入遊戲進度
        file.write("\n=== 遊戲進度 ===\n")
        file.write(f"當前章節：{progress['chapter']}\n")
        file.write(f"當前位置：{progress['location']}\n")
        file.write(f"完成任務：{progress['completed_quests']}\n")
        
        file.close()
        print(f"\n遊戲已儲存到存檔欄位 {slot}")
        return True
    except:
        print("\n存檔失敗！")
        return False

def load_game(slot):
    filename = f"save_slot_{slot}.txt"
    
    try:
        file = open(filename, "r")
        data = file.readlines()
        file.close()
        
        print(f"\n讀取存檔欄位 {slot}：")
        for line in data:
            print(line.strip())
        return True
    except:
        print(f"\n找不到存檔欄位 {slot}")
        return False

# 遊戲系統展示
def game_demo():
    # 初始化遊戲資料
    character = {
        "名稱": "勇者",
        "等級": 1,
        "生命值": 100,
        "魔力值": 50,
        "金幣": 100
    }
    
    inventory = ["木劍", "治療藥水", "皮革護甲"]
    
    progress = {
        "chapter": "第一章",
        "location": "新手村",
        "completed_quests": 0
    }
    
    while True:
        print("\n=== 遊戲選單 ===")
        print("1. 查看角色資料")
        print("2. 查看背包")
        print("3. 儲存遊戲")
        print("4. 讀取遊戲")
        print("5. 進行遊戲")
        print("6. 結束遊戲")
        
        choice = input("選擇操作：")
        
        if choice == "1":
            print("\n角色資料：")
            for key, value in character.items():
                print(f"{key}：{value}")
                
        elif choice == "2":
            print("\n背包內容：")
            for i, item in enumerate(inventory):
                print(f"{i+1}. {item}")
                
        elif choice == "3":
            slot = input("\n選擇存檔欄位 (1-3)：")
            save_game(slot, character, inventory, progress)
            
        elif choice == "4":
            slot = input("\n選擇存檔欄位 (1-3)：")
            load_game(slot)
            
        elif choice == "5":
            # 模擬遊戲進行
            print("\n進行遊戲...")
            character["等級"] += 1
            inventory.append("銀幣")
            progress["completed_quests"] += 1
            print("角色升級！獲得一個銀幣！完成一個任務！")
            
        elif choice == "6":
            print("\n遊戲結束！")
            break

if __name__ == "__main__":
    game_demo()
