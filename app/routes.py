from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        hashtag = request.form["hashtag"]
        music_id = request.form["music_id"]
        # Placeholder: qui inseriresti la tua logica TikTokApi
        result = [f"Scaricato: #{hashtag} con musica {music_id} (simulazione)"]
    return render_template("index.html", result=result)
