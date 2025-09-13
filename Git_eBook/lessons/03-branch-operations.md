# Git 分支操作 - 平行世界的圖書館管理 🌳

## 學習目標
完成本課程後，你將能夠：
- 理解分支（Branch）的概念和重要性
- 熟練使用分支相關指令
- 掌握分支合併的基本技巧
- 應用分支進行功能開發

## 分支是什麼？神奇的平行圖書館！ 🏢

還記得我們的圖書館比喻嗎？現在想像你有一個神奇的能力：

### 🌟 一個圖書館，無數個平行版本
```
📚 主圖書館 (main)
├── 🆕 新書專區分館 (feature/new-books)
├── 🔧 裝修分館 (fix/renovation) 
├── 📖 兒童專區分館 (feature/kids-section)
└── 🎨 藝術展覽分館 (feature/art-exhibition)
```

每個分館（分支）都是：
- ✅ 完全獨立的工作空間
- 🔄 基於某個時間點的主圖書館建立
- 🛡️ 不會影響其他分館的工作
- 🔗 最後可以合併回主圖書館

### 🤔 為什麼需要分支？

**沒有分支的痛苦：** 🚫
```
所有人都在同一個圖書館工作
張三在整理科學區 → 弄亂了歷史區
李四在新增童書 → 影響了小說區
王五在重新裝修 → 整個圖書館都不能用
```

**有了分支的美好：** ✨
```
張三在「科學區分館」安心工作
李四在「童書分館」專心整理
王五在「裝修分館」大膽改造
主圖書館依然正常營運！
```

## 基本分支操作 🎯

### 1. 查看現有分支 (git branch)

```bash
# 查看所有分支
git branch

# 查看所有分支（包含遠端分支）
git branch -a

# 查看分支詳細資訊
git branch -v
```

**預期輸出：**
```bash
# git branch
* main

# 解讀：
# * 表示目前所在的分支
# main 是預設的主分支名稱
```

### 2. 建立新分支 (git branch <分支名>)

```bash
# 建立新分支（但不切換過去）
git branch feature/user-login

# 查看分支列表
git branch
```

**預期輸出：**
```
  feature/user-login
* main
```

**發生了什麼？**
- 🏗️ Git 建立了一個新的「分館」
- 📋 這個分館完全複製了目前 main 分支的狀態
- 📍 但你目前還在 main 分支工作

### 3. 切換分支 (git checkout / git switch)

```bash
# 切換到指定分支（舊語法）
git checkout feature/user-login

# 切換到指定分支（新語法，推薦）
git switch feature/user-login

# 查看目前分支
git branch
```

**預期輸出：**
```bash
# git switch feature/user-login
Switched to branch 'feature/user-login'

# git branch
* feature/user-login
  main
```

### 4. 建立並立即切換 (一步到位)

```bash
# 建立新分支並立即切換（舊語法）
git checkout -b feature/shopping-cart

# 建立新分支並立即切換（新語法，推薦）
git switch -c feature/shopping-cart
```

**預期輸出：**
```
Switched to a new branch 'feature/shopping-cart'
```

## 實際演示：開發新功能 💡

讓我們透過一個完整的範例，體驗分支的威力！

### 📋 情境：為網站新增用戶登入功能

```bash
# 1. 確認目前在主分支
git branch
# * main

# 2. 建立功能分支
git switch -c feature/user-login

# 3. 建立登入相關檔案
echo "function login() { console.log('用戶登入'); }" > login.js
echo "<form>用戶登入表單</form>" > login.html

# 4. 查看狀態
git status
```

**輸出：**
```
On branch feature/user-login
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        login.html
        login.js

nothing added to commit but untracked files present
```

```bash
# 5. 提交新功能
git add .
git commit -m "新增用戶登入功能"

# 6. 檢查歷史
git log --oneline
```

**輸出：**
```
b2c3d4e 新增用戶登入功能
a1b2c3d (main) 初始版本：建立基本網頁結構
```

### 🔄 在分支間切換

```bash
# 切換回主分支
git switch main

# 檢查檔案
dir
```

