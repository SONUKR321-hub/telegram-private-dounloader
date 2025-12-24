# 🎯 TDL Usage Guide

Quick reference for common download scenarios.

---

## 🚀 Getting Started

### First Time Setup

```bash
# Login to Telegram
tdl login
```

Enter your:
1. API ID (from https://my.telegram.org)
2. API Hash
3. Phone number
4. OTP code

**You only need to do this once!**

---

## 📥 Download Examples

### Example 1: Download from Public Channel

```bash
tdl dl -u https://t.me/telegram --threads 16
```

### Example 2: Download Specific Message

```bash
tdl dl -u https://t.me/c/1234567890/100 --threads 16
```

### Example 3: Download Message Range

```bash
tdl dl -u https://t.me/c/1234567890/100-200 --threads 16
```

### Example 4: Download Videos Only

```bash
tdl dl -u https://t.me/my_channel --threads 16 --include "*.mp4,*.mkv,*.avi"
```

### Example 5: Download Large Files (>50MB)

```bash
tdl dl -u https://t.me/my_channel --threads 16 --min-size 52428800
```

### Example 6: Download to Custom Folder

```bash
tdl dl -u https://t.me/c/1234567890/100 --threads 16 -d "E:\TELE\downloads\my_folder"
```

---

## 🔍 Finding Content

### List Your Chats

```bash
tdl chat ls
```

This shows all your chats with their IDs.

### Get Telegram URL

1. Open Telegram app
2. Go to the message with the file
3. Right-click → "Copy Message Link"
4. Paste the URL in the command

**URL formats:**
- Public: `https://t.me/channelname/123`
- Private: `https://t.me/c/1234567890/123`

---

## ⚙️ Common Options

| Option | Description | Example |
|--------|-------------|---------|
| `--threads 16` | Use 16 parallel connections (MAX SPEED) | Required for fast downloads |
| `--include "*.mp4"` | Download only matching files | Videos only |
| `--exclude "*.jpg"` | Skip matching files | No images |
| `--min-size 10485760` | Minimum file size (bytes) | Files >= 10MB |
| `--max-size 104857600` | Maximum file size (bytes) | Files <= 100MB |
| `-d "path"` | Custom download directory | Organize downloads |
| `--continue` | Resume interrupted download | Continue from where it stopped |

---

## 📊 File Size Reference

| Size | Bytes |
|------|-------|
| 1 MB | 1048576 |
| 10 MB | 10485760 |
| 50 MB | 52428800 |
| 100 MB | 104857600 |
| 1 GB | 1073741824 |

---

## 🎯 Real-World Scenarios

### Scenario 1: Download All Videos from a Course Channel

```bash
# First, find the channel
tdl chat ls | grep "Course"

# Then download videos only
tdl dl -u https://t.me/course_channel --threads 16 --include "*.mp4,*.mkv"
```

### Scenario 2: Download Specific Lecture Range

```bash
# Download lectures 10-20
tdl dl -u https://t.me/c/1234567890/10-20 --threads 16
```

### Scenario 3: Download Large Files Only

```bash
# Download files larger than 100MB
tdl dl -u https://t.me/my_channel --threads 16 --min-size 104857600
```

### Scenario 4: Resume Failed Download

```bash
# If download was interrupted, resume it
tdl dl -u https://t.me/c/1234567890/100 --threads 16 --continue
```

---

## 💡 Tips & Tricks

1. **Maximum Speed:** Always use `--threads 16`
2. **Filter First:** Use `--include` or `--min-size` to avoid downloading unwanted files
3. **Organize:** Use `-d` to create separate folders for different channels
4. **Resume:** Use `--continue` if your download gets interrupted
5. **Check First:** Run `tdl chat ls` to find channel IDs

---

## 🆘 Troubleshooting

### "Not logged in"
```bash
tdl login
```

### "Database is locked"
Close any other TDL processes and try again.

### Slow downloads?
Make sure you're using `--threads 16`

### Download failed?
Use `--continue` to resume

---

## 📚 More Help

- **Quick reference:** [TDL_QUICKREF.md](TDL_QUICKREF.md)
- **Full guide:** [TDL_GUIDE.md](TDL_GUIDE.md)
- **TDL help:** `tdl --help`
- **Download help:** `tdl dl --help`

---

**Made with ❤️ by Sonu Kumar**  
**MMIT Muzaffarpur**

*Happy downloading! 🚀*
