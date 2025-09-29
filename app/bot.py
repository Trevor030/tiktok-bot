from TikTokApi import TikTokApi
import requests
import os
import time

def run_bot(hashtag, music_id, count=5):
    api = TikTokApi()
    DOWNLOAD_FOLDER = "downloads"
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    results = []

    videos = api.hashtag(name=hashtag).videos(count=count)
    filtered = [v for v in videos if v.music.id == music_id]

    for v in filtered:
        video_id = v.id
        url = v.video.download_addr
        res = requests.get(url, headers={"User-Agent": "okhttp"})
        path = f"{DOWNLOAD_FOLDER}/{video_id}.mp4"
        with open(path, "wb") as f:
            f.write(res.content)
        results.append(video_id)

    return results
