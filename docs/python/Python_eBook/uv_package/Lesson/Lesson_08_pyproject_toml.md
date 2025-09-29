# Lesson 8: 與 `pyproject.toml` 的整合

`pyproject.toml` 是現代 Python 專案的標準設定檔，用於定義專案的元資料、建置系統、相依性等。`uv` 與 `pyproject.toml` 緊密整合，使其成為管理專案的理想工具。

## `uv` 如何使用 `pyproject.toml`

`uv` 會自動偵測並讀取專案根目錄下的 `pyproject.toml` 檔案。它主要關注 `[project]` 和 `[tool.uv]` 這兩個區塊。

### `[project]` 區塊

這是 PEP 621 標準化的區塊，`uv` 從中讀取專案的相依性。

`pyproject.toml`:
```toml
[project]
name = "my-awesome-project"
version = "0.1.0"
description = "一個很棒的專案"
requires-python = ">=3.8"

# 主要相依性
dependencies = [
    "fastapi>=0.100.0",
    "pydantic<3",
]

[project.optional-dependencies]
# 可選相依性 (開發環境用)
dev = [
    "pytest",
    "ruff",
]
# 可選相依性 (文件產生用)
docs = [
    "sphinx",
]
```

當你執行 `uv pip install -e .` 或 `uv sync` (如果使用 `uv pip compile pyproject.toml`) 時，`uv` 會：
- 讀取 `dependencies` 列表並安裝這些套件。
- 如果你指定了 extras (例如 `uv pip install -e ".[dev,docs]"`), `uv` 會安裝 `optional-dependencies` 中對應的套件。

### `[tool.uv]` 區塊 (可選)

你可以在 `pyproject.toml` 中為 `uv` 設定一些專屬的配置，這樣就不需要在每次執行指令時都加上旗標。

`pyproject.toml`:
```toml
# ... [project] 區塊 ...

[tool.uv]
# 設定預設的 Python 直譯器
python = "3.11"

# 設定 dev extras
dev-dependencies = [
    "pytest",
    "ruff",
]
```
**注意**: `[tool.uv.dev-dependencies]` 是一個方便的簡寫，但標準化的方式是使用 `[project.optional-dependencies]`。

## 常用工作流程

### 1. 建立可編輯安裝

在開發過程中，你通常會希望以 "可編輯模式" (editable mode) 安裝你的專案。這意味著你對原始碼的修改會立即反映在執行的版本中，無需重新安裝。

```bash
# 安裝主要相依性和專案本身 (可編輯模式)
uv pip install -e .

# 同時安裝 dev 相依性
uv pip install -e ".[dev]"
```

### 2. 從 `pyproject.toml` 鎖定相依性

如 `Lesson_07` 所述，你可以直接從 `pyproject.toml` 產生鎖定檔案。

```bash
# 只鎖定主要相依性
uv pip compile pyproject.toml -o requirements.txt

# 鎖定主要和 dev 相依性
uv pip compile pyproject.toml --extra dev -o requirements-dev.txt
```
`--extra dev` 會告訴 `uv` 包含 `[project.optional-dependencies.dev]` 中的套件。

### 3. 同步環境

有了從 `pyproject.toml` 產生的鎖定檔案後，你可以使用 `uv sync` 來設定環境。

```bash
uv sync --require-hashes requirements-dev.txt
```

## 練習

1.  建立一個新的專案資料夾，並在其中建立 `pyproject.toml` 和 `src/my_project/__init__.py`。
2.  在 `pyproject.toml` 中定義 `name`, `version` 和一個相依套件 (例如 `cowsay`)。
3.  建立一個虛擬環境 `uv venv`。
4.  執行 `uv pip install -e .`。
5.  寫一個簡單的 Python 腳本，匯入並使用 `cowsay`，並用 `uv run` 執行它，確認相依性已安裝。
6.  在 `pyproject.toml` 中加入 `[project.optional-dependencies.dev]` 並列出 `pytest`。
7.  執行 `uv pip install -e ".[dev]"`，並確認 `pytest` 已被安裝 (`uv pip list`)。
