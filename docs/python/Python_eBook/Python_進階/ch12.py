"""
Python帶參數的裝飾器進階教學 - 範例代碼
這個文件包含第12章中的所有裝飾器範例，以RPG遊戲為背景
"""
import time
import random
from functools import wraps


# 範例1：技能冷卻時間裝飾器
def cooldown(seconds):
    def decorator(func):
        last_called = {}
        
        @wraps(func)
        def wrapper(character, *args, **kwargs):
            current_time = time.time()
            if character in last_called and current_time - last_called[character] < seconds:
                remaining = seconds - (current_time - last_called[character])
                print(f"{character}的技能 {func.__name__} 還在冷卻中，剩餘 {remaining:.1f} 秒")
                return None
            
            result = func(character, *args, **kwargs)
            last_called[character] = current_time
            return result
        
        return wrapper
    return decorator


# 範例2：技能消耗與效果增強裝飾器
def skill_effect(mp_cost, boost_percentage=0):
    def decorator(func):
        @wraps(func)
        def wrapper(character, target, *args, **kwargs):
            # 假設character是具有mp屬性的對象
            if hasattr(character, "mp") and character.mp >= mp_cost:
                character.mp -= mp_cost
                print(f"{character.name} 消耗 {mp_cost} 魔力值")
                
                # 如果有增益效果
                original_damage = func(character, target, *args, **kwargs)
                if boost_percentage > 0 and original_damage:
                    boost_amount = original_damage * (boost_percentage / 100)
                    total_damage = original_damage + boost_amount
                    print(f"技能增益: +{boost_percentage}%, 總傷害: {total_damage}")
                    return total_damage
                return original_damage
            else:
                print(f"{character.name if hasattr(character, 'name') else character} 魔力不足！")
                return 0
                
        return wrapper
    return decorator


# 範例3：日誌裝飾器
def log_skill(func):
    @wraps(func)
    def wrapper(character, target, *args, **kwargs):
        print(f"[記錄] {character.name} 正在對 {target} 使用 {func.__name__}")
        result = func(character, target, *args, **kwargs)
        print(f"[記錄] {func.__name__} 技能效果結束")
        return result
    return wrapper


# 範例4：暴擊機率裝飾器
def critical_chance(chance_percentage):
    def decorator(func):
        @wraps(func)
        def wrapper(character, target, *args, **kwargs):
            is_critical = random.randint(1, 100) <= chance_percentage
            
            result = func(character, target, *args, **kwargs)
            
            if result and is_critical:
                critical_damage = result * 2
                print(f"暴擊！傷害加倍: {result} → {critical_damage}")
                return critical_damage
            return result
        return wrapper
    return decorator


# 角色類別定義
class Character:
    def __init__(self, name, mp=100):
        self.name = name
        self.mp = mp
        
    def __str__(self):
        return f"{self.name} (MP: {self.mp})"


# 定義技能函數
@cooldown(5)
def fire_ball(character, target):
    print(f"{character} 向 {target} 釋放了火球術，造成100點傷害！")
    return 100

@cooldown(2)
def quick_slash(character, target):
    print(f"{character} 對 {target} 使用快速斬擊，造成50點傷害！")
    return 50

@skill_effect(mp_cost=30, boost_percentage=20)
def lightning_strike(character, target):
    base_damage = 80
    print(f"{character.name} 對 {target} 施放閃電打擊，造成 {base_damage} 點基礎傷害")
    return base_damage

@skill_effect(mp_cost=10)
def heal(character, target):
    heal_amount = 50
    print(f"{character.name} 對 {target} 施放治療，恢復 {heal_amount} 點生命值")
    return heal_amount

@log_skill
@critical_chance(30)
@skill_effect(mp_cost=25, boost_percentage=10)
def frost_nova(character, target):
    base_damage = 70
    print(f"{character.name} 釋放冰霜新星，對 {target} 造成 {base_damage} 點冰霜傷害")
    return base_damage


# 新增裝飾器示範：元素傷害增強
def elemental_boost(element, boost_against=None, boost_percentage=50):
    """
    元素系技能傷害增強裝飾器
    element: 技能元素類型 (火、水、風、土)
    boost_against: 特別有效的敵人類型
    boost_percentage: 對特定敵人的傷害提升百分比
    """
    def decorator(func):
        @wraps(func)
        def wrapper(character, target, *args, **kwargs):
            result = func(character, target, *args, **kwargs)
            
            # 檢查是否對特定敵人類型有傷害加成
            if boost_against and boost_against in target:
                boosted_damage = result * (1 + boost_percentage / 100)
                print(f"{element}系技能對{boost_against}特別有效! 傷害提升{boost_percentage}%")
                print(f"最終傷害: {boosted_damage}")
                return boosted_damage
                
            print(f"使用了{element}系技能，無特殊效果")
            return result
        return wrapper
    return decorator


# 使用新裝飾器的技能
@elemental_boost("火", "植物", 100)
@skill_effect(mp_cost=40)
def flame_burst(character, target):
    base_damage = 120
    print(f"{character.name} 對 {target} 釋放烈焰爆發，造成 {base_damage} 點火焰傷害")
    return base_damage


# 測試函數
def test_cooldown_skills():
    print("\n==== 測試技能冷卻效果 ====")
    fire_ball("魔法師", "哥布林")
    fire_ball("魔法師", "哥布林")  # 應該顯示冷卻中
    quick_slash("戰士", "史萊姆")
    quick_slash("戰士", "史萊姆")  # 應該顯示冷卻中
    print("等待2秒...")
    time.sleep(2)
    quick_slash("戰士", "史萊姆")  # 冷卻已過，可以再次使用
    fire_ball("魔法師", "哥布林")  # 仍在冷卻中


def test_skill_effects():
    print("\n==== 測試技能消耗與效果 ====")
    wizard = Character("巫師", mp=100)
    warrior = Character("戰士", mp=5)
    
    print(f"初始狀態: {wizard}, {warrior}")
    lightning_strike(wizard, "巨龍")  # 成功施放，有20%加成
    heal(wizard, "戰士")  # 成功施放治療
    lightning_strike(wizard, "巨龍")  # 魔力不足
    lightning_strike(warrior, "史萊姆")  # 魔力不足
    print(f"最終狀態: {wizard}, {warrior}")


def test_decorator_chain():
    print("\n==== 測試裝飾器鏈 ====")
    mage = Character("法師", mp=100)
    frost_nova(mage, "獸人群")
    print(f"法師剩餘魔力: {mage.mp}")


def test_elemental_boost():
    print("\n==== 測試元素傷害增強 ====")
    pyromancer = Character("火焰法師", mp=100)
    
    # 測試對普通敵人
    flame_burst(pyromancer, "石頭怪")
    
    # 測試對特殊敵人類型(植物)
    flame_burst(pyromancer, "植物怪")
    
    print(f"火焰法師剩餘魔力: {pyromancer.mp}")


# 主函數
if __name__ == "__main__":
    print("Python裝飾器RPG範例")
    print("=" * 40)
    
    # 執行各項測試
    test_cooldown_skills()
    test_skill_effects()
    test_decorator_chain()
    test_elemental_boost()
    
    print("\n所有測試完成!")
