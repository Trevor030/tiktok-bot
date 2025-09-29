from flask import Flask, render_template, request
from app.tiktok_bot import run_bot

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        hashtag = request.form["hashtag"]
        music_id = request.form["music_id"]
        result = run_bot(hashtag, music_id)
    return render_template("index.html", result=result)
