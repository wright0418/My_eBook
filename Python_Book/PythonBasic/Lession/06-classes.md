---
marp: true
---

# 第六章：Python類別(Class)概念 - 龍與地下城冒險

## 學習目標
- 理解類別的基本概念
- 學習定義和使用類別
- 掌握物件導向設計的基本技巧
- 實作遊戲角色系統

## 類別基礎

### 什麼是類別？
類別是一種程式設計的模板，可以想像成角色設計圖，定義了角色應該有的屬性和行為。

### 基本類別定義
```python
class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 50
```

### 建立物件
```python
# 建立一個角色
player = Character("勇者")
print(f"角色名稱：{player.name}")
```

## 類別的組成部分

### 建構子 (__init__)
```python
def __init__(self, name):
    self.name = name    # 設定角色名稱
    self.hp = 100      # 設定初始生命值
    self.mp = 50       # 設定初始魔力值
```

### 方法
```python
def show_status(self):
    print(f"=== {self.name} 的狀態 ===")
    print(f"生命值：{self.hp}")
    print(f"魔力值：{self.mp}")
```

## 繼承

### 基本繼承概念
```python
class Warrior(Character):
    def __init__(self, name):
        Character.__init__(self, name)
        self.hp = 150  # 戰士有較多生命值
```

### 特殊方法
```python
def attack(self):
    print(f"{self.name} 使用武器攻擊！")
```

## 物件使用範例：角色系統

### 基本角色類別
```python
class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 50
        self.inventory = []
        
    def show_status(self):
        print(f"=== {self.name} 的狀態 ===")
        print(f"生命值：{self.hp}")
        print(f"魔力值：{self.mp}")
```

### 職業類別
```python
class Warrior(Character):
    def attack(self):
        print(f"{self.name} 揮動劍刃！")

class Mage(Character):
    def cast_spell(self):
        print(f"{self.name} 施放魔法！")
```

### 使用物件
```python
# 建立角色
warrior = Warrior("戰士小明")
mage = Mage("法師小華")

# 使用方法
warrior.show_status()
warrior.attack()

mage.show_status()
mage.cast_spell()
```

## 實作練習建議
1. **角色類別系統**
   - 設計不同職業的類別
   - 實作技能與屬性

2. **道具類別**
   - 設計道具的類別結構
   - 使用道具改變角色屬性

3. **戰鬥系統**
   - 使用類別與方法實作回合制戰鬥

## 小結

在本章中，我們學習了：
1. 類別的基本概念與語法
2. 物件的建立與使用
3. 繼承與方法的定義
4. 使用類別實作遊戲系統