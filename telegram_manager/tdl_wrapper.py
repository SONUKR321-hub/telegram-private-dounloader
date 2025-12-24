"""
TDL Wrapper - Ultra-fast Telegram downloads using tdl CLI
This provides a Python interface to the blazing-fast tdl downloader
"""

import subprocess
import os
from pathlib import Path
from typing import Optional, List, Callable
import re


class TDLDownloader:
    """
    Wrapper for tdl (Telegram Downloader) CLI tool
    Provides ultra-fast downloads with multi-threading support
    """
    
    def __init__(self, download_dir: str = "downloads"):
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(exist_ok=True)
        
        # Check if tdl is installed
        if not self._is_tdl_installed():
            raise RuntimeError(
                "tdl is not installed. Install it with: go install github.com/iyear/tdl@latest"
            )
    
    def _is_tdl_installed(self) -> bool:
        """Check if tdl is installed and available"""
        try:
            result = subprocess.run(
                ["tdl", "version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.returncode == 0
        except (subprocess.SubprocessError, FileNotFoundError):
            return False
    
    def login(self, api_id: Optional[str] = None, api_hash: Optional[str] = None) -> bool:
        """
        Login to Telegram using tdl
        
        Args:
            api_id: Telegram API ID (optional, will prompt if not provided)
            api_hash: Telegram API Hash (optional, will prompt if not provided)
            
        Returns:
            True if login successful
        """
        cmd = ["tdl", "login"]
        
        env = os.environ.copy()
        if api_id:
            env["TDL_APP_ID"] = api_id
        if api_hash:
            env["TDL_APP_HASH"] = api_hash
        
        try:
            result = subprocess.run(
                cmd,
                env=env,
                check=False
            )
            return result.returncode == 0
        except subprocess.SubprocessError as e:
            print(f"Login failed: {e}")
            return False
    
    def download_url(
        self,
        url: str,
        threads: int = 16,
        chunk_size: int = 524288,  # 512KB
        output_dir: Optional[str] = None,
        progress_callback: Optional[Callable[[str], None]] = None,
        include_patterns: Optional[List[str]] = None,
        exclude_patterns: Optional[List[str]] = None,
        min_size: Optional[int] = None,
        max_size: Optional[int] = None,
        resume: bool = True
    ) -> tuple[bool, str]:
        """
        Download from Telegram URL using tdl (ULTRA FAST!)
        
        Args:
            url: Telegram URL (e.g., https://t.me/c/CHAT_ID/MSG_ID)
            threads: Number of parallel connections (1-16, default: 16 for max speed)
            chunk_size: Download chunk size in bytes (default: 512KB)
            output_dir: Custom output directory (default: self.download_dir)
            progress_callback: Callback function for progress updates
            include_patterns: File patterns to include (e.g., ["*.mp4", "*.mkv"])
            exclude_patterns: File patterns to exclude
            min_size: Minimum file size in bytes
            max_size: Maximum file size in bytes
            resume: Continue interrupted downloads
            
        Returns:
            Tuple of (success, message)
        """
        output_path = Path(output_dir) if output_dir else self.download_dir
        output_path.mkdir(exist_ok=True)
        
        # Build command
        cmd = [
            "tdl", "dl",
            "-u", url,
            "--threads", str(threads),
            "--size", str(chunk_size),
            "-d", str(output_path)
        ]
        
        # Add optional parameters
        if resume:
            cmd.append("--continue")
        
        if include_patterns:
            cmd.extend(["--include", ",".join(include_patterns)])
        
        if exclude_patterns:
            cmd.extend(["--exclude", ",".join(exclude_patterns)])
        
        if min_size:
            cmd.extend(["--min-size", str(min_size)])
        
        if max_size:
            cmd.extend(["--max-size", str(max_size)])
        
        try:
            print(f"🚀 Starting ultra-fast download with {threads} threads...")
            print(f"📥 URL: {url}")
            print(f"📁 Output: {output_path}")
            
            # Run tdl download
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                return True, f"✅ Downloaded successfully to {output_path}"
            else:
                error_msg = result.stderr or result.stdout or "Unknown error"
                return False, f"❌ Download failed: {error_msg}"
                
        except subprocess.SubprocessError as e:
            return False, f"❌ Download error: {str(e)}"
    
    def download_message(
        self,
        chat_id: str,
        message_id: int,
        threads: int = 16,
        output_dir: Optional[str] = None
    ) -> tuple[bool, str]:
        """
        Download a specific message from a chat
        
        Args:
            chat_id: Chat ID or username
            message_id: Message ID to download
            threads: Number of parallel connections (default: 16)
            output_dir: Custom output directory
            
        Returns:
            Tuple of (success, message)
        """
        url = f"https://t.me/c/{chat_id}/{message_id}"
        return self.download_url(url, threads=threads, output_dir=output_dir)
    
    def download_range(
        self,
        chat_id: str,
        start_msg: int,
        end_msg: int,
        threads: int = 16,
        output_dir: Optional[str] = None,
        **kwargs
    ) -> tuple[bool, str]:
        """
        Download a range of messages from a chat
        
        Args:
            chat_id: Chat ID or username
            start_msg: Starting message ID
            end_msg: Ending message ID
            threads: Number of parallel connections (default: 16)
            output_dir: Custom output directory
            **kwargs: Additional arguments passed to download_url
            
        Returns:
            Tuple of (success, message)
        """
        url = f"https://t.me/c/{chat_id}/{start_msg}-{end_msg}"
        return self.download_url(url, threads=threads, output_dir=output_dir, **kwargs)
    
    def download_chat(
        self,
        chat_username: str,
        limit: int = 100,
        threads: int = 16,
        output_dir: Optional[str] = None,
        **kwargs
    ) -> tuple[bool, str]:
        """
        Download files from a chat/channel
        
        Args:
            chat_username: Chat username (e.g., @telegram)
            limit: Number of messages to fetch (0 = all)
            threads: Number of parallel connections (default: 16)
            output_dir: Custom output directory
            **kwargs: Additional arguments passed to download_url
            
        Returns:
            Tuple of (success, message)
        """
        url = f"https://t.me/{chat_username}"
        
        cmd_args = kwargs.copy()
        if limit > 0:
            # Note: tdl doesn't have a direct limit flag, this is handled by message range
            pass
        
        return self.download_url(url, threads=threads, output_dir=output_dir, **cmd_args)
    
    def list_chats(self) -> List[dict]:
        """
        List available chats
        
        Returns:
            List of chat dictionaries
        """
        try:
            result = subprocess.run(
                ["tdl", "chat", "ls"],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                # Parse output (format depends on tdl version)
                return self._parse_chat_list(result.stdout)
            return []
            
        except subprocess.SubprocessError:
            return []
    
    def _parse_chat_list(self, output: str) -> List[dict]:
        """Parse chat list output"""
        chats = []
        # This is a simple parser - adjust based on actual tdl output format
        for line in output.split('\n'):
            if line.strip():
                chats.append({"raw": line})
        return chats
    
    @staticmethod
    def format_size(bytes_size: int) -> str:
        """Format bytes to human-readable size"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_size < 1024.0:
                return f"{bytes_size:.2f} {unit}"
            bytes_size /= 1024.0
        return f"{bytes_size:.2f} PB"


# Convenience functions
def quick_download(url: str, threads: int = 16, output_dir: str = "downloads") -> bool:
    """
    Quick download function - downloads with maximum speed
    
    Args:
        url: Telegram URL
        threads: Number of threads (default: 16 for max speed)
        output_dir: Output directory
        
    Returns:
        True if successful
    """
    downloader = TDLDownloader(output_dir)
    success, message = downloader.download_url(url, threads=threads)
    print(message)
    return success


def download_videos_only(url: str, threads: int = 16, output_dir: str = "downloads") -> bool:
    """
    Download only video files
    
    Args:
        url: Telegram URL
        threads: Number of threads
        output_dir: Output directory
        
    Returns:
        True if successful
    """
    downloader = TDLDownloader(output_dir)
    success, message = downloader.download_url(
        url,
        threads=threads,
        include_patterns=["*.mp4", "*.mkv", "*.avi", "*.mov", "*.webm"]
    )
    print(message)
    return success


def download_large_files_only(
    url: str,
    min_size_mb: int = 10,
    threads: int = 16,
    output_dir: str = "downloads"
) -> bool:
    """
    Download only large files (>= min_size_mb)
    
    Args:
        url: Telegram URL
        min_size_mb: Minimum file size in MB
        threads: Number of threads
        output_dir: Output directory
        
    Returns:
        True if successful
    """
    downloader = TDLDownloader(output_dir)
    min_bytes = min_size_mb * 1024 * 1024
    success, message = downloader.download_url(
        url,
        threads=threads,
        min_size=min_bytes
    )
    print(message)
    return success


# Example usage
if __name__ == "__main__":
    # Initialize downloader
    tdl = TDLDownloader("downloads")
    
    # Example 1: Download a specific message (ULTRA FAST with 16 threads!)
    success, msg = tdl.download_url(
        "https://t.me/c/1234567890/100",
        threads=16  # Maximum speed!
    )
    print(msg)
    
    # Example 2: Download message range
    success, msg = tdl.download_range(
        chat_id="1234567890",
        start_msg=100,
        end_msg=200,
        threads=16
    )
    print(msg)
    
    # Example 3: Download only videos
    success, msg = tdl.download_url(
        "https://t.me/my_channel",
        threads=16,
        include_patterns=["*.mp4", "*.mkv"]
    )
    print(msg)
    
    # Example 4: Download large files only (>50MB)
    success, msg = tdl.download_url(
        "https://t.me/my_channel",
        threads=16,
        min_size=50 * 1024 * 1024  # 50MB
    )
    print(msg)
    
    # Quick download (convenience function)
    quick_download("https://t.me/c/1234567890/500", threads=16)
