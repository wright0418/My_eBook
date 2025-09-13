# Git 基本指令操作 - 圖書館管理實務 📋

## 學習目標
完成本課程後，你將能夠：
- 熟練使用 git init, add, commit, status, log 等基本指令
- 理解 Git 的三階段工作流程
- 建立你的第一個完整的 Git 專案

## 圖書館管理的一天 🏛️

讓我們透過一個完整的工作日，學習 Git 的基本操作！

## 第一步：建立新的圖書館 (git init)

### 🏗️ 初始化專案
```bash
# 建立專案資料夾
mkdir my-first-git-project
cd my-first-git-project

# 初始化 Git 倉庫（建立圖書館管理系統）
git init
```

**預期輸出：**
```
Initialized empty Git repository in C:/Users/你的用戶名/my-first-git-project/.git/
```

**發生了什麼？**
- 🏛️ Git 在你的資料夾建立了一個隱藏的 `.git` 資料夹
- 📋 這就是圖書館的「管理系統」，記錄所有歷史
- ✅ 你的資料夾現在正式成為一個 Git 倉庫！

### 🔍 驗證初始化成功
```bash
# 檢查隱藏檔案（Windows PowerShell）
dir -Force

# 或使用 Git 指令確認
git status
```

**預期輸出：**
```powershell
# dir -Force 的輸出
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--h--       2025/9/12    下午 03:45                .git

# git status 的輸出
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track them)
```

## 第二步：檢查圖書館狀態 (git status)

### 📊 隨時了解圖書館狀況
`git status` 是你最好的朋友，它告訴你：
- 📍 目前在哪個分支（分館）
- 📚 有哪些書籍（檔案）發生變化
- 🚀 接下來可以做什麼

### 💡 實際演示
```bash
# 建立一個新檔案
echo "這是我的第一個 Git 專案！" > README.txt

# 檢查狀態
git status
```

**預期輸出：**
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.txt

nothing added to commit but untracked files present (use "git add" to track them)
```

**狀態解讀：**
- 🌿 `On branch main`：在主分館工作
- 🚫 `No commits yet`：還沒有任何快照記錄
- 📄 `Untracked files`：發現新書籍，但還沒登記到系統

## 第三步：準備登記書籍 (git add)

### 📦 把書籍放到「準備上架」區域

```bash
# 將單一檔案加入暫存區
git add README.txt

# 檢查狀態變化
git status
```

**預期輸出：**
```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.txt
```

**發生了什麼？**
- ✅ README.txt 現在在「準備上架」區域
- 📋 `Changes to be committed`：準備要登記的變更
- 🟢 檔案狀態從「未追蹤」變成「已暫存」

### 🎯 其他常用的 add 指令

```bash
# 加入所有檔案
git add .

# 加入特定類型的檔案
git add *.txt

# 加入特定資料夾的所有檔案
git add docs/

# 互動式選擇要加入的內容
git add -i
```

## 第四步：正式登記到系統 (git commit)

### 📸 建立圖書館快照

```bash
# 提交變更（建立快照）
git commit -m "第一次提交：新增 README 文件"
```

**預期輸出：**
```
[main (root-commit) a1b2c3d] 第一次提交：新增 README 文件
 1 file changed, 1 insertion(+)
 create mode 100644 README.txt
```

**輸出解釋：**
- 🆔 `a1b2c3d`：這個快照的唯一編號（前7位）
- 📊 `1 file changed, 1 insertion(+)`：變更統計
- ✨ `create mode 100644 README.txt`：建立新檔案

### ✍️ 撰寫好的提交訊息

**好的提交訊息：**
```bash
git commit -m "新增用戶登入功能"
git commit -m "修正密碼驗證的安全性漏洞"
git commit -m "更新 README 文件的安裝說明"
```

**不好的提交訊息：**
```bash
git commit -m "修改"
git commit -m "更新"
git commit -m "asdf"
```

### 📝 多行提交訊息
```bash
# 不加 -m 參數會打開編輯器
git commit

# 或是使用多個 -m 參數
git commit -m "新增用戶登入功能" -m "包含表單驗證和錯誤處理"
```

## 第五步：查看圖書館歷史 (git log)

### 📖 瀏覽過去的記錄

```bash
# 基本的歷史記錄
git log
```

**預期輸出：**
```
commit a1b2c3d4e5f6g7h8i9j0 (HEAD -> main)
Author: 你的名字 <你的email@example.com>
Date:   Thu Sep 12 15:30:00 2025 +0800

    第一次提交：新增 README 文件
```

### 🎨 更美觀的歷史顯示

```bash
# 一行顯示模式
git log --oneline

