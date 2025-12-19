# YouTube to MP3 Downloader (Python)

A streamlined Python utility designed to download individual songs or entire playlists from YouTube, convert them into high-quality MP3 format, and automatically organize them into folders with embedded metadata and album art.

## 🚀 Features
- **Playlist Support:** Automatically detects and downloads entire playlists into dedicated folders.
- **High-Quality Audio:** Extracts the best available audio stream and converts it to 192kbps MP3.
- **Smart Metadata:** Automatically embeds song titles, artist names, and YouTube thumbnails as album art.
- **Self-Contained:** Designed to run with local FFmpeg binaries for easy portability.

## 🛠️ Prerequisites
- **Python 3.x**
- **yt-dlp**: The core engine for video processing.
- **FFmpeg**: The industry standard for audio conversion and metadata embedding.

## 📜 Credits & Attribution

This project is made possible by the incredible work of the open-source community. Special thanks to the authors and contributors of the following tools:

### 1. yt-dlp
The primary engine used for downloading and parsing YouTube data. 
* **Authors:** The yt-dlp team and the original youtube-dl contributors.
* **Repository:** [https://github.com/yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)
* **License:** Unlicense

### 2. FFmpeg
The "Swiss Army Knife" of multimedia processing, used here for MP3 encoding and metadata tagging.
* **Authors:** Fabrice Bellard and the FFmpeg team.
* **Website:** [https://ffmpeg.org](https://ffmpeg.org)
* **License:** LGPL/GPL

### 3. Python Community
Special thanks to the developers of the `os` and `path` modules in the Python Standard Library that allow for cross-platform file management.

---

## 📖 How to Use
1. Place `ffmpeg.exe`, `ffprobe.exe`, and `ffplay.exe` in the same directory as the script.
2. Install dependencies:
   ```bash
   py -m pip install yt-dlp
3. Open a terminal/command-line in your scripts location and run 'py yt-dl.py'