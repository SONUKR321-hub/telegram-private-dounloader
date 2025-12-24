# 📖 Quick Setup Guide

## For First-Time Users

### 1. Get Telegram API Credentials

1. Go to https://my.telegram.org
2. Log in with your phone number
3. Click "API development tools"
4. Create a new application:
   - App title: Any name (e.g., "My Downloader")
   - Short name: Any short name
   - Platform: Desktop
5. Copy your **API ID** and **API Hash**

### 2. Install Requirements

**Install Go** (if not installed):
- Windows: Download from https://go.dev/dl/
- Mac: `brew install go`
- Linux: `sudo apt install golang-go`

**Install TDL:**
```bash
go install github.com/iyear/tdl@latest
```

### 3. Login to Telegram

```bash
tdl login
```

Enter:
- Your API ID
- Your API Hash
- Your phone number (with country code, e.g., +1234567890)
- OTP code from Telegram
- 2FA password (if you have it)

**You only need to do this once!**

### 4. Run the Downloader

```bash
python download.py
```

## Menu Options Explained

### Option 1: Download from Channel/Group
- Use when you have a message link
- Right-click message in Telegram → Copy Message Link
- Paste the link

### Option 2: Search & Download by Filename
- **Best for bots!**
- Enter bot's chat ID (from Option 4)
- Search for files by name
- Download by message range

### Option 3: Download by Message ID
- If you know exact message numbers
- Faster than Option 2

### Option 4: List All Chats
- **Start here!**
- Shows all your chats with IDs
- Copy the chat ID you need

## Common Workflows

### Download from a Bot

```
1. Run: python download.py
2. Choose: 4 (List chats)
3. Find bot's chat ID (first column)
4. Press Enter
5. Choose: 2 (Search & download)
6. Enter: Bot's chat ID
7. Enter: Filename or ".mp4" for videos
8. Choose: A (Download by range)
9. Enter: 1-50 (or any range)
10. Wait for download!
```

### Download from a Channel

```
1. Open Telegram
2. Right-click on message
3. Copy Message Link
4. Run: python download.py
5. Choose: 1
6. Paste link
7. Done!
```

## Tips

- **Always use Option 4 first** to find chat IDs
- **For bots**, use Option 2 (they don't have message links)
- **For channels**, use Option 1 (fastest)
- **File filters** help download only what you need
- **Message ranges** like 1-100 download all files in that range

## Need Help?

- Check [USAGE.md](USAGE.md) for detailed examples
- Check [TDL_QUICKREF.md](TDL_QUICKREF.md) for command reference
- Run `tdl --help` for TDL help

---

**Made with ❤️ by Sonu Kumar**  
**MMIT Muzaffarpur**

*That's it! You're ready to download at 80-150+ MB/s! 🚀*
