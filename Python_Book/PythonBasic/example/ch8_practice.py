import game_character_system as char_sys
import game_item_system as item_sys
import game_combat_system as combat_sys
import game_record_system as record_sys

def main():
    print("=== RPG遊戲系統展示 ===")
    
    # 創建角色
    warrior = char_sys.create_character("戰士小明", "warrior")
    mage = char_sys.create_character("法師小華", "mage")
    
    # 建立物品
    potion = item_sys.create_item("治療藥水", "potion", 50)
    mana = item_sys.create_item("魔力藥水", "mana", 30)
    
    while True:
        print("\n=== 遊戲選單 ===")
        print("1. 查看角色狀態")
        print("2. 使用物品")
        print("3. 進行戰鬥")
        print("4. 儲存遊戲")
        print("5. 讀取遊戲")
        print("6. 結束遊戲")
        
        choice = input("選擇操作：")
        
        if choice == "1":
            char_sys.show_status(warrior)
            char_sys.show_status(mage)
            
        elif choice == "2":
            warrior = item_sys.use_item(potion, warrior)
            mage = item_sys.use_item(mana, mage)
            
        elif choice == "3":
            warrior, mage = combat_sys.battle(warrior, mage)
            
        elif choice == "4":
            record_sys.save_game(warrior, "warrior_save.txt")
            record_sys.save_game(mage, "mage_save.txt")
            
        elif choice == "5":
            warrior = record_sys.load_game("warrior_save.txt")
            mage = record_sys.load_game("mage_save.txt")
            
        elif choice == "6":
            print("遊戲結束！")
            break

if __name__ == "__main__":
    main()
