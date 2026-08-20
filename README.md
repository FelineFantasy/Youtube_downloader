# YouTube Video Downloader 🎥

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A simple utility for downloading videos from YouTube, written in Python. Paste a link — get the video!

## 📝 Description

**YouTube Video Downloader** is a simple console program for downloading videos from YouTube. It uses the powerful `yt-dlp` library and automatically saves videos in the best available quality.

### Features:
- 🚀 **Simplicity** — Paste a link and get the video
- 🎯 **Quality selection** — Choose video quality (4K, 1080p, 720p, 480p, 360p, audio)
- 📦 **Compact** — Just a few lines of code
- ⚡ **Speed** — Downloads videos in selected quality
- 🛡️ **Safety** — Error handling during download

## 🎮 How to Use

1. Run the program
2. Paste a YouTube video link
3. Choose video quality (1-6):
   - 1: Best (up to 4K)
   - 2: 1080p (Full HD)
   - 3: 720p (HD)
   - 4: 480p
   - 5: 360p
   - 6: Audio only (M4A)
4. Press Enter
5. Wait for the download completion message

The video will be saved in the same folder as the program.

## ⚙️ Installation

### Option 1: Download ZIP
1. Click the green **"Code"** button on this page
2. Select **"Download ZIP"**
3. Extract the archive
4. Install dependencies: `pip install -r requirements.txt`
5. Run the program: `python YouTube_Downloader.py`

### Option 2: Clone repository
```bash
git clone https://github.com/FelineFantasy/Youtube_downloader
cd Youtube_downloader
pip install -r requirements.txt
python youtube_downloader.py
```

## 💻 Example Usage

```
Enter YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Downloading...
Download complete!
```

## 📁 Project Files

```
Youtube_downloader/
├── .github/
│   └── FUNDING.yml           # Support link for DonationAlerts
├── youtube_downloader.py     # Main program file
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
├── LICENSE                   # MIT License file
└── .gitignore                # Files and folders to ignore
```

## 📋 Requirements

- Python 3.x
- yt-dlp

## 👤 Author
- **FelineFantasy**
- **License**: MIT
