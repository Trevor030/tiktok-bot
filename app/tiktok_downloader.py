import requests
import os
import re

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download_tiktok_video(url):
    try:
        # Usa l'API Tikmate gratuita (limitatamente pubblica)
        video_id_match = re.search(r'/video/(\d+)', url)
        if not video_id_match:
            return f"❌ URL non valido: {url}"
        video_id = video_id_match.group(1)

        lookup_url = "https://api.tikmate.app/api/lookup"
        resp = requests.post(lookup_url, data={"url": url})
        data = resp.json()

        download_url = f"https://tikmate.app/download/{data['token']}/{data['id']}.mp4"
        file_path = os.path.join(DOWNLOAD_FOLDER, f"{data['id']}.mp4")

        video_data = requests.get(download_url)
        with open(file_path, "wb") as f:
            f.write(video_data.content)

        return f"✅ Scaricato: {file_path}"
    except Exception as e:
        return f"❌ Errore: {e}"
