# Lesson 03 — 基本測試編寫與斷言（約30分鐘）

## 目標
- 學會撰寫測試函數
- 使用不同類型的斷言
- 學會讀懂 pytest 的失敗訊息

## 重點
- 測試函數和命名：`def test_xxx():`
- 常見斷言形式：`assert x == y`, `assert x in y`, `with pytest.raises(...)`
- 測試組織：setup/teardown 的基礎概念（在下一堂課用 fixture 深入介紹）

## 實作練習
1. 建立 `test_math.py`：

```python
# test_math.py

def multiply(a, b):
    return a * b


def test_multiply_positive():
    assert multiply(3, 4) == 12


def test_multiply_zero():
    assert multiply(0, 5) == 0
```

2. 嘗試讓一個測試故意失敗，觀察 pytest 的錯誤輸出並說明失敗原因。
3. 使用 `pytest.raises` 測試例外情況。

## 小結
- 斷言是測試的核心，pytest 的錯誤輸出對於除錯非常有幫助。