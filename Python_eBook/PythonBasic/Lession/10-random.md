---
marp: true
---

# 第十章：隨機數的使用 - 龍與地下城冒險

## 學習目標
- 理解隨機數的概念與用途
- 學習使用 random 模組
- 設計遊戲中的隨機機制
- 實作隨機事件與掉落系統

## 隨機數基礎

### 為什麼需要隨機數？
在遊戲開發中，隨機數是用來製造變化性與不確定性的關鍵元素。

### random 模組的基本用法
```python
import random

# 產生 1-6 的隨機整數
dice = random.randint(1, 6)

# 產生 0.0-1.0 的隨機浮點數
chance = random.random()

# 從清單中隨機選擇
items = ["劍", "盾", "藥水"]
reward = random.choice(items)
```

## 遊戲中的應用

### 戰鬥系統
```python
def calculate_damage(base_damage):
    multiplier = random.uniform(0.8, 1.2)
    return int(base_damage * multiplier)
```

### 掉落系統
```python
def get_loot():
    if random.random() < 0.3:
        return "稀有物品"
    else:
        return "普通物品"
```

## 進階應用

### 權重掉落系統
```python
def weighted_loot():
    items = {
        "普通": 70,
        "稀有": 25,
        "傳說": 5
    }
    roll = random.randint(1, 100)
    if roll <= 70:
        return "普通"
    elif roll <= 95:
        return "稀有"
    else:
        return "傳說"
```

### 隨機事件系統
```python
def random_event():
    events = [
        "遇到商人",
        "遇到怪物",
        "發現寶箱"
    ]
    return random.choice(events)
```

## 實作練習建議
1. 骰子系統
2. 隨機掉落設計
3. 隨機事件與地圖生成

## 小結

在本章中，我們學習了隨機數在遊戲中的重要應用與實作方式。