# Lesson 02 — 安裝與快速上手（約30分鐘）

## 目標
- 安裝 pytest
- 了解如何在專案中組織測試檔案
- 執行基本測試並解讀輸出

## 重點
- 使用 pip 安裝 pytest（例如：`pip install pytest`）
- 測試檔命名規則（test_*.py 或 *_test.py）
- 基本 pytest 命令：`pytest`, `pytest -q`, `pytest -k <expr>`

## 實作練習
1. 安裝 pytest：

```powershell
pip install pytest
```

2. 在專案中建立 `tests` 目錄，並將 `test_sample.py` 放入其中。
3. 在命令列執行 `pytest -q`，並觀察輸出。
4. 使用 `pytest -k add` 只執行與 `add` 有關的測試。

## 小結
- 安裝與執行測試非常簡單，pytest 的命令列工具能快速回饋測試結果。