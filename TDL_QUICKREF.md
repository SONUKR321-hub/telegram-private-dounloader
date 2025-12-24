# 🚀 TDL Quick Reference Card

## ⚡ FASTEST DOWNLOAD COMMANDS

### Login (First Time Only)
```bash
tdl login
```

### Download Single Message (MAX SPEED)
```bash
tdl dl -u https://t.me/c/CHAT_ID/MSG_ID --threads 16 --size 524288
```

### Download Message Range (MAX SPEED)
```bash
tdl dl -u https://t.me/c/CHAT_ID/100-200 --threads 16 --size 524288
```

### Download Entire Chat/Channel (MAX SPEED)
```bash
tdl dl -u https://t.me/CHANNEL_USERNAME --threads 16 --size 524288
```

---

## 🎯 COMMON USE CASES

### 1. Download Videos Only
```bash
tdl dl -u https://t.me/CHANNEL --threads 16 --include "*.mp4,*.mkv,*.avi"
```

### 2. Download Large Files (>50MB)
```bash
tdl dl -u https://t.me/CHANNEL --threads 16 --min-size 52428800
```

### 3. Download to Custom Folder
```bash
tdl dl -u https://t.me/c/CHAT_ID/MSG_ID --threads 16 -d "E:\TELE\downloads\my_folder"
```

### 4. Resume Interrupted Download
```bash
tdl dl -u https://t.me/c/CHAT_ID/MSG_ID --threads 16 --continue
```

---

## 🐍 PYTHON USAGE

### Quick Download (Easiest)
```python
from telegram_manager.tdl_wrapper import quick_download

# Download with max speed (16 threads)
quick_download("https://t.me/c/1234567890/100")
```

### Advanced Download
```python
from telegram_manager.tdl_wrapper import TDLDownloader

tdl = TDLDownloader("downloads")

# Download with custom settings
success, msg = tdl.download_url(
    url="https://t.me/c/1234567890/100",
    threads=16,              # Max speed
    chunk_size=524288,       # 512KB chunks
    output_dir="downloads",
    resume=True
)
print(msg)
```

### Download Videos Only
```python
from telegram_manager.tdl_wrapper import download_videos_only

download_videos_only("https://t.me/my_channel", threads=16)
```

### Download Large Files Only
```python
from telegram_manager.tdl_wrapper import download_large_files_only

download_large_files_only("https://t.me/my_channel", min_size_mb=50, threads=16)
```

### Download Message Range
```python
from telegram_manager.tdl_wrapper import TDLDownloader

tdl = TDLDownloader("downloads")
success, msg = tdl.download_range(
    chat_id="1234567890",
    start_msg=100,
    end_msg=200,
    threads=16
)
```

---

## 🎮 INTERACTIVE CLI

Run the interactive CLI:
```bash
python tdl_cli.py
```

Features:
- ✅ Login to Telegram
- ✅ Download from URL (16 threads)
- ✅ Download message ranges
- ✅ Download videos only
- ✅ Download large files only

---

## ⚙️ PERFORMANCE SETTINGS

### Maximum Speed (Fast Connection >100Mbps)
```bash
--threads 16 --size 1048576
```

### Balanced (Medium Connection 10-100Mbps)
```bash
--threads 16 --size 524288
```

### Conservative (Slow Connection <10Mbps)
```bash
--threads 8 --size 131072
```

---

## 📊 SPEED COMPARISON

| Method | Typical Speed | Threads |
|--------|--------------|---------|
| Telegram Desktop | 5-10 MB/s | 1 |
| Python Telethon | 8-15 MB/s | 1-4 |
| **TDL (16 threads)** | **30-100+ MB/s** | **16** |

---

## 🔧 FILE FILTERS

### Include Patterns
```bash
--include "*.mp4,*.mkv"           # Videos only
--include "*.pdf,*.docx"          # Documents only
--include "*.zip,*.rar,*.7z"      # Archives only
```

### Exclude Patterns
```bash
--exclude "*.jpg,*.png"           # No images
--exclude "*.txt"                 # No text files
```

### Size Filters
```bash
--min-size 10485760               # Files >= 10MB
--max-size 104857600              # Files <= 100MB
```

---

## 💡 PRO TIPS

1. **Always use `--threads 16`** for maximum speed
2. **Use `--continue`** to resume interrupted downloads
3. **Filter by file type** to avoid downloading unwanted files
4. **Download during off-peak hours** for best speeds
5. **Use custom folders** to organize downloads

---

## 🆘 TROUBLESHOOTING

### Not logged in?
```bash
tdl login
```

### Slow downloads?
- Increase threads: `--threads 16`
- Increase chunk size: `--size 1048576`

### Download failed?
- Resume with: `--continue`
- Reduce threads: `--threads 8`

---

## 📚 MORE INFO

- Full guide: `TDL_GUIDE.md`
- TDL help: `tdl --help`
- Download help: `tdl dl --help`

---

**Remember:** For maximum speed, always use `--threads 16`! 🚀
