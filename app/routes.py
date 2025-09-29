from flask import Flask, render_template, request
from app.tiktok_downloader import download_tiktok_video
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        urls = request.form["urls"].splitlines()
        for url in urls:
            res = download_tiktok_video(url.strip())
            result.append(res)
    return render_template("index.html", result=result)
