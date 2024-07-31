import yt_dlp
import os

def download_video(url, directory):
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Download options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        # Assuming the file name can be retrieved or is known
        filename = 'example_video.mp4'  # Replace this with actual file name logic
        return filename, ''  # Return filename and empty error message
    except Exception as e:
        return '', str(e)
