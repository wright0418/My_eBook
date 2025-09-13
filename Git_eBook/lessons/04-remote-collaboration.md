# Git 遠端倉庫協作 - 雲端圖書館網絡 🌐

## 學習目標
完成本課程後，你將能夠：
- 理解本地倉庫與遠端倉庫的關係
- 熟練使用 push, pull, fetch 等指令
- 掌握 GitHub 的基本使用
- 了解團隊協作的基本工作流程

## 什麼是遠端倉庫？圖書館總部！ 🏛️

想像一下，你管理的本地圖書館現在要連接到一個強大的「圖書館總部」：

### 🌟 圖書館網絡系統
```
☁️ GitHub 雲端總部
    ↕️ (同步)
💻 你的本地圖書館
    ↕️ (同步)  
💻 同事A的圖書館
    ↕️ (同步)
💻 同事B的圖書館
```

### 📚 遠端倉庫的優勢
- ☁️ **雲端備份**：永遠不怕電腦損壞
- 👥 **多人協作**：全球的圖書館員一起工作
- 🔄 **版本同步**：所有人都能取得最新版本
- 🌍 **開源分享**：讓全世界看到你的專案

## GitHub 快速入門 🚀

### 🎯 建立你的第一個 GitHub 倉庫

1. **註冊 GitHub 帳號**
   - 前往 https://github.com
   - 點擊「Sign up」註冊帳號

2. **建立新倉庫**
   - 點擊右上角的 "+" → "New repository"
   - 輸入倉庫名稱：`my-first-repo`
   - 選擇「Public」（公開）
   - ✅ 勾選「Add a README file」
   - 點擊「Create repository」

### 📋 GitHub 倉庫資訊解讀

建立完成後，你會看到類似這樣的頁面：
```
https://github.com/你的用戶名/my-first-repo.git
```

這就是你的「雲端圖書館總部」地址！

## 連接本地與遠端倉庫 🔗

### 方法一：從 GitHub 複製到本地 (git clone)

```bash
# 複製遠端倉庫到本地（建議方式）
git clone https://github.com/你的用戶名/my-first-repo.git

# 進入專案資料夾
cd my-first-repo

# 檢查遠端連接
git remote -v
```

**預期輸出：**
```bash
# git clone 的輸出
Cloning into 'my-first-repo'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

# git remote -v 的輸出
origin  https://github.com/你的用戶名/my-first-repo.git (fetch)
origin  https://github.com/你的用戶名/my-first-repo.git (push)
```

**發生了什麼？**
- 📦 Git 將整個雲端圖書館複製到你的電腦
- 🔗 自動建立了名為 `origin` 的遠端連接
- ✅ 本地與雲端已經完美連接！

### 方法二：將現有專案連接到 GitHub

如果你已經有本地專案：

```bash
# 在你的現有專案中
cd existing-project

# 添加遠端倉庫連接
git remote add origin https://github.com/你的用戶名/existing-project.git

# 檢查連接
git remote -v

# 將本地內容推送到雲端
git push -u origin main
```

**預期輸出：**
```bash
# git push -u origin main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 242 bytes | 242.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/你的用戶名/existing-project.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

## 核心遠端操作 📡

### 1. 推送變更到雲端 (git push)

想像你在本地圖書館整理了新書，現在要送到總部：

```bash
# 在本地進行一些變更
echo "今天學會了 Git 遠端操作！" >> README.md

# 查看狀態
git status

# 提交變更
git add .
git commit -m "更新學習筆記"

# 推送到雲端
git push origin main
```

**預期輸出：**
```bash
# git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
        modified:   README.md

# git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (3/3), 298 bytes | 298.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To https://github.com/你的用戶名/my-first-repo.git
   a1b2c3d..b2c3d4e  main -> main
```

🎉 **成功！** 你的變更已經上傳到 GitHub！

### 2. 從雲端獲取最新版本 (git pull)

想像總部有新的圖書目錄更新，你要同步到本地：

```bash
# 獲取並合併雲端的最新變更
git pull origin main
```

**預期輸出（如果有更新）：**
```bash
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 3 (delta 1), pack-reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/你的用戶名/my-first-repo
 * branch            main       -> FETCH_HEAD
   b2c3d4e..c3d4e5f  main       -> origin/main
