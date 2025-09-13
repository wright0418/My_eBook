---
marp: true
---

# 第九章：Python 例外處理 - 龍與地下城冒險

## 學習目標
- 理解例外處理的概念與用途
- 學習使用 try-except 結構
- 掌握常見的例外類型
- 實作安全的遊戲功能

## 例外處理基礎

### 什麼是例外處理？
例外處理用於管理程式執行時可能發生的錯誤，讓程式能優雅處理問題而不崩潰。

### 基本語法範例
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("發生除以零錯誤！")
except Exception:
    print("發生未預期的錯誤！")
```

### 指定例外類型
```python
try:
    file = open("save.txt", "r")
except FileNotFoundError:
    print("找不到檔案！")
except Exception:
    print("發生其他錯誤！")
```

## 例外處理的應用

### 檔案操作
```python
def load_game_data():
    try:
        with open("save.txt", "r") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print("找不到存檔！")
        return None
```

### 數值轉換
```python
def get_player_level():
    try:
        level = int(input("輸入等級："))
        return level
    except ValueError:
        print("請輸入有效的數字！")
        return 1
```

## 進階使用

### raise 拋出例外
```python
def use_item(item, character):
    if character["hp"] <= 0:
        raise ValueError("角色已經倒下！")
```

### try-except-else-finally 結構
```python
def save_game():
    file = None
    try:
        file = open("save.txt", "w")
        file.write("遊戲資料")
    except Exception:
        print("儲存失敗！")
    finally:
        if file:
            file.close()
```

## 實作練習建議
1. 安全的檔案操作
2. 使用者輸入驗證
3. 遊戲錯誤防護設計

## 小結

在本章中，我們學習了例外處理的基本概念、常見用法與實務應用，讓遊戲系統更穩健。