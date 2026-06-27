from flask import Flask, request, jsonify
from downloader import download_video

app = Flask(__name__)

@app.route("/")
def index():
    return "YouTube MP4 API is running."

@app.route("/download", methods=["GET"])
def download():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        file_path = download_video(url)
        return jsonify({"file": file_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
