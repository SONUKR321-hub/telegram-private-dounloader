# 🚀 TDL - Ultra-Fast Telegram Downloader Guide

## What is TDL?

`tdl` is a **blazing-fast** Telegram downloader written in Go that supports:
- ⚡ **Multi-threaded downloads** (up to 16 parallel connections)
- 📦 **Batch downloads** (download entire chats/channels)
- 🔄 **Resume support** (continue interrupted downloads)
- 🎯 **Selective downloads** (filter by file type, size, date)
- 📊 **Progress tracking** with real-time speed

## 🎯 Quick Start

### 1. Login to Telegram

First time setup - login with your credentials:

```bash
tdl login
```

You'll be prompted for:
- API ID (from https://my.telegram.org)
- API Hash
- Phone number
- OTP code
- 2FA password (if enabled)

### 2. Download from a Chat/Channel

#### Download specific message:
```bash
tdl dl -u https://t.me/c/CHAT_ID/MESSAGE_ID
```

#### Download message range:
```bash
tdl dl -u https://t.me/c/CHAT_ID/MESSAGE_ID-MESSAGE_ID2
```

#### Download entire chat (last 100 messages):
```bash
tdl dl -u https://t.me/CHAT_USERNAME
```

## 🔥 Advanced Usage

### Maximum Speed Downloads

Use **16 threads** for maximum speed:

```bash
tdl dl -u https://t.me/c/CHAT_ID/MESSAGE_ID --threads 16 --size 524288
```

Parameters:
- `--threads 16` - Use 16 parallel connections (max speed)
- `--size 524288` - Chunk size 512KB (optimal for large files)
- `--limit 0` - No download limit (download all)

### Download Specific File Types

#### Videos only:
```bash
tdl dl -u https://t.me/CHAT_USERNAME --include "*.mp4,*.mkv,*.avi"
```

#### Documents only:
```bash
tdl dl -u https://t.me/CHAT_USERNAME --include "*.pdf,*.docx,*.zip"
```

#### Exclude certain types:
```bash
tdl dl -u https://t.me/CHAT_USERNAME --exclude "*.jpg,*.png"
```

### Download by Size

#### Only files larger than 10MB:
```bash
tdl dl -u https://t.me/CHAT_USERNAME --min-size 10485760
```

#### Only files smaller than 100MB:
```bash
tdl dl -u https://t.me/CHAT_USERNAME --max-size 104857600
```

### Custom Download Directory

```bash
tdl dl -u https://t.me/CHAT_USERNAME -d "E:\TELE\downloads\my_folder"
```

## 📋 Common Commands

### List available chats:
```bash
tdl chat ls
```

### Export chat messages to JSON:
```bash
tdl chat export -c CHAT_ID
```

### Resume interrupted download:
```bash
tdl dl -u https://t.me/c/CHAT_ID/MESSAGE_ID --continue
```

### Download with custom naming:
```bash
tdl dl -u https://t.me/CHAT_USERNAME --template "{{.FileName}}"
```

## 🎯 Real-World Examples

### Example 1: Download all videos from a channel
```bash
tdl dl -u https://t.me/my_channel --include "*.mp4,*.mkv" --threads 16
```

### Example 2: Download specific message range
```bash
tdl dl -u https://t.me/c/1234567890/100-200 --threads 16
```

### Example 3: Download large files only (>50MB)
```bash
tdl dl -u https://t.me/my_channel --min-size 52428800 --threads 16
```

### Example 4: Download to specific folder
```bash
tdl dl -u https://t.me/c/1234567890/500 -d "E:\TELE\downloads\important" --threads 16
```

## ⚡ Performance Tips

1. **Use maximum threads for large files:**
   ```bash
   --threads 16
   ```

2. **Optimize chunk size for your connection:**
   - Fast connection (>100Mbps): `--size 1048576` (1MB)
   - Medium connection (10-100Mbps): `--size 524288` (512KB)
   - Slow connection (<10Mbps): `--size 131072` (128KB)

3. **Use filters to avoid downloading unwanted files:**
   ```bash
   --include "*.mp4" --min-size 10485760
   ```

4. **Download during off-peak hours** for maximum speed

## 🔧 Configuration

TDL stores configuration in: `%APPDATA%\tdl\`

Edit config for default settings:
```bash
tdl config
```

## 📊 Speed Comparison

| Method | Speed | Parallel Downloads |
|--------|-------|-------------------|
| Telegram Desktop | ~5-10 MB/s | No |
| Python Telethon | ~8-15 MB/s | Limited |
| **TDL (16 threads)** | **30-100+ MB/s** | ✅ Yes |

## 🎯 Integration with Python

You can call `tdl` from your Python scripts:

```python
import subprocess

def download_with_tdl(url, threads=16, output_dir="downloads"):
    cmd = [
        "tdl", "dl",
        "-u", url,
        "--threads", str(threads),
        "-d", output_dir,
        "--size", "524288"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0
```

## 🆘 Troubleshooting

### "No package found" error:
- TDL is already installed via Go

### "Not logged in" error:
```bash
tdl login
```

### Slow downloads:
- Increase threads: `--threads 16`
- Increase chunk size: `--size 1048576`
- Check your internet connection

### Download fails:
- Use `--continue` to resume
- Try reducing threads: `--threads 8`

## 📚 Full Command Reference

```bash
tdl --help                    # Show all commands
tdl dl --help                 # Download command help
tdl chat --help               # Chat commands help
tdl login --help              # Login help
```

## 🎉 Why TDL is Faster

1. **Written in Go** - Compiled language, much faster than Python
2. **True parallel downloads** - Multiple connections simultaneously
3. **Optimized chunk management** - Better memory usage
4. **Native Telegram protocol** - Direct MTProto implementation
5. **No overhead** - No web UI or unnecessary processing

---

**Pro Tip:** For maximum speed, always use `--threads 16` and adjust `--size` based on your connection speed!
