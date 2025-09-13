# Git 進階操作與問題解決 - 圖書館危機處理專家 🚨

## 學習目標
完成本課程後，你將能夠：
- 解決複雜的合併衝突
- 使用 rebase 重整提交歷史
- 掌握 reset 和 revert 的差異
- 運用 cherry-pick 精選提交
- 處理各種緊急狀況

## 合併衝突處理 - 當圖書館員意見不合 💥

### 🤯 什麼是合併衝突？

想像兩位圖書館員同時整理同一本書：
- 👨‍💼 張三說：「這本書應該放在科學區」
- 👩‍💼 李四說：「這本書應該放在歷史區」
- 🤖 Git 說：「我不知道該聽誰的，你們自己決定！」

### 📋 製造一個衝突情境

```bash
# 1. 建立測試專案
mkdir conflict-demo
cd conflict-demo
git init

# 2. 建立初始檔案
echo "歡迎來到我們的網站" > index.html
git add .
git commit -m "初始版本"

# 3. 建立功能分支A
git switch -c feature/header-update
echo "歡迎來到我們的現代化網站" > index.html
git add .
git commit -m "更新網站標題為現代化"

# 4. 切換到主分支，建立功能分支B
git switch main
git switch -c feature/header-design
echo "歡迎來到我們的美麗網站" > index.html
git add .
git commit -m "更新網站標題為美麗"

# 5. 合併分支A到主分支
git switch main
git merge feature/header-update  # 這會成功

# 6. 嘗試合併分支B（產生衝突！）
git merge feature/header-design
```

**預期輸出（衝突發生）：**
```bash
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

### 🔍 檢查衝突狀況

```bash
# 查看衝突狀態
git status
```

**輸出：**
```bash
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   index.html

no changes added to commit (use "git add" to track them)
```

### 📖 檢視衝突內容

```bash
# 查看衝突檔案內容
type index.html
```

**輸出：**
```html
<<<<<<< HEAD
歡迎來到我們的現代化網站
=======
歡迎來到我們的美麗網站
>>>>>>> feature/header-design
```

**衝突標記解釋：**
- `<<<<<<< HEAD`：目前分支（main）的內容
- `=======`：分隔線
- `>>>>>>> feature/header-design`：要合併的分支內容

### ✏️ 手動解決衝突

編輯 `index.html` 檔案，決定要保留什麼內容：

```html
歡迎來到我們的現代化美麗網站
```

或者你可以選擇保留其中一邊：
```html
歡迎來到我們的現代化網站
```

### ✅ 完成衝突解決

```bash
# 1. 標記衝突已解決
git add index.html

# 2. 完成合併提交
git commit -m "解決合併衝突：整合現代化和美麗的網站標題"

# 3. 檢查結果
git log --oneline --graph
```

**預期輸出：**
```bash
*   d4e5f6g (HEAD -> main) 解決合併衝突：整合現代化和美麗的網站標題
|\  
| * c3d4e5f (feature/header-design) 更新網站標題為美麗
* | b2c3d4e (feature/header-update) 更新網站標題為現代化
|/  
* a1b2c3d 初始版本
```

### 🛠️ 衝突解決工具

#### 使用 VS Code 解決衝突
1. VS Code 會自動偵測衝突
2. 提供「Accept Current Change」、「Accept Incoming Change」等選項
3. 可以手動編輯結合兩邊內容

#### 使用 Git 內建工具
```bash
# 啟動合併工具（如果有設定）
git mergetool

# 取消合併（回到合併前狀態）
git merge --abort
```

## 重寫歷史 - 圖書館時光機 ⏰

### 🚨 重要警告
重寫歷史會改變提交的 SHA 值，**絕對不要**在已推送的公開分支上進行！

### 📝 Interactive Rebase（互動式重定基底）

想像你要重新整理圖書館的歷史記錄：

```bash
# 查看最近5次提交
git log --oneline -5

# 進入互動式 rebase
git rebase -i HEAD~3
```

**會開啟編輯器：**
```
pick a1b2c3d 新增用戶登入功能
pick b2c3d4e 修正登入錯誤
pick c3d4e5f 新增登入樣式

# Rebase instructions:
# p, pick = use commit
# r, reword = use commit, but edit the commit message
# e, edit = use commit, but stop for amending
# s, squash = use commit, but meld into previous commit
# f, fixup = like "squash", but discard this commit's log message
# x, exec = run command (the rest of the line) using shell
# d, drop = remove commit
```

### 🎯 常用 Rebase 操作

#### 1. 修改提交訊息 (reword)
```
reword a1b2c3d 新增用戶登入功能
pick b2c3d4e 修正登入錯誤  
pick c3d4e5f 新增登入樣式
```

#### 2. 合併提交 (squash)
```
pick a1b2c3d 新增用戶登入功能
squash b2c3d4e 修正登入錯誤
squash c3d4e5f 新增登入樣式
```
結果：三個提交合併成一個

#### 3. 刪除提交 (drop)
```
pick a1b2c3d 新增用戶登入功能
drop b2c3d4e 修正登入錯誤
pick c3d4e5f 新增登入樣式
```

### 🔄 實際範例：整理提交歷史

```bash
# 建立一些雜亂的提交
echo "第1版" > feature.txt
git add .
git commit -m "新增功能"

