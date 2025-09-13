# Copilot Instructions for My_eBook

## 專案架構總覽
- 本倉庫為個人學習電子書，分為多主題資料夾：
  - `Git_eBook/`：Git 學習中心，包含基礎、進階、協作等課程，所有章節在 `lessons/` 目錄下以 Markdown 編寫。
  - `Python_Book/`：Python 學習中心，分為 `PythonBasic/`（RPG 專案式教學，章節與範例程式分離）與 `Python_進階/`（進階語法與裝飾器範例）。
- 每個主題資料夾均有獨立 `README.md`，說明學習目標、章節結構與特色。

## 關鍵開發模式與慣例
- **章節內容**：
  - Markdown (`.md`) 用於理論、說明、章節目錄。
  - Python (`.py`) 用於程式範例、練習、挑戰題與解答。
  - 範例程式與練習題通常以 `chX.py`、`chX_practice.py` 命名，便於對應章節。
- **RPG 專案教學**：
  - `game_character.py`、`game_combat.py`、`game_items.py` 等檔案分別對應角色、戰鬥、物品等系統模組。
  - 系統主控程式如 `game_character_system.py`、`game_combat_system.py`、`game_item_system.py` 負責整合各模組。
  - 建議 AI agent 依章節目錄與檔案命名推斷內容關聯。
- **Git 教學**：
  - 章節以 `01-git-basics.md`、`02-basic-commands.md` 等命名，內容循序漸進。
  - 章節間以「圖書館管理」比喻貫穿，便於理解 Git 概念。

## 重要工作流程
- 本倉庫無自動化 build/test 流程，重點在內容撰寫與教學結構。
- 若需新增章節，請依現有命名規則與目錄結構放置。
- 若需擴充 RPG 專案，請遵循現有模組分工（角色、戰鬥、物品、紀錄等）。

## 風格與撰寫建議
- 內容以教學、說明為主，程式碼需具備註解與易懂結構。
- 範例程式鼓勵分段設計，便於逐步學習與測試。
- 若有跨檔案互動，請明確標註依賴關係。

## 參考檔案
- 主倉庫 `README.md`：總覽與主題索引
- `Git_eBook/README.md`、`Python_Book/README.md`、`Python_Book/PythonBasic/README.md`：各主題教學說明
- RPG 專案核心檔案：`game_character.py`、`game_combat.py`、`game_items.py`、`game_character_system.py` 等

---
如有不明確或未涵蓋的部分，請主動詢問使用者以補充規則或慣例。
