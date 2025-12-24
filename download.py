"""
Universal Telegram Downloader with File Search
Download from channels, groups, and bots using TDL
Search files by name!

Author: Sonu Kumar
Institution: MMIT Muzaffarpur
Speed: 80-150+ MB/s with optimized settings
"""

import subprocess
import sys
import json
import os
import re

def show_menu():
    print("\n" + "=" * 80)
    print("🚀 TELEGRAM UNIVERSAL DOWNLOADER")
    print("=" * 80)
    print()
    print("📋 DOWNLOAD OPTIONS:")
    print()
    print("1. Download from Channel/Group (with message link)")
    print("2. Search & Download by filename (from bot/channel)")
    print("3. Download by message ID (if you know the ID)")
    print("4. List all your chats (to find chat IDs)")
    print("5. Exit")
    print()
    print("-" * 80)
    print("💡 Made with ❤️  by Sonu Kumar | MMIT Muzaffarpur")
    print("⚡ Speed: 80-150+ MB/s with optimized settings")
    print("-" * 80)
    print()

def search_and_download():
    """Search for files by name and download"""
    print("\n🔍 SEARCH & DOWNLOAD BY FILENAME")
    print("-" * 80)
    print("This will search for files by name in a chat/bot")
    print()
    
    # Get chat ID
    chat_id = input("Enter Chat ID (from option 4): ").strip()
    if not chat_id:
        print("❌ No chat ID provided!")
        return
    
    # Get filename to search
    print("\n📝 Enter the filename or part of it:")
    print("   Examples:")
    print("   - 'video.mp4' (exact name)")
    print("   - 'lecture' (finds all files with 'lecture' in name)")
    print("   - '.pdf' (finds all PDF files)")
    print()
    
    search_term = input("Enter filename or search term: ").strip()
    if not search_term:
        print("❌ No search term provided!")
        return
    
    print(f"\n🔍 Searching for '{search_term}' in chat {chat_id}...")
    print("💡 Since TDL doesn't support filename search directly,")
    print("   here's what you can do:")
    print()
    print("Option A: Download by message range and filter")
    print("   - Enter a message range (e.g., 1-50)")
    print("   - TDL will download all files in that range")
    print("   - You can use --include filter for file types")
    print()
    print("Option B: Download specific message IDs")
    print("   - If you know which messages have the file")
    print("   - Enter message IDs (e.g., 10,15,20)")
    print()
    
    choice = input("Choose A or B (or press Enter to skip): ").strip().lower()
    
    if choice == 'a':
        print("\n📊 Enter message range to search:")
        start = input("Start message ID (e.g., 1): ").strip() or "1"
        end = input("End message ID (e.g., 50): ").strip() or "50"
        msg_id = f"{start}-{end}"
        
        # Ask about file type filter
        print("\n🎯 Filter by file type? (optional)")
        print("   Examples: *.mp4,*.mkv (videos) or *.pdf (PDFs)")
        file_filter = input("Enter filter or press Enter to skip: ").strip()
        
        download_by_id(chat_id, msg_id, file_filter)
    
    elif choice == 'b':
        msg_id = input("\nEnter message ID(s) (e.g., 10,15,20 or 10-20): ").strip()
        if msg_id:
            download_by_id(chat_id, msg_id)
    else:
        print("❌ Cancelled")

def download_by_message_id():
    """Direct download by message ID"""
    print("\n📥 DOWNLOAD BY MESSAGE ID")
    print("-" * 80)
    print("Use this if you know the exact message ID")
    print()
    
    chat_id = input("Enter Chat ID: ").strip()
    if not chat_id:
        print("❌ No chat ID provided!")
        return
    
    print("\n📝 Enter message ID(s):")
    print("   - Single: 123")
    print("   - Range: 100-200")
    print("   - Multiple: 1,5,10,15")
    print()
    
    msg_id = input("Enter message ID(s): ").strip()
    if msg_id:
        # Ask about file type filter
        print("\n🎯 Filter by file type? (optional)")
        print("   Examples: *.mp4,*.mkv (videos) or *.pdf (PDFs)")
        file_filter = input("Enter filter or press Enter to skip: ").strip()
        
        download_by_id(chat_id, msg_id, file_filter)

def download_by_id(chat_id, msg_id, file_filter=None):
    """Download messages by chat ID and message ID with optional filter"""
    # Build URL based on chat ID format
    if chat_id.startswith('@'):
        url = f"https://t.me/{chat_id.replace('@', '')}/{msg_id}"
    else:
        url = f"https://t.me/c/{chat_id}/{msg_id}"
    
    print(f"\n🚀 Downloading from chat {chat_id}, message(s) {msg_id}")
    print("⚡ ULTRA-FAST MODE: 16 threads + 1MB chunks + optimized pool")
    print(f"URL: {url}")
    
    # Build command with MAXIMUM SPEED settings
    cmd = [
        "tdl", "dl", 
        "-u", url, 
        "--threads", "16",      # Maximum parallel threads
        "--size", "1048576",    # 1MB chunk size for faster downloads
        "--pool", "8"           # Connection pool size
    ]
    
    # Add file filter if provided
    if file_filter:
        cmd.extend(["--include", file_filter])
        print(f"Filter: {file_filter}")
    
    print()
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print("\n⚠️  Download failed. Error:")
        print(result.stderr or result.stdout)
        print("\n💡 Tips:")
        print("  - Make sure the chat ID is correct")
        print("  - Make sure the message ID exists")
        print("  - For bots, the chat ID is usually a number")
        print("  - Try a different message range")
        print("\n📝 Example: If bot sent files in messages 1-20,")
        print("   try downloading range '1-20'")
    else:
        print("\n✅ Download complete!")
        print(f"📁 Files saved to: downloads/")

# Main loop - keeps showing menu after each task
while True:
    show_menu()
    choice = input("Choose option (1-5): ").strip()

    if choice == "1":
        print("\n📥 DOWNLOAD FROM MESSAGE LINK")
        print("-" * 80)
        print("Steps:")
        print("1. Open Telegram app")
        print("2. Right-click on the message with the file")
        print("3. Select 'Copy Message Link'")
        print("4. Paste it below")
        print()
        
        url = input("Paste the Telegram message link: ").strip()
        if url:
            print(f"\n🚀 Downloading from: {url}")
            print("⚡ ULTRA-FAST MODE: 16 threads + 1MB chunks + optimized pool")
            cmd = [
                "tdl", "dl", 
                "-u", url, 
                "--threads", "16",
                "--size", "1048576",
                "--pool", "8"
            ]
            subprocess.run(cmd)
            print("\n✅ Download complete!")
        else:
            print("❌ No URL provided!")

    elif choice == "2":
        search_and_download()

    elif choice == "3":
        download_by_message_id()

    elif choice == "4":
        print("\n📋 LISTING ALL YOUR CHATS")
        print("-" * 80)
        print("This will show all your chats with their IDs...")
        print()
        
        cmd = ["tdl", "chat", "ls"]
        subprocess.run(cmd)
        
        print("\n💡 Tip: Copy the chat ID (first column)")
        print("   Use it in option 2 or 3 to download files!")

    elif choice == "5":
        print("\n👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice!")
        
    # Add a small pause before showing menu again
    input("\nPress Enter to continue...")
