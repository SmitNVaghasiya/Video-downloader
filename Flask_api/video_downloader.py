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
            filename = ydl.prepare_filename(info)
        return filename, ''
    except Exception as e:
        return '', str(e)