# 圖形化顯示分支
git log --oneline --graph

# 顯示檔案變更統計
git log --stat

# 顯示最近 3 次提交
git log -3
```

**各種輸出範例：**

```bash
# git log --oneline
a1b2c3d 第一次提交：新增 README 文件

# git log --oneline --graph
* a1b2c3d 第一次提交：新增 README 文件

# git log --stat
commit a1b2c3d4e5f6g7h8i9j0
Author: 你的名字 <你的email@example.com>
Date:   Thu Sep 12 15:30:00 2025 +0800

    第一次提交：新增 README 文件

 README.txt | 1 +
 1 file changed, 1 insertion(+)
```

## 完整的工作流程範例 🔄

讓我們透過一個實際範例，練習完整的工作流程：

### 🎯 情境：建立一個簡單的個人網頁

```bash
# 1. 建立並初始化專案
mkdir my-website
cd my-website
git init

# 2. 建立基本檔案
echo "<h1>歡迎來到我的網站</h1>" > index.html
echo "這是我的個人網站專案" > README.md

# 3. 檢查狀態
git status
```

**輸出：**
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
        index.html

nothing added to commit but untracked files present (use "git add" to track them)
```

```bash
# 4. 加入所有檔案到暫存區
git add .

# 5. 檢查暫存狀態
git status
```

**輸出：**
```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
        new file:   index.html
```

```bash
# 6. 提交第一個版本
git commit -m "初始版本：建立基本網頁結構"

# 7. 修改網頁內容
echo "<h1>歡迎來到我的網站</h1><p>這裡有我的作品集</p>" > index.html

# 8. 檢查變更
git status
```

**輸出：**
```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")
```

```bash
# 9. 加入並提交修改
git add index.html
git commit -m "新增網頁內容：加入作品集說明"

# 10. 查看完整歷史
git log --oneline
```

**輸出：**
```
b2c3d4e 新增網頁內容：加入作品集說明
a1b2c3d 初始版本：建立基本網頁結構
```

## 常見狀況處理 🛠️

### ❌ 忘記加入檔案到暫存區
```bash
# 錯誤：直接提交會沒有任何變更
git commit -m "更新檔案"
# 輸出：nothing to commit, working tree clean

# 正確：先加入再提交
git add 檔案名稱
git commit -m "更新檔案"
```

### 📝 修改最後一次提交訊息
```bash
# 修改最近一次的提交訊息
git commit --amend -m "正確的提交訊息"
```

### 🔄 撤銷暫存區的檔案
```bash
# 將檔案從暫存區移除（但保留工作目錄的變更）
git restore --staged 檔案名稱

# 或使用舊的語法
git reset HEAD 檔案名稱
```

## 圖解 Git 工作流程 📊

```
工作目錄          暫存區           倉庫
(Working Dir)    (Staging)       (Repository)
                                 
📄 檔案修改  -->  📦 準備提交  -->  📋 永久記錄
              git add          git commit
              
         <--  git restore  <--  git checkout
           撤銷暫存           取出歷史版本
```

## 小測驗 📝

在進入下一課之前，請試著完成這個小練習：

1. 建立一個名為 `git-practice` 的新專案
2. 初始化 Git 倉庫
3. 建立 `app.py` 檔案，內容：`print("Hello, Git!")`
4. 建立 `.gitignore` 檔案，內容：`*.tmp`
5. 將兩個檔案都提交到倉庫
6. 修改 `app.py`，新增一行：`print("學習 Git 真有趣！")`
7. 提交這個修改
8. 使用 `git log --oneline` 查看歷史

**期望的最終輸出：**
```bash
git log --oneline
# b2c3d4e 更新程式：新增學習心得
# a1b2c3d 初始版本：建立 Python 程式和 gitignore
```

## 重點整理 🎯

| 指令 | 圖書館比喻 | 實際功能 |
|------|-----------|----------|
| `git init` | 建立圖書館管理系統 | 初始化 Git 倉庫 |
| `git status` | 檢查圖書館狀況 | 查看檔案狀態 |
| `git add` | 把書放到準備區 | 將變更加入暫存區 |
| `git commit` | 建立圖書館快照 | 提交變更到倉庫 |
| `git log` | 查看歷史記錄 | 顯示提交歷史 |

## 下一步 🚀

在下一課「分支操作 - 平行世界的管理」中，我們將學習：
- 🌿 如何建立和切換分支
- 🔀 分支合併的概念
- 🏗️ 功能開發的最佳實務
- 🛡️ 如何避免破壞主要程式碼

準備好探索 Git 的平行世界功能了嗎？ ✨