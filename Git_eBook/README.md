# Try_Git - Git 學習中心 📚

歡迎來到 Git 學習中心！這是一個專為初學者設計的 Git 版本控制系統學習專案。我們使用「圖書館管理」這個統一的比喻，讓你輕鬆理解 Git 的核心概念。

## 🎯 學習目標

完成本課程後，你將能夠：
- ✅ 掌握 Git 的基本概念和術語
- ✅ 熟練使用 Git 的核心指令
- ✅ 管理分支並處理合併
- ✅ 與 GitHub 協作開發專案
- ✅ 解決常見問題和緊急狀況
- ✅ 建立標準的 Git 工作流程

## 📖 課程大綱

### 🏗️ 基礎篇

#### [第1課：Git 基礎概念](lessons/01-git-basics.md)
- Git 是什麼？為什麼需要版本控制？
- Repository、Working Directory、Staging Area 概念
- 用圖書館比喻理解 Git 的工作原理
- 安裝和初始設定

**學習時間：** 30分鐘  
**難度：** ⭐

#### [第2課：基本指令操作](lessons/02-basic-commands.md)
- `git init` - 初始化倉庫
- `git add` - 暫存變更
- `git commit` - 提交變更
- `git status` - 檢查狀態
- `git log` - 查看歷史
- 完整的工作流程演示

**學習時間：** 45分鐘  
**難度：** ⭐⭐

### 🌿 中級篇

#### [第3課：分支操作](lessons/03-branch-operations.md)
- Branch 概念：平行世界的圖書館管理
- 建立、切換、合併分支
- Fast-forward vs 三方合併
- 分支命名規範和最佳實務
- 實戰練習：開發個人部落格

**學習時間：** 60分鐘  
**難度：** ⭐⭐⭐

#### [第4課：遠端倉庫協作](lessons/04-remote-collaboration.md)
- GitHub 入門和基本設置
- `git clone`, `git push`, `git pull` 操作
- 本地與遠端分支的關係
- Pull Request 工作流程
- 團隊協作最佳實務

**學習時間：** 75分鐘  
**難度：** ⭐⭐⭐

### 🚀 進階篇

#### [第5課：進階操作與問題解決](lessons/05-advanced-operations.md)
- 合併衝突的處理
- Interactive Rebase 重整歷史
- Reset vs Revert 的使用時機
- Cherry-pick 精選提交
- Git Stash 臨時保存
- 緊急狀況處理技巧

**學習時間：** 90分鐘  
**難度：** ⭐⭐⭐⭐

## 🎓 學習路徑

### 🐣 初學者路徑（推薦）
```
第1課 → 第2課 → 實作練習 → 第3課 → 更多練習 → 第4課 → 第5課
```

### ⚡ 快速上手路徑
```
第1課（快速瀏覽）→ 第2課 → 第4課 → 依需求學習第3課和第5課
```

### 🎯 問題解決路徑
有特定問題？直接跳到相關章節：
- **合併衝突**：第5課 - 合併衝突處理
- **分支管理**：第3課 - 分支操作
- **GitHub 協作**：第4課 - 遠端倉庫協作
- **歷史修改**：第5課 - Reset vs Revert

## 🛠️ 開發環境設定

### 系統需求
- **作業系統**：Windows 10/11
- **終端機**：PowerShell 5.1+
- **編輯器**：VS Code（推薦）或任何文字編輯器

### Git 安裝
1. 下載 Git：https://git-scm.com/download/windows
2. 安裝時選擇預設選項
3. 驗證安裝：`git --version`

### 初始設定
```powershell
# 設定用戶資訊
git config --global user.name "你的名字"
git config --global user.email "your.email@example.com"

# 設定預設編輯器（可選）
git config --global core.editor "code --wait"

# 檢查設定
git config --list
```

## 🏋️‍♀️ 實作練習

每一課都包含實作練習，建議在 `exercises/` 資料夾中練習：

```powershell
# 建立練習環境
mkdir exercises
cd exercises

# 第1課練習
mkdir lesson1-basics
cd lesson1-basics
git init
# ... 跟著課程內容練習

# 第2課練習
cd ..
mkdir lesson2-commands
cd lesson2-commands
# ... 繼續練習
```

## 🆘 常見問題與解答

### Q: Git 和 GitHub 有什麼不同？
A: Git 是版本控制工具，GitHub 是雲端平台。就像 Word 是編輯軟體，而 Google Drive 是雲端儲存服務。

### Q: 我可以跳過某些課程嗎？
A: 可以，但建議按順序學習。第1-2課是基礎，第3-4課是實用技能，第5課是進階應用。

### Q: 練習時出錯怎麼辦？
A: 別擔心！出錯是學習的一部分。查看第5課的問題解決章節，或者刪除練習資料夾重新開始。

### Q: 如何知道我學會了？
A: 如果你能獨立完成以下任務，就算學會了：
- 建立新專案並推送到 GitHub
- 建立功能分支並合併
- 解決簡單的合併衝突
- 與他人協作開發

## 📚 延伸學習資源

### 📖 推薦閱讀
- [Pro Git Book](https://git-scm.com/book/zh-tw/v2) - 官方文檔（繁體中文）
- [GitHub 官方指南](https://guides.github.com/)
- [Atlassian Git 教程](https://www.atlassian.com/git/tutorials)

### 🎮 互動學習
- [Learn Git Branching](https://learngitbranching.js.org/?locale=zh_CN) - 視覺化 Git 學習
- [GitHub Skills](https://skills.github.com/) - GitHub 官方互動課程

### 🛠️ 實用工具
- [GitKraken](https://www.gitkraken.com/) - 圖形化 Git 工具
- [GitHub Desktop](https://desktop.github.com/) - GitHub 官方桌面應用
- [VS Code Git 擴充](https://code.visualstudio.com/docs/editor/versioncontrol) - 編輯器整合

## 🤝 貢獻與回饋

這是一個學習專案，歡迎你的改進建議！

### 如何貢獻
1. Fork 這個專案
2. 建立功能分支：`git checkout -b feature/improvement`
3. 提交變更：`git commit -m "改進說明"`
4. 推送分支：`git push origin feature/improvement`
5. 建立 Pull Request

### 回饋方式
- 🐛 回報問題：建立 Issue
- 💡 改進建議：建立 Issue 或 Pull Request
- ⭐ 覺得有用：給個星星鼓勵
- 📢 分享專案：讓更多人受益

## 🎉 學習成就

完成課程後，給自己一些鼓勵：

- [ ] 🏗️ **Git 新手**：完成第1-2課，理解基本概念
- [ ] 🌿 **分支高手**：完成第3課，掌握分支操作
- [ ] 🌐 **協作達人**：完成第4課，會用 GitHub 協作
- [ ] 🚀 **Git 專家**：完成第5課，能解決複雜問題
- [ ] 🎖️ **實戰老兵**：完成所有練習，建立自己的專案

## 📞 聯絡資訊

如果你有任何問題或建議，歡迎透過以下方式聯絡：

- 📧 Email：[在這裡加上你的聯絡方式]
- 💬 GitHub Issues：[專案問題回報區]
- 🌟 GitHub Discussions：[專案討論區]

---


**記住：** 學習 Git 就像學習開車，理論很重要，但實際練習更關鍵。不要怕犯錯，每個錯誤都是學習的機會！

祝你學習愉快！ 🎉✨

---

*「版本控制不只是工具，更是一種思維方式。掌握了 Git，就掌握了軟體開發的基石。」*

**最後更新：** 2025年9月13日  
**版本：** v1.0.1