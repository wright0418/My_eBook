---
marp: true
---

# 第七章：Python 檔案處理技巧 - 龍與地下城冒險

## 學習目標
- 理解檔案處理的基本概念
- 學習讀寫文字檔案
- 掌握檔案錯誤處理
- 實作遊戲存檔系統

## 什麼是檔案處理？
檔案處理是指對電腦檔案進行讀取、寫入、修改和刪除等操作的過程。透過檔案處理，我們可以將程式產生的資料儲存到檔案中，或是將檔案中的資料讀取到程式中，以便進行後續的處理。

## 為什麼要學習檔案處理？
學習檔案處理可以讓我們的程式具備永久儲存資料的能力，避免因為程式結束而導致資料遺失。此外，透過檔案處理，我們還可以方便地與其他程式或使用者分享資料。

## 如何讀取檔案
在 Python 中，我們可以使用內建的 `open()` 函式來開啟一個檔案，並回傳一個檔案物件（file object）。透過這個檔案物件，我們就可以對檔案進行各種操作，例如讀取檔案內容、寫入資料等等。

### 讀取文字檔案
以下是一個讀取文字檔案的範例：
```python
# 開啟檔案
file = open('example.txt', 'r', encoding='utf-8')

# 讀取檔案內容
content = file.read()

# 關閉檔案
file.close()

# 顯示檔案內容
print(content)
```
在這個範例中，我們使用 `open()` 函式開啟一個名為 `example.txt` 的檔案，並指定檔案的編碼為 UTF-8。接著，我們使用檔案物件的 `read()` 方法來讀取檔案的全部內容，然後將其儲存到變數 `content` 中。最後，我們關閉檔案並印出檔案內容。

### 逐行讀取檔案
如果檔案的內容非常龐大，一次讀取全部內容可能會佔用過多的記憶體空間。這時候，我們可以考慮逐行讀取檔案：
```python
# 開啟檔案
file = open('example.txt', 'r', encoding='utf-8')

# 逐行讀取檔案
for line in file:
    # 處理每一行的資料
    print(line.strip())

# 關閉檔案
file.close()
```
在這個範例中，我們使用 `for` 迴圈逐行讀取檔案的內容，並對每一行的資料進行處理（例如去除行末的換行符號）。

## 如何寫入檔案
除了讀取檔案之外，我們還可以將資料寫入檔案。在 Python 中，我們可以使用檔案物件的 `write()` 方法將資料寫入檔案：
```python
# 開啟檔案
file = open('output.txt', 'w', encoding='utf-8')

# 寫入資料
file.write('Hello, world!\n')
file.write('Welcome to the world of Python file handling.\n')

# 關閉檔案
file.close()
```
在這個範例中，我們開啟一個名為 `output.txt` 的檔案，並使用 `write()` 方法將兩行文字寫入檔案。請注意，若檔案已存在，則原有的內容將會被覆蓋。

## 檔案錯誤處理
在檔案處理的過程中，可能會發生各種錯誤，例如檔案不存在、檔案無法讀取等等。為了避免程式異常終止，我們需要對這些錯誤進行處理。在 Python 中，我們可以使用 `try` 和 `except` 來捕捉和處理例外狀況：
```python
try:
    # 嘗試開啟檔案
    file = open('example.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    # 處理檔案不存在的錯誤
    print('檔案不存在！')
else:
    # 讀取檔案內容
    content = file.read()
    # 關閉檔案
    file.close()
    # 顯示檔案內容
    print(content)
```
在這個範例中，我們嘗試開啟一個檔案，如果檔案不存在，就會觸發 `FileNotFoundError` 例外，我們可以在 `except` 區塊中處理這個錯誤。若檔案成功開啟，我們就讀取檔案內容並關閉檔案。

## 實作遊戲存檔系統
檔案處理在遊戲開發中非常重要，特別是當我們需要儲存和讀取遊戲進度時。以下是一個簡單的遊戲存檔系統範例：
```python
# 遊戲進度資料
save_data = {
    'player_name': '勇者',
    'level': 10,
    'experience': 2500,
}

# 儲存遊戲進度
def save_game(data):
    try:
        with open('savefile.txt', 'w', encoding='utf-8') as file:
            for key, value in data.items():
                file.write(f'{key}:{value}\n')
    except Exception as e:
        print(f'儲存遊戲進度時發生錯誤：{e}')

# 讀取遊戲進度
def load_game():
    try:
        with open('savefile.txt', 'r', encoding='utf-8') as file:
            data = {}
            for line in file:
                key, value = line.strip().split(':')
                data[key] = value
            return data
    except Exception as e:
        print(f'讀取遊戲進度時發生錯誤：{e}')
        return None

# 測試儲存和讀取遊戲進度
save_game(save_data)
loaded_data = load_game()
print(loaded_data)
```
在這個範例中，我們定義了 `save_game()` 和 `load_game()` 兩個函式，分別用於儲存和讀取遊戲進度。儲存遊戲進度時，我們將玩家名稱、關卡和經驗值等資料寫入檔案；讀取遊戲進度時，我們從檔案中讀取資料並轉換為字典格式。

## 小結
本章介紹了檔案處理的基本概念和技巧，包括如何讀取和寫入檔案、檔案錯誤處理以及實作遊戲存檔系統。檔案處理在程式設計中非常重要，掌握檔案處理技巧將有助於我們開發出更完善的應用程式。