**神奇的事情發生了！** ✨
- 📂 `login.js` 和 `login.html` 消失了！
- 🏛️ 你回到了原本的主圖書館
- 🔒 分支的變更被安全地保存著

```bash
# 切換回功能分支
git switch feature/user-login

# 檢查檔案
dir
```

**檔案又回來了！** 🎉
- 📄 `login.js` 和 `login.html` 重新出現
- 🌿 你在功能分支的所有工作都被保存

## 分支合併 🤝

功能開發完成後，我們要把分館的改變合併回主圖書館！

### 🔀 Fast-forward 合併（快轉合併）

這是最簡單的合併情況：

```bash
# 1. 切換到主分支
git switch main

# 2. 合併功能分支
git merge feature/user-login
```

**預期輸出：**
```
Updating a1b2c3d..b2c3d4e
Fast-forward
 login.html | 1 +
 login.js   | 1 +
 2 files changed, 2 insertions(+)
 create mode 100644 login.html
 create mode 100644 login.js
```

**發生了什麼？**
- ⚡ `Fast-forward`：主分支直接「快轉」到功能分支的位置
- ✅ 功能分支的所有變更都被合併到主分支
- 📄 `login.html` 和 `login.js` 現在出現在主分支

### 📊 檢查合併結果

```bash
# 查看檔案
dir

# 查看歷史
git log --oneline

# 查看圖形化歷史
git log --oneline --graph
```

**輸出：**
```bash
# dir
login.html  login.js  index.html  README.md

# git log --oneline
b2c3d4e (HEAD -> main, feature/user-login) 新增用戶登入功能
a1b2c3d 初始版本：建立基本網頁結構

# git log --oneline --graph
* b2c3d4e (HEAD -> main, feature/user-login) 新增用戶登入功能
* a1b2c3d 初始版本：建立基本網頁結構
```

### 🗑️ 刪除已完成的分支

```bash
# 刪除功能分支（因為已經合併完成）
git branch -d feature/user-login

# 查看分支列表
git branch
```

**輸出：**
```bash
# git branch -d feature/user-login
Deleted branch feature/user-login (was b2c3d4e).

# git branch
* main
```

## 複雜的合併情況 🧩

### 🌿 三方合併（Three-way Merge）

當主分支和功能分支都有新的提交時：

```bash
# 模擬複雜情況
# 1. 建立新功能分支
git switch -c feature/shopping-cart
echo "購物車功能" > cart.js
git add .
git commit -m "新增購物車功能"

# 2. 切換到主分支，模擬其他人的變更
git switch main
echo "<footer>版權所有</footer>" >> index.html
git add .
git commit -m "新增網頁版權資訊"

# 3. 查看分支狀況
git log --oneline --graph --all
```

**輸出：**
```
* c3d4e5f (HEAD -> main) 新增網頁版權資訊
| * d4e5f6g (feature/shopping-cart) 新增購物車功能
|/  
* b2c3d4e 新增用戶登入功能
* a1b2c3d 初始版本：建立基本網頁結構
```

**圖解：**
```
main 分支:    a1b2c3d → b2c3d4e → c3d4e5f
                         ↘
shopping-cart:                    d4e5f6g
```

### 🤝 執行三方合併

```bash
# 在主分支合併功能分支
git merge feature/shopping-cart
```

**預期輸出：**
```
Merge made by the 'ort' strategy.
 cart.js | 1 +
 1 file changed, 1 insertion(+)
```

**如果出現編輯器：**
```
Merge branch 'feature/shopping-cart'

# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.
```

只需要保存並關閉編輯器即可（在 nano 中按 `Ctrl+X`，vim 中輸入 `:wq`）

### 📊 檢查合併結果

```bash
git log --oneline --graph
```

**輸出：**
```
*   e5f6g7h (HEAD -> main) Merge branch 'feature/shopping-cart'
|\  
| * d4e5f6g (feature/shopping-cart) 新增購物車功能
* | c3d4e5f 新增網頁版權資訊
|/  
* b2c3d4e 新增用戶登入功能
* a1b2c3d 初始版本：建立基本網頁結構
```

## 分支命名規範 📝

### 🏷️ 常見的分支命名模式

