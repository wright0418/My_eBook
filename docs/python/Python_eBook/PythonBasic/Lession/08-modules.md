---
marp: true
---

# 第八章：Python 模組系統與 import 用法 - 龍與地下城冒險

## 學習目標
- 理解模組的概念與用途
- 學習如何導入模組
- 掌握模組的組織方式
- 實作模組化遊戲系統

## 模組基礎

### 什麼是模組？
模組是一個包含Python定義和陳述式的檔案，可以在其他Python程式中重複使用。

### 基本 import 用法
```python
import game_character
import game_items
```

### 使用模組功能
```python
warrior = game_character.create_warrior("勇者")
sword = game_items.create_weapon("鐵劍", 10)
```

## 模組開發

### 建立模組
```python
# game_character.py
def create_warrior(name):
    warrior = {
        "name": name,
        "hp": 100
    }
    return warrior
```

### 模組化設計
- 將相關功能歸類到同一模組
- 每個模組專注於特定功能
- 保持模組之間的獨立性

## 實作練習建議

1. **角色模組**
   - 設計角色建立功能
   - 屬性管理功能

2. **道具模組**
   - 道具建立、使用與管理

3. **戰鬥模組**
   - 戰鬥邏輯與計算

## 小結

在本章中，我們學習了：
1. 模組的基本概念與使用方式
2. 如何建立並導入模組
3. 模組化設計的原則
4. 使用模組構建遊戲系統