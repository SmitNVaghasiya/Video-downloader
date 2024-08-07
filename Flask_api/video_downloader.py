# import yt_dlp
# import os

# def fetch_video_info(url):
#     ydl_opts = {
#         'format': 'bestvideo+bestaudio/best',
#         'skip_download': True,  # This option skips the actual download
#     }

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=False)
#             formats = info.get('formats', [])
#             available_formats = []
#             for fmt in formats:
#                 if fmt.get('acodec') != 'none' and fmt.get('vcodec') != 'none':  # Exclude audio-only and video-only formats
#                     format_info = {
#                         'format_id': fmt.get('format_id'),
#                         'resolution': f"{fmt.get('width')}x{fmt.get('height')}",
#                         'filesize': fmt.get('filesize', 'N/A')
#                     }
#                     available_formats.append(format_info)
#             return info, available_formats
#     except Exception as e:
#         print(f"Error fetching video info: {str(e)}")  # Debug print
#         return None, []

# def download_video(url, format_id, directory):
#     if not os.path.exists(directory):
#         os.makedirs(directory)

#     ydl_opts = {
#         'format': format_id,
#         'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),
#     }

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=True)
#             filename = ydl.prepare_filename(info)
#             return filename, '', info['title'], info.get('thumbnail', '')
#     except Exception as e:
#         print(f"Error downloading video: {str(e)}")  # Debug print
#         return 'Something Went Wrong', str(e), '', ''


import os 
import yt_dlp
def download_video(url, format_id, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    ydl_opts = {
        'format': format_id,
        'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            return filename, '', info['title'], info.get('thumbnail', '')
    except Exception as e:
        print(f"Error downloading video: {str(e)}")  # Debug print
        return 'Something Went Wrong', str(e), '', ''