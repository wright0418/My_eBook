---
marp: true
---

# 第二章：Python 條件判斷與流程控制 - 龍與地下城冒險

## 學習目標
- 掌握條件判斷：`if-elif-else` 結構
- 學習迴圈控制：`while` 和 `for` 迴圈
- 理解流程控制的觀念
- 實作基本的遊戲邏輯控制

## 什麼是條件判斷？

---
marp: true
---

# 第二章：Python 條件判斷與控制流程 - 龍與地下城冒險

## 學習目標
- 掌握條件判斷：`if-elif-else` 結構
- 學習迴圈控制：`while` 和 `for` 迴圈
- 理解程式流程控制的概念
- 實作基本的遊戲邏輯控制

## 條件判斷：if-elif-else

### 基本語法結構
```python
if 條件1:
    # 當條件1為True時執行的程式碼
elif 條件2:
    # 當條件2為True時執行的程式碼
else:
    # 當所有條件都不成立時執行的程式碼
```

### 實例：遇到戰鬥
```python
action = input("你要：1.戰鬥 2.逃跑 3.對話 （請輸入數字）：")

if action == "1":
    print("你掏出武器，準備戰鬥！")
elif action == "2":
    print("你轉身就跑，但哥布林的動作更快...")
elif action == "3":
    print("出口意外地，哥布林會說人類的語言！")
else:
    print("你躊躇不決，哥布林趁機發動攻擊！")
```

### 比較運算符
- `==` 等於
- `!=` 不等於
- `>` 大於
- `<` 小於
- `>=` 大於等於
- `<=` 小於等於

### 邏輯運算符
- `and` 且
- `or` 或
- `not` 非

## while 迴圈

### 基本語法
```python
while 條件:
    # 當條件為True時重複執行的程式碼
```

### 實例：逃出迷宮
```python
steps = 0
escape_steps = 5

while steps < escape_steps:
    move = input(f"還需要{escape_steps - steps}步才能出去。要往前走嗎？(是/否)：")
    if move == "是":
        steps += 1
        print(f"你向前走了一步，已經走了{steps}步。")
    else:
        print("你原地踏步，沒有前進。")
```

### while 迴圈的控制
- `break`: 立即跳出迴圈
- `continue`: 跳過本次迴圈剩餘部分，進入下一次迴圈
- `while...else`: 當迴圈正常結束時執行else區塊

## for 迴圈

### 基本語法
```python
for 變數 in range(開始值, 結束值):
    # 對範圍內的每個數字執行程式碼
```

### 實例：探索洞窟
```python
for room in range(1, 6):  # 從1到5
    print(f"正在探索第{room}號房間")
```

### range() 函數的用法
1. **單一參數**
```python
for i in range(5):  # 0到4
    print(f"這是第{i+1}次嘗試")
```

2. **雙參數**
```python
for level in range(1, 4):  # 1到3
    print(f"現在在第{level}層")
```

3. **三參數**
```python
for count in range(0, 10, 2):  # 0,2,4,6,8
    print(f"計數：{count}")
```

### 常見的for迴圈應用

1. **倒數計時**
```python
for countdown in range(5, 0, -1):
    print(f"還剩{countdown}秒")
```

2. **簡單計步**
```python
for step in range(1, 6):
    print(f"走了{step}步")
```

## 進階流程控制

### 巢狀結構
- 可以在條件判斷或迴圈中再包其它的條件或迴圈。

```python
attempts = 3
found_treasure = False

while attempts > 0 and not found_treasure:
    door = input(f"選擇一扇門 (1/2/3)，還有{attempts}次機會：")
    
    if door == "2":
        print("恭喜你！你找到寶藏！")
        found_treasure = True
    else:
        attempts -= 1
        if attempts > 0:
            print(f"這扇門後什麼都沒有，還有{attempts}次機會。")
        else:
            print("機會用完了，寶藏消失了...")
```

## 實作練習建議
1. **簡單的戰鬥系統**
   - 實作玩家和怪物的回合制戰鬥
   - 使用 while 迴圈控制戰鬥流程
   - 使用 if-elif-else 處理不同的選擇

2. **迷宮探索**
   - 創建一個簡單的迷宮地圖
   - 使用 for 或 while 進行探索
   - 實作簡單的事件觸發

3. **逃脫挑戰**
   - 設計一個倒數計時的挑戰
   - 使用 break 在成功時立即終止迴圈

## 小結

在本章中，我們學習了：
1. 使用 if-elif-else 進行條件判斷
2. 使用 while 迴圈進行重複執行
3. 使用 for 迴圈遍歷序列
4. 結合這些結構實作遊戲邏輯