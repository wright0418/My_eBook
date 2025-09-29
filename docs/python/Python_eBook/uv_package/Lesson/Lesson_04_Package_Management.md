# Lesson 4: 包安裝和管理

## 學習目標
- 學習安裝、更新和移除包
- 了解如何使用需求檔案 (`requirements.in`) 管理依賴
- 查看已安裝的包及其依賴關係

## 內容
包就像你房間裡的家具。`uv` 讓管理這些「家具」變得簡單又快速。

### 安裝、更新和移除包

- **安裝一個或多個包**：
  ```bash
  uv pip install requests "flask>=2.0"
  ```

- **更新一個包**：
  ```bash
  uv pip install --upgrade requests
  ```

- **移除一個包**：
  ```bash
  uv pip uninstall requests
  ```

### 使用需求檔案管理依賴

在專業的 Python 開發中，我們不推薦使用 `pip freeze` 來記錄依賴，因為它會混合直接依賴（你需要的）和間接依賴（你的依賴所需要的），導致檔案混亂。

更好的做法是使用一個 `requirements.in` 檔案來只記錄你的**直接依賴**。

1.  **建立 `requirements.in` 檔案**：
    ```
    # requirements.in
    flask
    requests
    ```

2.  **從 `requirements.in` 安裝所有包**：
    ```bash
    uv pip install -r requirements.in
    ```
    `uv` 會讀取這個檔案，並安裝 `flask` 和 `requests` 以及它們需要的所有子依賴。這個方法確保了你的環境是根據你的高階需求建立的。在後面的章節中，我們將學習如何將這些依賴「鎖定」到一個 `requirements.txt` 檔案中，以確保團隊中的每個人都使用完全相同的版本。

### 查看包信息

- **列出所有已安裝的包**：
  ```bash
  uv pip list
  ```

- **查看特定包的詳細資訊**：
  ```bash
  uv pip show requests
  ```
  這會顯示包的版本、作者、依賴等資訊。

- **以樹狀圖查看依賴關係**：
  ```bash
  uv pip tree
  ```
  這個指令非常有用，可以清晰地看到哪個包引入了哪個子依賴。

## 互動練習
1. 在你的虛擬環境中，建立一個 `requirements.in` 檔案，並寫入 `flask` 和 `cowsay`。
2. 從 `requirements.in` 安裝套件。
3. 執行 `uv pip tree` 查看 `flask` 帶來了哪些依賴。
4. 執行 `uv pip uninstall cowsay` 來移除 `cowsay`。
5. 再次從 `requirements.in` 安裝，確認 `cowsay` 被重新安裝回來。

## 生活比喻
`requirements.in` 就像你的購物清單，只寫下你最終想要的物品（例如「蛋糕」和「咖啡」）。`uv` 則像一個聰明的採購員，它會根據你的清單，自動買來所有製作這些物品所需的原料（麵粉、雞蛋、咖啡豆等）。

## 下一步
現在你知道如何管理專案的「家具」了！下一堂課我們將學習如何使用 `uv` 從頭開始建立一個結構化的專案。