Updating b2c3d4e..c3d4e5f
Fast-forward
 README.md | 1 +
 1 file changed, 1 insertion(+)
```

**預期輸出（如果沒有更新）：**
```bash
Already up to date.
```

### 3. 僅獲取資訊，不自動合併 (git fetch)

想像你只是想知道總部有什麼新消息，但還不想立即更新：

```bash
# 獲取遠端資訊（但不合併）
git fetch origin

# 查看遠端分支狀況
git branch -r

# 查看本地與遠端的差異
git log --oneline main..origin/main
```

## 實戰演練：完整的協作流程 🏋️‍♀️

### 📋 情境：你和朋友一起開發網站

1. **建立專案並推送到 GitHub**

```bash
# 建立本地專案
mkdir team-website
cd team-website
git init

# 建立基本檔案
echo "<h1>團隊網站</h1>" > index.html
echo "# 團隊網站專案" > README.md

# 初始提交
git add .
git commit -m "初始版本：建立基本網站結構"

# 連接到 GitHub（假設你已在 GitHub 建立 team-website 倉庫）
git remote add origin https://github.com/你的用戶名/team-website.git

# 推送到 GitHub
git push -u origin main
```

2. **模擬朋友的變更**

為了模擬協作，我們在 GitHub 網頁上直接編輯：
- 前往你的 GitHub 倉庫
- 點擊 `README.md` 檔案
- 點擊鉛筆圖示編輯
- 加入一行：`這是朋友在 GitHub 上的修改`
- 提交變更

3. **同步朋友的變更到本地**

```bash
# 檢查遠端狀態
git fetch origin

# 查看差異
git log --oneline HEAD..origin/main

# 同步變更
git pull origin main
```

**預期輸出：**
```bash
# git log --oneline HEAD..origin/main
c3d4e5f 朋友更新 README 檔案

# git pull origin main
Updating b2c3d4e..c3d4e5f
Fast-forward
 README.md | 1 +
 1 file changed, 1 insertion(+)
```

4. **你做的新變更**

```bash
# 新增樣式檔案
echo "body { font-family: Arial; }" > style.css

# 修改主頁面
echo "<link rel='stylesheet' href='style.css'>" >> index.html

# 提交變更
git add .
git commit -m "新增 CSS 樣式"

# 推送變更
git push origin main
```

### 🌊 完整的日常工作流程

```bash
# 每天開始工作前
git pull origin main          # 獲取最新版本

# 開發功能
git switch -c feature/new-page # 建立功能分支
# ... 進行開發 ...
git add .
git commit -m "新增關於我們頁面"

# 準備合併
git switch main               # 切換到主分支
git pull origin main         # 再次確認最新版本
git merge feature/new-page    # 合併功能分支

# 推送到雲端
git push origin main

# 清理分支
git branch -d feature/new-page
```

## 處理推送衝突 ⚠️

### 🚨 常見錯誤：推送被拒絕

```bash
git push origin main
```

**錯誤輸出：**
```bash
To https://github.com/你的用戶名/my-repo.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/你的用戶名/my-repo.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
```

**原因：** 雲端圖書館有其他人的新變更，你的本地版本已經過時。

### 🔧 解決方法

```bash
# 1. 先獲取最新版本
git pull origin main

# 2. 如果出現合併衝突，解決後提交
git add .
git commit -m "解決合併衝突"

# 3. 再次推送
git push origin main
```

## 分支的遠端操作 🌿

### 🔗 推送本地分支到雲端

```bash
# 建立功能分支
git switch -c feature/mobile-responsive

# 進行開發
echo "@media (max-width: 768px) { ... }" >> style.css
git add .
git commit -m "新增響應式設計"

# 推送分支到雲端
git push -u origin feature/mobile-responsive
```

**預期輸出：**
```bash
Total 3 (delta 1), reused 0 (delta 0)
remote: Create a pull request for 'feature/mobile-responsive' on GitHub by visiting:
remote:   https://github.com/你的用戶名/your-repo/pull/new/feature/mobile-responsive
To https://github.com/你的用戶名/your-repo.git
 * [new branch]      feature/mobile-responsive -> feature/mobile-responsive
