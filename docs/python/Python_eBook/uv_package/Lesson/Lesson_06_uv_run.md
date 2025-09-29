# Lesson 6: 使用 `uv run` 執行指令

## 什麼是 `uv run`？

`uv run` 是一個強大的指令，它允許你在專案的虛擬環境中執行指令，而**不需要手動啟用 (activate)** 該環境。這讓執行專案腳本或工具變得更加方便和直接。

### `uv run` 的優勢

- **簡化工作流程**：你不需要再記得執行 `source .venv/bin/activate` 或 `.\.venv\Scripts\activate`。
- **避免環境污染**：指令只在 `uv` 管理的虛擬環境中執行，不會影響到你的全域 Python 環境。
- **腳本化更容易**：在 `Makefile` 或 `package.json` 的 `scripts` 中，你可以直接使用 `uv run python my_script.py`，而不用處理啟用腳本的路徑問題。

## 如何使用 `uv run`

假設你的專案結構如下：

```
my_project/
├── .venv/
├── pyproject.toml
└── src/
    └── main.py
```

`pyproject.toml` 內容：

```toml
[project]
name = "my_project"
version = "0.1.0"
dependencies = [
    "requests",
]
```

`src/main.py` 內容：

```python
import requests

def main():
    response = requests.get("https://www.google.com")
    print(f"Status Code: {response.status_code}")

if __name__ == "__main__":
    main()
```

### 執行 Python 腳本

你可以使用以下指令來執行 `main.py`：

```bash
uv run python src/main.py
```

`uv` 會自動偵測到 `.venv` 虛擬環境，並在該環境中執行 `python src/main.py`。即使 `requests` 只安裝在 `.venv` 中，這個指令也能成功執行。

### 執行已安裝的工具

如果你安裝了一個帶有命令列介面的工具（例如 `pytest`），你也可以用 `uv run` 來執行它。

首先，將 `pytest` 加入開發相依性：

```bash
uv pip install --dev pytest
```

然後，你可以這樣執行測試：

```bash
uv run pytest
```

`uv` 會在虛擬環境中找到 `pytest` 並執行它。

## `uv run` 與傳遞參數

你可以像平常一樣向指令傳遞參數。`uv run` 會將 `run` 後面的所有內容都當作要執行的指令和參數。

例如，如果你的腳本接受命令列參數：

`src/greeter.py`:
```python
import sys

def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        greet(sys.argv[1])
    else:
        print("Please provide a name.")
```

你可以這樣執行：

```bash
uv run python src/greeter.py "World"
```

輸出將會是：
```
Hello, World!
```

## 練習

1.  在你的專案中建立一個簡單的 Python 腳本，該腳本匯入一個你已安裝的套件。
2.  使用 `uv run` 來執行這個腳本，確認它能成功執行。
3.  嘗試在不啟用虛擬環境的情況下直接用 `python your_script.py` 執行，觀察會發生什麼錯誤。
4.  將 `black` (一個程式碼格式化工具) 加入你的開發相依性，並使用 `uv run black .` 來格式化你的專案程式碼。
