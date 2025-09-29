# Lesson 3: 虛擬環境管理

## 學習目標
- 理解虛擬環境的概念
- 學習創建和激活虛擬環境
- 練習包安裝

## 內容
想像你的家裡有好幾個房間，每個房間都裝飾不同，存放不同的物品。這就是虛擬環境的概念！

### 為什麼需要虛擬環境？
- 避免不同項目的包版本衝突
- 保持系統 Python 乾淨
- 輕鬆管理項目依賴

### 創建虛擬環境
1. 打開終端機，進入你的項目資料夾。
2. 運行以下指令，這會建立一個名為 `.venv` 的虛擬環境資料夾，這是 Python 社群的通用慣例。
   ```bash
   uv venv
   ```
   你也可以指定 Python 版本來建立環境，例如 `uv venv --python 3.11`。

### 在 VS Code 中使用 uv 創建虛擬環境
VS Code 提供了內建終端機，讓你輕鬆管理虛擬環境。以下是步驟：

1. 在 VS Code 中打開你的項目資料夾。
2. 按 `Ctrl + Shift + P`（或 `Cmd + Shift + P` 在 Mac 上）打開命令面板，輸入 "Terminal: Create New Terminal" 並選擇它來打開終端機。
3. 在終端機中，確保你在項目根目錄，然後運行：
   ```bash
   uv venv
   ```
   這會在項目資料夾中創建一個名為 `.venv` 的虛擬環境。
4. 激活虛擬環境：
   ```powershell
   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   ```
   ```bash
   # Windows (Command Prompt)
   .venv\Scripts\activate.bat
   ```
   ```bash
   # macOS/Linux
   source .venv/bin/activate
   ```
   激活後，命令提示符會顯示 `(.venv)`。
5. 安裝包（例如）：
   ```bash
   uv pip install requests
   ```
6. 設置 VS Code 的 Python 解釋器：
   - 當你建立 `.venv` 並安裝套件後，VS Code 通常會自動偵測到並提示你是否要使用這個環境。
   - 如果沒有，按 `Ctrl + Shift + P` 打開命令面板。
   - 輸入 "Python: Select Interpreter" 並選擇它。
   - 從列表中選擇虛擬環境的 Python 解釋器（通常會標示為 `.venv`）。

### 激活虛擬環境
在 Windows (PowerShell) 上：
```powershell
.venv\Scripts\Activate.ps1
```

在 macOS/Linux 上：
```bash
source .venv/bin/activate
```

激活後，你會看到命令提示符前面有 `(.venv)`。

### 在虛擬環境中安裝包
```bash
uv pip install requests
```

### 檢查安裝的包
```bash
uv pip list
```

### 退出虛擬環境
```bash
deactivate
```

## 互動練習
1. 創建一個名為 `.venv` 的虛擬環境。
2. 激活它。
3. 安裝 `requests` 包。
4. 檢查安裝的包列表。
5. 退出虛擬環境。

## 生活比喻
就像你不會把臥室的衣服和廚房的食材混在一起一樣，每個 Python 項目都應該有自己的「房間」。

## 下一步
現在你知道如何管理「房間」了！下一堂課學習如何在房間裡管理「家具」（包）。