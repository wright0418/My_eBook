---
marp: true
---

# 第四章：Python List(列表)概念 - 龍與地下城冒險

## 學習目標
- 理解List的基本概念
- 學習建立和訪問List
- 掌握List的基本操作
- 使用迴圈處理List

## List基礎

### 什麼是List？
List是Python中最基本的資料結構，可想像成一個可以存放多個物品的背包。

### python list 的寫法說明
```python
# List的基本寫法
empty_list = []  # 建立一個空的List
numbers = [1, 2, 3, 4, 5]  # 建立一個包含數字的List
items = ["劍", "盾", "藥水"]  # 建立一個包含字串的List
mixed = [1, "劍", True]  # 建立一個包含不同類型元素的List
```
### 建立List
```python
# 建立一個包含三個物品的背包
backpack = ["木劍", "治療藥水", "皮甲護甲"]
```
### 訪問List元素
```python
# 取得第一個物品（索引從0開始）
print(f"第一個物品是：{backpack[0]}")  # 木劍
print(f"第二個物品是：{backpack[1]}")  # 治療藥水
```

## List的基本操作

### append() 方法詳解
append() 用於在 List 尾端加入新元素：
```python
# 使用 append() 添加物品
backpack = ["木劍", "治療藥水"]
print(f"原始背包：{backpack}")  # ['木劍', '治療藥水']

backpack.append("皮甲護甲")
print(f"添加後背包：{backpack}")  # ['木劍', '治療藥水', '皮甲護甲']
```

使用時機：
- 撿到新物品時
- 學習新技能時
- 接受新任務時
- 隊伍加入新成員時

### pop() 方法詳解
pop() 有兩種用法：
1. 無參數：移除並回傳最後一個元素
2. 帶索引：移除並回傳指定位置的元素

```python
# 範例 pop() 的兩種用法
backpack = ["木劍", "治療藥水", "皮甲護甲", "火把"]
print(f"原始背包：{backpack}")  
# ['木劍', '治療藥水', '皮甲護甲', '火把']

# 1. 移除最後一個物品
last_item = backpack.pop()
print(f"移除的物品：{last_item}")  # 火把
print(f"移除後背包：{backpack}")   
# ['木劍', '治療藥水', '皮甲護甲']

# 2. 移除指定位置的物品（例如第二個物品，索引為1）
second_item = backpack.pop(1)
print(f"移除的物品：{second_item}")  # 治療藥水
print(f"移除後背包：{backpack}")     
# ['木劍', '皮甲護甲']
```

使用時機：
- 使用消耗品時
- 丟棄物品時
- 完成任務時
- 移除隊伍成員時

注意事項：
1. pop() 會改變原始 List 的內容
2. 對空 List 使用 pop() 會產生錯誤
3. 索引超出範圍也會產生錯誤

安全的使用方式：
```python
# 安全地使用 pop()
backpack = ["木劍"]
if len(backpack) > 0:
    item = backpack.pop()
    print(f"移除了：{item}")
else:
    print("背包是空的！")
```

### 添加元素
```python
# 在背包中添加新物品
backpack.append("火把")
```

### 修改元素
```python
# 升級裝備
backpack[0] = "鐵劍"  # 將木劍換成鐵劍
```

### 移除元素
```python
# 使用pop()移除並回傳最後一個物品
removed_item = backpack.pop()
```

## List基礎操作

### len() 函數
len() 函數用於取得 List 的長度(元素個數)：
```python
backpack = ["木劍", "治療藥水", "皮甲護甲"]
items_count = len(backpack)  # 結果為 3
print(f"背包中有 {items_count} 個物品")
```

常見用途：
1. 檢查背包是否已滿
```python
if len(backpack) >= 10:
    print("背包已經滿了！")
```

2. 搭配for迴圈遍歷
```python
for i in range(len(backpack)):
    print(f"第{i+1}個物品是：{backpack[i]}")
```

3. 檢查背包是否為空
```python
if len(backpack) == 0:
    print("背包是空的！")
```

### List索引說明
- 索引從0開始計數
- 正數索引：0 代表第一個元素，1 代表第二個元素
- 負數索引：-1 代表最後一個元素，-2 代表倒數第二個元素

範例：
```python
backpack = ["木劍", "治療藥水", "皮甲護甲"]
print(backpack[0])    # 顯示："木劍"
print(backpack[-1])   # 顯示："皮甲護甲"
```

## 使用迴圈處理List

### for迴圈遍歷
```python
# 顯示背包中的所有物品
for i in range(len(backpack)):
    print(f"物品{i+1}: {backpack[i]}")
```

## 實作練習：背包管理系統

### 顯示背包內容
```python
def show_backpack(items):
    print("\n=== 背包內容 ===")
    for i in range(len(items)):
        print(f"{i+1}. {items[i]}")
```

### 添加物品
```python
def add_item(items, new_item):
    items.append(new_item)
    return items
```

## 實作練習建議
1. **背包管理系統**
   - 建立背包系統(物品管理)
   - 實作物品的添加和移除
   - 顯示背包內容

2. **技能列表系統**
   - 管理技能的列表
   - 顯示已習得技能
   - 學習新技能

3. **任務清單系統**
   - 記錄進行中的任務
   - 完成任務後移除

## 小結

在本章中，我們學習了：
1. List 的基本概念和建立方法
2. 如何訪問和修改 List 的元素
3. List 的基本操作(添加/移除)
4. 使用迴圈處理 List