# Lesson 10: 遷移現有專案至 `uv`

將使用傳統 `pip` 和 `requirements.txt` 的專案遷移到 `uv` 是一個相對簡單的過程，可以立即為你的專案帶來速度和效率的提升。

本章節將引導你完成遷移步驟。

## 遷移情境

假設你有一個現有的專案，其結構如下：

```
legacy_project/
├── venv/              # 由 virtualenv 或 venv 建立的環境
├── requirements.txt   # 使用 pip freeze > requirements.txt 產生
└── src/
    └── main.py
```

`requirements.txt` 內容可能非常冗長，包含了所有直接和間接的相依性：
```
anyio==4.4.0
certifi==2024.7.4
fastapi==0.111.0
h11==0.14.0
httpcore==1.0.5
...
```

## 遷移步驟

### 步驟 1: 建立 `requirements.in` (或更新 `pyproject.toml`)

遷移的核心是將**高階相依性**與**鎖定的版本**分開。

你需要建立一個 `requirements.in` 檔案，只列出你的專案**直接**依賴的套件。你可能需要查看你的原始碼 (`import` 語句) 或舊的 `requirements.txt` 中的註解來找出這些套件。

`requirements.in`:
```
fastapi
uvicorn
```

如果你想使用 `pyproject.toml`，則將這些相依性加入 `[project.dependencies]`。

### 步驟 2: 使用 `uv` 建立新的虛擬環境

你可以保留舊的 `venv` 資料夾作為參考，但建議使用 `uv` 建立一個全新的、乾淨的環境。

```bash
# 在專案根目錄執行
uv venv
```

這會建立一個 `.venv` 資料夾。

### 步驟 3: 鎖定相依性

現在，使用 `uv pip compile` 從你的 `requirements.in` 產生一個新的、乾淨的 `requirements.txt` 鎖定檔案。

```bash
uv pip compile requirements.in -o requirements.txt
```

這個新的 `requirements.txt` 將會結構清晰，並包含雜湊值以增加安全性。

### 步驟 4: 同步環境

使用 `uv sync` 來安裝所有在新的 `requirements.txt` 中定義的套件。

```bash
uv sync --require-hashes requirements.txt
```

`uv` 會快速地在你的 `.venv` 中設定好所有東西。

### 步驟 5: 更新 `.gitignore` 並清理

1.  將新的虛擬環境資料夾 `.venv/` 加入你的 `.gitignore` 檔案。
2.  一旦你確認新環境運作正常，就可以安全地刪除舊的 `venv/` 資料夾。
3.  將新的 `requirements.in` 和更新後的 `requirements.txt` 提交到版本控制。

## 遷移完成

恭喜！你的專案現在已經完全由 `uv` 管理。你和你的團隊現在可以享受更快的相依性安裝和一致的開發環境。

之後的開發流程就如 `Lesson_07` 所述：
- **修改** `requirements.in`。
- **執行** `uv pip compile` 來更新 `requirements.txt`。
- **執行** `uv sync` 來更新你的環境。

## 練習

1.  找到一個你過去使用 `pip` 和 `requirements.txt` 的舊專案。
2.  按照本章節的步驟，將其遷移到 `uv`。
3.  建立 `requirements.in`，重新產生 `requirements.txt`。
4.  使用 `uv venv` 和 `uv sync` 設定新環境。
5.  執行專案的測試或主要功能，確保一切運作正常。
