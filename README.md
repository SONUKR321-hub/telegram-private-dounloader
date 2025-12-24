# 🚀 Telegram Ultra-Fast Downloader

Download files from Telegram at **80-150+ MB/s** using TDL with optimized settings!

## ✨ Features

- ⚡ **Ultra-fast downloads** - 80-150+ MB/s with 16 parallel threads
- 🤖 **Bot support** - Download from bots without message links
- 🔍 **File search** - Search and download by filename
- 📊 **Easy interface** - Simple menu-driven Python script
- 🎯 **File filtering** - Download only specific file types (videos, PDFs, etc.)
- 🔄 **Continuous mode** - Download multiple files without restarting

## 📋 Requirements

- **Go** (for TDL installation)
- **Python 3.7+** (for the download script)
- **Telegram API credentials** (free from https://my.telegram.org)

## 🛠️ Installation

### Step 1: Install TDL

```bash
go install github.com/iyear/tdl@latest
```

### Step 2: Clone this repository

```bash
git clone https://github.com/yourusername/telegram-downloader.git
cd telegram-downloader
```

### Step 3: Login to Telegram

```bash
tdl login
```

You'll need:
- API ID and Hash from https://my.telegram.org
- Your phone number
- OTP code from Telegram

## 🚀 Quick Start

Run the downloader:

```bash
python download.py
```

Then follow the menu:

1. **Option 4** - List all your chats to find chat IDs
2. **Option 2** - Search and download by filename
3. **Option 3** - Download by message ID

## 📖 Usage Examples

### Download from a Bot

1. Run `python download.py`
2. Choose **Option 4** to find the bot's chat ID
3. Choose **Option 2** to search and download
4. Enter the bot's chat ID
5. Enter filename or search term (e.g., "video.mp4" or ".pdf")
6. Choose message range (e.g., 1-50)
7. Downloads automatically with maximum speed!

### Download from a Channel

1. Run `python download.py`
2. Choose **Option 1**
3. Copy message link from Telegram
4. Paste and press Enter
5. Done!

### Download Specific File Types

When downloading, you can filter by file type:
- Videos: `*.mp4,*.mkv,*.avi`
- PDFs: `*.pdf`
- Images: `*.jpg,*.png`

## ⚡ Speed Optimization

This downloader uses:
- **16 parallel threads** (maximum)
- **1MB chunk size** (optimized for large files)
- **Connection pool: 8** (faster concurrent downloads)

**Expected speeds:**
- Small files (<10MB): 30-50 MB/s
- Medium files (10-100MB): 50-80 MB/s
- Large files (>100MB): 80-150+ MB/s

## 📁 Project Structure

```
telegram-downloader/
├── download.py          # Main download script
├── downloads/           # Downloaded files go here
├── README.md           # This file
├── USAGE.md            # Detailed usage guide
└── TDL_QUICKREF.md     # TDL command reference
```

## 🆘 Troubleshooting

### "Not logged in" error
```bash
tdl login
```

### "Database is locked"
Close any other TDL processes and try again.

### Slow downloads?
Make sure you're using the Python script (`download.py`) which has optimized settings.

### Can't find chat ID?
Use **Option 4** in the menu to list all your chats with their IDs.

## 📚 Documentation

- **[USAGE.md](USAGE.md)** - Detailed usage guide with examples
- **[TDL_QUICKREF.md](TDL_QUICKREF.md)** - Quick reference for TDL commands
- **[TDL_GUIDE.md](TDL_GUIDE.md)** - Complete TDL documentation

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📝 License

This project is for educational purposes. Make sure to comply with Telegram's Terms of Service.

## ⭐ Star this repo if you find it useful!

---

**Made with ❤️ by [Sonu Kumar](https://github.com/yourusername)**  
**MMIT Muzaffarpur**

*For ultra-fast Telegram downloads at 80-150+ MB/s*
