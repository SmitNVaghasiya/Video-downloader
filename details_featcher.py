import yt_dlp

def fetch_video_info(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'skip_download': True,  # This option skips the actual download
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
            available_formats = []
            for fmt in formats:
                if fmt.get('acodec') != 'none' and fmt.get('vcodec') != 'none':  # Exclude audio-only and video-only formats
                    filesize = fmt.get('filesize', None)
                    if filesize:
                        filesize_mb = round(filesize / (1024 * 1024), 2)
                        filesize = f"{filesize_mb} MB" if filesize_mb < 1024 else f"{round(filesize_mb / 1024, 2)} GB"
                    format_info = {
                        'format_id': fmt.get('format_id'),
                        'resolution': f"{fmt.get('width')}x{fmt.get('height')}" if fmt.get('width') and fmt.get('height') else 'Audio',
                        'filesize': filesize or 'Unknown size',
                        'format_note': fmt.get('format_note', 'N/A')
                    }
                    available_formats.append(format_info)
            return info, available_formats
    except Exception as e:
        print(f"Error fetching video info: {str(e)}")  # Debug print
        return None, []