Branch 'feature/mobile-responsive' set up to track remote branch 'feature/mobile-responsive' from 'origin'.
```

### 👥 GitHub Pull Request（合併請求）

GitHub 建議建立 Pull Request（PR），這是一個強大的協作功能：

1. **點擊 GitHub 提供的連結**
2. **填寫 PR 資訊**：
   - 標題：描述這個功能
   - 內容：詳細說明變更內容
3. **指定審查者**（如果是團隊專案）
4. **建立 Pull Request**

### 📋 查看和管理遠端分支

```bash
# 查看所有分支（本地+遠端）
git branch -a

# 查看遠端分支詳細資訊
git remote show origin

# 刪除遠端分支
git push origin --delete feature/mobile-responsive

# 清理本地的遠端分支參考
git fetch origin --prune
```

## 實用的遠端操作技巧 💡

### 🔧 常用指令組合

```bash
# 簡化的推送（當分支已設定追蹤時）
git push

# 簡化的拉取
git pull

# 檢查本地與遠端的差異
git diff main origin/main

# 查看遠端倉庫資訊
git remote -v
git remote show origin
```

### ⚡ 設定 Git 快捷指令

```bash
# 設定別名讓指令更簡短
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.pl pull
git config --global alias.ps push

# 現在可以使用簡短指令
git st    # 等同於 git status
git ci -m "message"  # 等同於 git commit -m "message"
```

## 安全和驗證 🔐

### 🔑 SSH 金鑰設定（推薦）

使用 SSH 金鑰可以避免每次輸入密碼：

```bash
# 1. 產生 SSH 金鑰（如果還沒有）
ssh-keygen -t ed25519 -C "your_email@example.com"

# 2. 複製公鑰內容
cat ~/.ssh/id_ed25519.pub

# 3. 到 GitHub Settings > SSH and GPG keys 新增金鑰

# 4. 測試連接
ssh -T git@github.com

# 5. 改用 SSH URL
git remote set-url origin git@github.com:你的用戶名/your-repo.git
```

### 🛡️ 個人存取權杖（Personal Access Token）

對於 HTTPS 連接，GitHub 需要使用存取權杖：

1. GitHub Settings > Developer settings > Personal access tokens
2. Generate new token
3. 選擇適當的權限範圍
4. 複製產生的權杖
5. 在命令列中使用權杖作為密碼

## 故障排除 🛠️

### ❌ 常見問題與解決方案

**問題 1: 推送被拒絕**
```bash
# 解決方案
git pull origin main
# 解決衝突後
git push origin main
```

**問題 2: 遠端分支不存在**
```bash
# 查看遠端分支
git branch -r

# 獲取最新遠端資訊
git fetch origin
```

**問題 3: 本地與遠端分支不同步**
```bash
# 重設本地分支與遠端同步
git reset --hard origin/main
```

**⚠️ 警告：** `git reset --hard` 會永久刪除本地未提交的變更！

## 重點整理 🎯

### 🌟 遠端協作核心概念

| 指令 | 圖書館比喻 | 實際功能 |
|------|-----------|----------|
| `git clone` | 複製總部圖書館 | 複製遠端倉庫 |
| `git push` | 送書到總部 | 推送變更到遠端 |
| `git pull` | 從總部取新書 | 獲取並合併遠端變更 |
| `git fetch` | 查看總部目錄 | 獲取遠端資訊 |
| `git remote` | 檢查總部連線 | 管理遠端連接 |

### 🔄 標準遠端工作流程

```
1. 開始工作前同步
   git pull origin main

2. 建立功能分支
   git switch -c feature/new-feature

3. 開發並提交
   git add .
   git commit -m "完成新功能"

4. 推送分支
   git push -u origin feature/new-feature

5. 在 GitHub 建立 Pull Request

6. 合併後清理
   git switch main
   git pull origin main
   git branch -d feature/new-feature
```

## 下一步 🚀

在下一課「進階操作與問題解決」中，我們將學習：
- 🔀 複雜的合併衝突解決
- ↩️ 重寫歷史（rebase, reset）
- 🍒 Cherry-pick 精選提交
- 🔧 Git hooks 和自動化
- 🚨 緊急狀況的處理技巧

準備好成為 Git 高手了嗎？ ⚡✨