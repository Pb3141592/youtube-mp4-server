from yt_dlp import YoutubeDL

def get_mp4_url(video_id):
    ydl_opts = {
        "format": "mp4[height<=1080]",
        "quiet": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
        return info["url"]
