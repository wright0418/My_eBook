# Git 基礎概念 - 歡迎來到程式碼圖書館！📚

## 學習目標
完成本課程後，你將能夠：
- 理解 Git 是什麼以及為什麼需要它
- 掌握 Git 的基本術語和概念
- 了解版本控制的重要性

## Git 是什麼？用圖書館來理解！

想像一下，你是一位圖書館的館長，需要管理一個巨大的圖書館。在這個圖書館裡：

### 🏛️ Git = 圖書館管理系統
Git 就像是一個非常智慧的圖書館管理系統，它幫你：
- 📖 記錄每本書（檔案）的所有版本
- 📋 追蹤誰改了什麼內容
- 🔄 讓多個館員（開發者）同時工作
- ⏰ 隨時回到過去的任何時間點

### 📚 Repository（倉庫）= 整個圖書館
**Repository**（常簡稱為 repo）就是你的整個圖書館建築。裡面包含：
```
我的圖書館/
├── 小說區/
├── 歷史區/
├── 科學區/
└── 管理紀錄/ (這就是 .git 資料夾)
```

### 📝 Working Directory（工作目錄）= 圖書館大廳
這是你目前正在整理書籍的地方。你可以：
- 新增新書
- 修改書的內容
- 刪除舊書
- 重新排列書籍

## Git 的三個重要區域

### 1. 🏢 Working Directory（工作目錄）
```
現在你正在圖書館大廳工作
你可以自由地移動、修改書籍
但這些改變還沒有被「正式記錄」
```

### 2. 📦 Staging Area（暫存區）
```
這像是一個「準備上架」的區域
你把要正式登記的書籍先放在這裡
確認沒問題後，再一次性登記到系統中
```

### 3. 📋 Repository（倉庫）
```
這是正式的圖書館管理系統
所有的變更都被永久記錄在這裡
就像是官方的藏書目錄
```

## 重要術語解釋

### 🏷️ Commit（提交）= 建立圖書館快照
每次 commit 就像是為整個圖書館拍一張快照，記錄：
```
📅 時間：2025年9月12日 下午3點
👨‍💼 館員：張三
📝 做了什麼：新增了10本程式設計書籍
🆔 快照編號：a1b2c3d4（Git 會自動產生）
```

### 🌿 Branch（分支）= 平行的圖書館版本
想像你有一個神奇的能力，可以創造平行的圖書館：
```
📚 主圖書館 (main/master)
├── 🏗️ 新書區分館 (feature/new-books)
├── 🔧 整修分館 (fix/renovation)
└── 📖 特別展覽分館 (docs/exhibition)
```
每個分支都是獨立的，互不干擾！

### 🔄 Merge（合併）= 合併分館的改變
當分館的工作完成後，你可以把改變合併回主圖書館：
```
新書區分館的書 → 合併到 → 主圖書館
```

## 為什麼需要 Git？

### ❌ 沒有 Git 的痛苦
```
檔案名稱混亂：
my_project.txt
my_project_v2.txt
my_project_v2_final.txt
my_project_v2_final_REAL.txt
my_project_v2_final_REAL_THIS_TIME.txt
```

### ✅ 有了 Git 的美好
```bash
# 檢視所有版本
git log --oneline
a1b2c3d 新增用戶登入功能
b2c3d4e 修正密碼驗證錯誤
c3d4e5f 初始版本

# 隨時回到任何版本
git checkout c3d4e5f  # 回到初始版本
git checkout a1b2c3d  # 回到最新版本
```

## 實際範例：第一次使用 Git

假設你要開始管理一個名為「我的日記」的專案：

### 1. 初始化圖書館（Repository）
```bash
# 建立資料夾並進入
mkdir 我的日記
cd 我的日記

# 初始化 Git（建立圖書館管理系統）
git init
```

**預期輸出：**
```
Initialized empty Git repository in C:/Users/你的用戶名/我的日記/.git/
```

### 2. 建立第一本書（檔案）
```bash
# 建立一個日記檔案
echo "今天是我使用 Git 的第一天！" > 日記.txt
```

### 3. 檢查圖書館狀態
```bash
git status
```

**預期輸出：**
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        日記.txt

nothing added to commit but untracked files present (use "git add" to track them)
```

**解讀輸出：**
- 📍 目前在 main 分支（主圖書館）
- 🚫 還沒有任何快照記錄
- 📄 發現了一個未追蹤的檔案：日記.txt

## 小結

恭喜！你現在已經了解了 Git 的基本概念：

| Git 術語 | 圖書館比喻 | 實際意義 |
|---------|-----------|----------|
| Repository | 整個圖書館 | 專案資料夾 |
| Working Directory | 圖書館大廳 | 你正在編輯的檔案 |
| Staging Area | 準備上架區 | 準備提交的變更 |
| Commit | 圖書館快照 | 保存的版本記錄 |
| Branch | 平行分館 | 獨立的開發線 |

## 下一步

在下一課「基本指令操作」中，我們將學習如何：
- 📦 把書放到準備區（git add）
- 📋 正式登記到系統（git commit）
- 👀 檢查圖書館狀態（git status）
- 📖 查看歷史記錄（git log）

準備好繼續你的 Git 學習之旅了嗎？ 🚀