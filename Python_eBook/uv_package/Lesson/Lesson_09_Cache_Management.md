# Lesson 9: 快取管理

`uv` 的速度優勢之一來自其智慧的全域快取機制。當你下載一個套件時，`uv` 會將其儲存在一個共用的快取目錄中。下次當另一個專案也需要同一個版本的套件時，`uv` 可以直接從快取中複製，而無需重新下載。

## `uv` 的快取在哪裡？

`uv` 的快取位置取決於你的作業系統。你可以使用以下指令來找到它：

```bash
uv cache dir
```

- **macOS**: `~/Library/Caches/uv`
- **Linux**: `~/.cache/uv`
- **Windows**: `%LOCALAPPDATA%\uv\Cache` (例如 `C:\Users\YourUser\AppData\Local\uv\Cache`)

## 查看快取內容

你可以列出快取中的內容，但通常更有用的是查看快取佔用了多少空間。

```bash
uv cache clean --stats
```

這個指令會顯示快取中不同類型檔案的統計資訊，例如已解壓縮的套件、wheel 檔案等，以及總大小。

## 清理快取

雖然 `uv` 的快取通常不需要手動管理，但在某些情況下你可能想要清理它：
- 釋放磁碟空間。
- 懷疑快取已損壞 (極少發生)。
- 確保你正在從遠端來源重新下載套件。

### 清理整個快取

要完全刪除所有快取的內容，請執行：

```bash
uv cache clean
```
或者
```bash
uv cache purge
```

這會移除所有已下載的套件、建置的 wheel 和其他暫存檔案。下次你安裝套件時，`uv` 會重新從網際網路下載它們。

### 清理特定套件

如果你只想清理特定套件的快取 (例如 `requests`)，你可以指定套件名稱：

```bash
uv cache clean requests
```

這會從快取中移除所有版本的 `requests` 套件。

## 快取與離線工作

`uv` 的快取也使得在沒有網路連線的情況下工作成為可能。如果你要安裝的套件版本已經存在於快取中，`uv` 就不會嘗試連線到網路。

你可以使用 `--cache-dir` 旗標來指定一個不同的快取目錄，這在 CI/CD 環境中或當你想在不同位置之間共用快取時很有用。

## 練習

1.  執行 `uv cache dir` 來找出你的快取目錄在哪裡。
2.  執行 `uv cache clean --stats` 查看目前快取的大小。
3.  安裝一個你之前沒有安裝過的套件，例如 `uv pip install rich`。
4.  再次執行 `uv cache clean --stats`，觀察快取大小的變化。
5.  執行 `uv cache clean rich` 來只移除 `rich` 套件。
6.  最後，執行 `uv cache clean` 來清空整個快取，並再次檢查大小以確認。