```bash
# 功能開發
feature/user-authentication
feature/shopping-cart
feature/payment-system

# 錯誤修復
fix/login-bug
fix/memory-leak
hotfix/security-vulnerability

# 文件更新
docs/api-documentation
docs/user-guide

# 實驗性功能
experiment/new-ui-design
experiment/performance-optimization
```

### 📋 命名最佳實務

**好的命名：** ✅
- `feature/user-login`：清楚描述功能
- `fix/password-validation`：說明修復內容
- `docs/installation-guide`：明確文件類型

**不好的命名：** ❌
- `branch1`：沒有意義
- `fix`：太籠統
- `新功能`：使用中文可能造成編碼問題

## 常用分支操作速查 🔧

### 📋 分支管理指令表

| 指令 | 圖書館比喻 | 實際功能 |
|------|-----------|----------|
| `git branch` | 查看所有分館 | 列出所有分支 |
| `git branch 名稱` | 建立新分館 | 建立新分支 |
| `git switch 名稱` | 移動到指定分館 | 切換分支 |
| `git switch -c 名稱` | 建立並移動到新分館 | 建立並切換分支 |
| `git merge 名稱` | 合併分館到主館 | 合併分支 |
| `git branch -d 名稱` | 拆除已完成的分館 | 刪除分支 |

### 🚨 緊急狀況處理

```bash
# 如果有未提交的變更要切換分支
git stash                    # 暫存變更
git switch other-branch      # 切換分支
git stash pop               # 恢復變更

# 強制刪除未合併的分支
git branch -D branch-name

# 重新命名分支
git branch -m old-name new-name
```

## 實戰練習 🏋️‍♀️

### 🎯 練習任務：開發個人部落格

完成以下步驟來鞏固分支操作：

1. **建立主專案**
```bash
mkdir my-blog
cd my-blog
git init
echo "# 我的個人部落格" > README.md
git add .
git commit -m "初始專案設置"
```

2. **開發文章功能**
```bash
git switch -c feature/article-system
echo "function createArticle() {}" > article.js
echo "<div>文章模板</div>" > article-template.html
git add .
git commit -m "新增文章系統基本功能"
```

3. **開發評論功能**
```bash
git switch -c feature/comment-system
echo "function addComment() {}" > comment.js
echo "<div>評論區</div>" > comment-section.html
git add .
git commit -m "新增評論系統"
```

4. **合併功能到主分支**
```bash
git switch main
git merge feature/article-system
git merge feature/comment-system
```

5. **清理完成的分支**
```bash
git branch -d feature/article-system
git branch -d feature/comment-system
```

6. **檢查最終結果**
```bash
git log --oneline --graph
dir
```

**期望的最終輸出：**
```bash
# git log --oneline --graph
*   f6g7h8i Merge branch 'feature/comment-system'
|\  
| * e5f6g7h 新增評論系統
* |   d4e5f6g Merge branch 'feature/article-system'
|\ \  
| * | c3d4e5f 新增文章系統基本功能
| |/  
|/|   
* | b2c3d4e 初始專案設置

# dir 應該包含：
README.md
article.js
article-template.html
comment.js
comment-section.html
```

## 重點整理 🎯

### 🌟 分支的核心價值
1. **隔離開發**：每個功能獨立開發，互不干擾
2. **並行工作**：多人可以同時開發不同功能
3. **實驗安全**：可以在分支上嘗試新想法
4. **版本管理**：清楚追蹤每個功能的開發歷程

### 🔄 標準分支工作流程
```
1. 從主分支建立功能分支
   git switch -c feature/new-feature

2. 在功能分支開發
   # 修改檔案
   git add .
   git commit -m "功能描述"

3. 合併回主分支
   git switch main
   git merge feature/new-feature

4. 刪除功能分支
   git branch -d feature/new-feature
```

## 下一步 🚀

在下一課「遠端倉庫協作」中，我們將學習：
- 🌐 如何連接 GitHub 等遠端服務
- ⬆️⬇️ push 和 pull 的操作
- 👥 多人協作的工作流程
- 🔗 本地分支與遠端分支的關係

準備好將你的圖書館連接到雲端了嗎？ ☁️✨