echo "第2版" > feature.txt
git add .
git commit -m "修正拼字錯誤"

echo "第3版" > feature.txt
git add .
git commit -m "再次修正拼字"

echo "第4版" > feature.txt
git add .
git commit -m "完善功能說明"

# 查看歷史
git log --oneline -4

# 整理最近4次提交
git rebase -i HEAD~4
```

在編輯器中設定：
```
pick 第1次 新增功能
squash 第2次 修正拼字錯誤
squash 第3次 再次修正拼字
squash 第4次 完善功能說明
```

保存後會要求編輯合併後的提交訊息：
```
新增功能：包含完整的功能實作和說明文件
```

## Reset vs Revert - 時光倒流的兩種方式 ↩️

### 🔄 Git Reset（重設）
想像你要將圖書館「倒回」到某個時間點：

```bash
# 軟重設：保留工作目錄和暫存區的變更
git reset --soft HEAD~1

# 混合重設：保留工作目錄，清空暫存區（預設）
git reset --mixed HEAD~1
git reset HEAD~1  # 簡寫

# 硬重設：完全回到指定狀態，刪除所有變更
git reset --hard HEAD~1
```

#### 📊 Reset 模式比較

| 模式 | 工作目錄 | 暫存區 | 提交歷史 |
|------|---------|-------|----------|
| `--soft` | 保留 | 保留 | 重設 |
| `--mixed` | 保留 | 清空 | 重設 |
| `--hard` | 清空 | 清空 | 重設 |

### ↩️ Git Revert（撤銷）
想像你要「撤銷」某個圖書館員的操作，但保留歷史記錄：

```bash
# 撤銷最近一次提交（建立新的撤銷提交）
git revert HEAD

# 撤銷指定提交
git revert a1b2c3d

# 撤銷一系列提交
git revert HEAD~3..HEAD
```

### 🤔 什麼時候用 Reset vs Revert？

**使用 Reset：**
- ✅ 在本地分支，還沒推送
- ✅ 想要「重寫」歷史
- ❌ 絕不在公開分支使用

**使用 Revert：**
- ✅ 在已推送的公開分支
- ✅ 想要保留完整歷史記錄
- ✅ 安全的「撤銷」操作

## Cherry-pick - 精選書籍搬運術 🍒

想像你要從其他分館挑選特定的書籍：

### 🎯 基本 Cherry-pick

```bash
# 從其他分支挑選特定提交
git cherry-pick a1b2c3d

# 挑選多個提交
git cherry-pick a1b2c3d b2c3d4e

# 挑選一系列提交
git cherry-pick a1b2c3d..c3d4e5f
```

### 📋 實際範例

```bash
# 1. 建立功能分支
git switch -c feature/user-profile
echo "用戶資料頁面" > profile.html
git add .
git commit -m "新增用戶資料頁面"

echo "用戶設定頁面" > settings.html
git add .
git commit -m "新增用戶設定頁面"

echo "修正安全性問題" >> profile.html
git add .
git commit -m "修正用戶資料的安全性漏洞"

# 2. 回到主分支，只挑選安全性修正
git switch main
git log --oneline feature/user-profile

# 假設安全性修正的 SHA 是 c3d4e5f
git cherry-pick c3d4e5f
```

**預期輸出：**
```bash
[main d4e5f6g] 修正用戶資料的安全性漏洞
 Date: Thu Sep 12 16:00:00 2025 +0800
 1 file changed, 1 insertion(+)
```

### 🛠️ Cherry-pick 選項

```bash
# 只套用變更，不自動提交
git cherry-pick --no-commit a1b2c3d

# 編輯提交訊息
git cherry-pick --edit a1b2c3d

# 記錄原始提交資訊
git cherry-pick -x a1b2c3d
```

## 緊急狀況處理 🚨

### 💾 Git Stash - 臨時保存工作

想像你正在整理書籍，突然有緊急任務：

```bash
# 保存目前的工作狀態
git stash

# 保存並加上說明
git stash push -m "正在開發用戶登入功能"

# 查看 stash 清單
git stash list

# 恢復最近的 stash
git stash pop

# 恢復指定的 stash
git stash apply stash@{1}

# 刪除 stash
git stash drop stash@{0}

