from TikTokApi import TikTokApi
import requests
import os
import time

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def run_bot(hashtag, music_id, count=5):
    api = TikTokApi()
    results = []

    try:
        hashtag_obj = api.hashtag(name=hashtag)
        videos = hashtag_obj.videos(count=count)
        for video in videos:
            if video.music.id == music_id:
                video_id = video.id
                url = video.video.download_addr
                headers = {"User-Agent": "okhttp"}
                response = requests.get(url, headers=headers)
                path = os.path.join(DOWNLOAD_FOLDER, f"{video_id}.mp4")
                with open(path, "wb") as f:
                    f.write(response.content)
                results.append(f"✅ Scaricato: {video_id}")
    except Exception as e:
        results.append(f"❌ Errore: {e}")

    return results
