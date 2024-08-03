import yt_dlp
import os

def download_video(url, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            if 'entries' in info:  
                for entry in info['entries']:
                    filename = ydl.prepare_filename(entry)
                    print(f"Downloaded: {filename}")
                return f"Playlist '{info['title']}' downloaded", '', info['title'], info['thumbnail']
            else:
                filename = ydl.prepare_filename(info)
                return f"Downloaded: {filename}", '', info['title'], info['thumbnail']
    except Exception as e:
        return 'Something Went Wrong', str(e), '', ''
