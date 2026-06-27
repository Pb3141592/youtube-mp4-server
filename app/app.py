from flask import Flask, request, jsonify
from downloader import get_mp4_url

app = Flask(__name__)

@app.route("/watch")
def watch():
    video_id = request.args.get("v")
    if not video_id:
        return jsonify({"error": "video id missing"}), 400

    url = get_mp4_url(video_id)
    return jsonify({"url": url})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