# 清空所有 stash
git stash clear
```

### 🔍 找回遺失的提交

```bash
# 查看所有操作歷史（包含已刪除的提交）
git reflog

# 恢復特定提交
git reset --hard a1b2c3d
```

**Reflog 輸出範例：**
```bash
a1b2c3d (HEAD -> main) HEAD@{0}: reset: moving to a1b2c3d
b2c3d4e HEAD@{1}: commit: 新增功能
c3d4e5f HEAD@{2}: commit: 修正錯誤
```

### 🧹 清理和維護

```bash
# 查看倉庫狀況
git status
git log --oneline --graph

# 清理未追蹤的檔案（小心使用！）
git clean -f        # 刪除檔案
git clean -fd       # 刪除檔案和目錄
git clean -n        # 預覽要刪除的內容

# 垃圾回收和壓縮
git gc

# 檢查倉庫完整性
git fsck
```

## 實戰演練：完整的危機處理 🏋️‍♀️

### 📋 情境：專案出現重大問題

```bash
# 1. 建立問題情境
mkdir crisis-demo
cd crisis-demo
git init

# 建立一些提交
echo "版本1" > app.js
git add .
git commit -m "初始版本"

echo "版本2 - 新增功能" > app.js
git add .
git commit -m "新增重要功能"

echo "版本3 - 有bug" > app.js
git add .
git commit -m "更新功能（引入bug）"

echo "版本4 - 更多bug" > app.js
git add .
git commit -m "嘗試修復但引入更多問題"

# 2. 發現問題，需要回到版本2
git log --oneline

# 3. 使用 reset 回到版本2（假設在本地分支）
git reset --hard HEAD~2

# 4. 檢查狀態
git log --oneline
cat app.js
```

### 🔄 如果是公開分支的處理

```bash
# 如果已推送，使用 revert 撤銷問題提交
git revert HEAD~1    # 撤銷最近一次
git revert HEAD~2    # 撤銷倒數第二次

# 或批量撤銷
git revert --no-commit HEAD~2..HEAD
git commit -m "撤銷有問題的提交"
```

## 最佳實務和建議 💡

### ✅ 安全操作原則

1. **在重要操作前備份**
```bash
git tag backup-before-rebase
```

2. **使用分支進行實驗**
```bash
git switch -c experiment-branch
# 進行危險操作
# 如果成功，合併回主分支
# 如果失敗，直接刪除分支
```

3. **小步前進**
- 經常提交
- 提交訊息要清楚
- 一次只做一件事

### 🚨 危險操作警告

**絕對不要在公開分支上做：**
- `git reset --hard`（已推送的提交）
- `git rebase`（重寫已推送的歷史）
- `git push --force`（除非你確定知道後果）

**安全替代方案：**
- 使用 `git revert` 替代 `git reset`
- 使用 `git push --force-with-lease` 替代 `git push --force`

## 重點整理 🎯

### 🛠️ 問題解決工具箱

| 問題 | 解決工具 | 使用時機 |
|------|---------|----------|
| 合併衝突 | 手動編輯 | 自動合併失敗時 |
| 錯誤的提交 | `git revert` | 已推送的分支 |
| 想重寫歷史 | `git rebase -i` | 本地分支 |
| 回到過去 | `git reset` | 本地未推送 |
| 挑選提交 | `git cherry-pick` | 跨分支套用 |
| 臨時保存 | `git stash` | 切換分支時 |
| 找回提交 | `git reflog` | 提交遺失時 |

### 🎖️ 進階操作決策樹

```
有問題的提交？
├── 還沒推送？
│   ├── 是 → 使用 git reset 或 rebase
│   └── 否 → 使用 git revert
└── 要挑選特定提交？
    └── 使用 git cherry-pick
```

## 恭喜！你已經是 Git 高手了！ 🎉

通過這一系列的課程，你已經掌握了：
- 📚 Git 的基本概念和術語
- ⚙️ 基本和進階的 Git 指令
- 🌿 分支管理和合併技巧
- 🌐 遠端協作和 GitHub 使用
- 🚨 問題解決和危機處理

你現在具備了：
- ✅ 獨立使用 Git 管理專案的能力
- ✅ 與團隊協作開發的技能
- ✅ 處理複雜狀況的信心
- ✅ 持續學習更多進階技巧的基礎

### 🚀 繼續學習的方向

1. **Git Hooks**：自動化工作流程
2. **Git Submodules**：管理子專案
3. **Git LFS**：大檔案版本控制
4. **GitHub Actions**：持續整合/部署
5. **Git Flow**：標準化分支策略

**記住：** Git 是一個強大的工具，持續練習和實驗是精通的關鍵！

---

*「程式碼的版本控制就像時間管理一樣，看似複雜，但掌握了基本原則，就能讓一切井然有序。」*

祝你在 Git 的世界中探索愉快！ 🌟