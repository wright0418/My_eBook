# Lesson 5: 項目創建和管理

## 學習目標
- 使用 `uv` 初始化一個現代 Python 專案
- 了解 `pyproject.toml` 的基本結構
- 在專案中管理依賴並執行程式碼

## 內容
現在我們要建造整個房子了！`uv` 可以幫助我們建立一個結構良好、易於管理的專案。

### 初始化新專案
```bash
uv init my-awesome-project
```

這會創建一個新資料夾 `my-awesome-project`，並在其中生成一個 `pyproject.toml` 檔案。這是現代 Python 專案的標準設定檔。

### `pyproject.toml` 檔案解析
打開 `pyproject.toml`，你會看到類似這樣的結構：
```toml
[project]
name = "my-awesome-project"
version = "0.1.0"
description = "Add your description here."
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```
- `[project]`: 定義了專案的名稱、版本和**相依性**。
- `dependencies`: 這是一個列表，用來存放你的專案直接需要的套件。

### 在專案中添加依賴
`uv` 不會像 `poetry` 或 `pdm` 那樣自動修改 `pyproject.toml`。你需要手動管理它，然後使用 `uv` 來安裝。

1.  **手動編輯 `pyproject.toml`**，將 `requests` 和 `flask` 加入 `dependencies` 列表：
    ```toml
    # ...
    dependencies = [
        "requests",
        "flask",
    ]
    # ...
    ```

2.  **安裝依賴**：
    在專案根目錄下，建立虛擬環境並安裝 `pyproject.toml` 中定義的所有依賴。
    ```bash
    # 建立 .venv 虛擬環境
    uv venv
    
    # 安裝 pyproject.toml 中定義的依賴
    uv pip install -e .
    ```
    `-e .` 表示以「可編輯模式」安裝目前專案。這讓 `uv` 知道這是一個專案，並根據 `pyproject.toml` 來安裝依賴。

### 查看專案依賴樹
```bash
uv pip tree
```
這個指令會以樹狀圖顯示專案的完整依賴關係。

### 在專案環境中執行程式碼
使用 `uv run` 指令，可以在不啟用虛擬環境的情況下，直接在專案的環境中執行指令。

1.  創建一個簡單的 `src/main.py`：
    ```python
    # src/main.py
    import flask
    import requests

    print(f"Flask version: {flask.__version__}")
    print(f"Requests version: {requests.__version__}")
    ```

2.  執行它：
    ```bash
    uv run python src/main.py
    ```
    `uv` 會自動找到 `.venv` 環境並在其中執行你的腳本。

## 互動練習
1. 使用 `uv init` 創建一個名為 `hello_uv` 的新專案。
2. 編輯 `pyproject.toml`，加入 `cowsay` 作為依賴。
3. 執行 `uv venv` 和 `uv pip install -e .` 來設定環境。
4. 創建一個 `src/main.py`，`import cowsay` 並使用 `cowsay.cow("Hello UV!")` 來印出訊息。
5. 使用 `uv run python src/main.py` 執行你的腳本。
6. 執行 `uv pip tree` 查看依賴。

## 生活比喻
`pyproject.toml` 就像房子的設計藍圖。你先在藍圖上規劃好需要哪些主要建材 (`dependencies`)，然後叫 `uv` 這個施工隊 (`uv pip install`) 一次性地把所有東西都準備好。

## 課程總結
恭喜你完成了 UV Package 入門教學！

你現在知道如何：
- 安裝和使用 `uv`
- 管理虛擬環境
- 使用 `requirements.in` 和 `pyproject.toml` 管理依賴
- 創建和運行一個結構化的 Python 專案

繼續練習，將 `uv` 應用到你的日常 Python 開發中。快樂編程！