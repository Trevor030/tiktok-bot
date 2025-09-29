from TikTokApi import TikTokApi
import requests
import os
import time

# ✅ CONFIGURAZIONE FILTRI
HASHTAG = "arte"               # senza #
MUSIC_ID = "7064358123608314113"  # ID musica TikTok (estraibile da URL o app)

# 📁 Cartella di destinazione
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Inizializza TikTokApi
api = TikTokApi()

def get_videos_by_hashtag(hashtag, count=10):
    print(f"Cercando video con hashtag #{hashtag}...")
    return api.hashtag(name=hashtag).videos(count=count)

def get_videos_by_music(music_id, count=10):
    print(f"Cercando video con musica ID {music_id}...")
    return api.music(id=music_id).videos(count=count)

def download_video(video):
    try:
        video_id = video.id
        url = video.video.download_addr
        headers = {"User-Agent": "okhttp"}
        res = requests.get(url, headers=headers)
        filepath = os.path.join(DOWNLOAD_FOLDER, f"{video_id}.mp4")

        with open(filepath, "wb") as f:
            f.write(res.content)
        print(f"✅ Scaricato: {filepath}")
    except Exception as e:
        print(f"❌ Errore durante il download: {e}")

def main():
    # Prendi video da hashtag
    videos = get_videos_by_hashtag(HASHTAG)

    # Filtra per musica, se necessario
    filtered_videos = [
        v for v in videos if v.music.id == MUSIC_ID
    ]

    print(f"Trovati {len(filtered_videos)} video validi.")

    for video in filtered_videos:
        download_video(video)
        time.sleep(1)

if __name__ == "__main__":
    main()
