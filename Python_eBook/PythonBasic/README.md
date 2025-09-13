# Python 基礎技術教學 - RPG風格學習

## 專案介紹
這是一個以角色扮演遊戲(RPG)為主題的 Python 教學專案。透過建立遊戲系統的過程，逐步學習 Python 的基礎概念和程式設計技巧。

## 教學特色

# PythonBasic 專案式學習說明

## 學習目標
- 以 RPG 專案為主軸，循序漸進學習 Python 基礎語法、物件導向、模組化設計。
- 每章節搭配範例程式與練習題，強化實作能力。

## 結構說明
- `Lession/`：章節理論與說明，皆以 Markdown 編寫。
	- 00-preface.md：前言與學習地圖
	- 01-basic-io.md ~ 10-random.md：基礎語法、資料結構、例外處理、隨機模組等
- `example/`：各章節對應範例程式與練習題
	- chX.py：章節範例程式
	- chX_practice.py：章節練習題
	- RPG 專案模組：
		- game_character.py / game_character_system.py：角色系統
		- game_combat.py / game_combat_system.py：戰鬥系統
		- game_items.py / game_item_system.py：物品系統
		- game_record_system.py：紀錄系統
		- map_example.py：地圖範例

## 特色與建議
- 章節內容理論與實作分離，便於逐步學習與測試。
- RPG 專案模組化設計，鼓勵跨檔案互動與系統整合。
- 範例程式皆具備註解，適合初學者閱讀。
- 建議依章節順序學習，並嘗試修改範例程式以加深理解。

## 參考
- 主倉庫 `README.md`：總覽與主題索引
- RPG 專案核心檔案：`game_character.py`、`game_combat.py`、`game_items.py`、`game_character_system.py` 等

---
如有疑問或建議，歡迎於 Issues 討論。

## 學習架構
每個章節都包含：
1. 概念說明 (.md)
2. 程式範例 (.py)
3. 實作練習
4. 課後挑戰
5. 參考解答 (_practice.py)

## 章節目錄

### [前言：RPG風格學習法](Lession/00-preface.md)
- 為什麼選擇RPG主題
- 學習方法說明
- 課程規劃概述

### [第一章：基礎輸入輸出](Lession/01-basic-io.md)
- print() 函數
- input() 函數
- f-string 格式化

### [第二章：條件判斷與控制流程](Lession/02-conditions-loops.md)
- if-elif-else 結構
- while 迴圈
- for 迴圈

### [第三章：函數的定義與使用](Lession/03-functions.md)
- 函數基礎
- 參數傳遞
- 返回值

### [第四章：List(列表)概念](Lession/04-lists.md)
- List 基本操作
- 遍歷列表
- 列表應用

### [第五章：字典(Dictionary)概念](Lession/05-dictionaries.md)
- 字典基礎
- 鍵值對操作
- 字典應用

### [第六章：類別(Class)概念](Lession/06-classes.md)
- 類別定義
- 物件建立
- 繼承概念

### [第七章：檔案處理技巧](Lession/07-files.md)
- 檔案讀寫
- 檔案操作
- 遊戲存檔實作

### [第八章：模組系統與import用法](Lession/08-modules.md)
- 模組基礎
- import 語法
- 模組化設計

### [第九章：例外處理](Lession/09-exceptions.md)
- try-except 結構
- 錯誤處理
- 安全性設計

### [第十章：隨機數的使用](Lession/10-random.md)
- random 模組
- 隨機遊戲系統
- 機率計算

## 使用方式
1. 依序閱讀各章節的說明文件 (.md)
2. 研讀並運行範例程式 (.py)
3. 完成章節練習
4. 挑戰進階任務
5. 參考解答檢視學習成果

## 建議學習方式
- 確實完成每章的實作練習
- 先自行嘗試課後挑戰
- 實在無法解決時再參考解答
- 根據自己的興趣擴充遊戲功能

## 專案結構
> 註：原始檔案 chNN.md 已備份於 `Lession/backup_original_chapters/`，主要檔案請參考 Lession 下的英文章節檔名。

```
PythonBaseicTech/
├── README.md                 # 本說明文件
├── Lession/00-preface.md     # 前言
├── Lession/01-basic-io.md    # 第一章說明
├── Lession/01-basic-io.py    # 第一章範例
├── Lession/01-basic-io_practice.py # 第一章解答
└── ...                       # 其他章節檔案
```

## 開發環境
- Python 3.8+
- 任何文字編輯器或IDE
- 建議使用 Visual Studio Code

讓我們開始這趟充滿冒險的 Python 學習之旅吧！
