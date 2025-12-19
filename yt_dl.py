import yt_dlp
import os

def download_audio(url):
    # FIX: Define base_dir so the script knows where to save files
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to where your ffmpeg.exe files are (the current folder)
    ffmpeg_path = base_dir

    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': ffmpeg_path,
        
        # This creates a folder named after the playlist (or song) and puts the mp3 inside
        'outtmpl': os.path.join(base_dir, '%(playlist_title|title)s', '%(title)s.%(ext)s'),
        
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
            {
                'key': 'EmbedThumbnail',
            },
            {
                'key': 'FFmpegMetadata',
                'add_metadata': True,
            },
        ],
        'writethumbnail': True,
        'noplaylist': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Starting download: {url}")
            ydl.download([url])
            print("\nDone! Your files are in the sub-folder.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    link = input("Enter YouTube Video or Playlist URL: ").strip()
    download_audio(link)