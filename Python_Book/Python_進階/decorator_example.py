# 範例 1：記錄日誌
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"執行 {func.__name__} 函數...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} 函數執行完畢")
        return result
    return wrapper

@log_execution
def attack(character, target, damage):
    print(f"{character} 攻擊 {target}，造成 {damage} 點傷害！")

# 範例 2：檢查權限
def check_permission(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if role == "admin":
                print("權限驗證通過")
                return func(*args, **kwargs)
            else:
                print("權限不足")
                return
        return wrapper
    return decorator

@check_permission("admin")
def create_item(item_name):
    print(f"創建道具：{item_name}")

@check_permission("player")
def get_item(item_name):
    print(f"取得道具：{item_name}")

if __name__ == '__main__':
    attack("英雄", "怪物", 10)
    create_item("魔法劍")
    get_item("魔法劍")
