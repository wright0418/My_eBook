# Lesson 04 — 進階功能：參數化與 Fixture（約30分鐘）

## 目標
- 使用參數化測試覆蓋多種情況
- 使用 fixture 準備與清理測試環境
- 了解如何整合 coverage 工具檢查測試覆蓋率

## 重點
- `@pytest.mark.parametrize` 的用法
- `@pytest.fixture` 的作用與 scope 選項
- 使用 `pytest --maxfail=1 --disable-warnings -q` 篩選輸出
- 基本 coverage 工具整合（例如：`coverage run -m pytest`）

## 實作練習
1. 建立 `test_param.py`：

```python
# test_param.py
import pytest


def is_even(n):
    return n % 2 == 0


@pytest.mark.parametrize("input,expected", [
    (2, True),
    (3, False),
    (0, True),
    (-1, False),
])
def test_is_even(input, expected):
    assert is_even(input) == expected
```

2. 建立 `conftest.py` 並加入一個簡單的 fixture：

```python
# conftest.py
import pytest


@pytest.fixture
def sample_data():
    return {"a": 1, "b": 2}
```

3. 在測試中使用 `sample_data` fixture。
4. 使用 coverage 檢查測試覆蓋率。

## 小結
- 參數化與 fixture 能讓測試更簡潔且具可重用性；將 coverage 整合能幫助你了解測試覆蓋情況。