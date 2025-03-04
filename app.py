import os
import requests
from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

PROXIES = {
    "http": "http://dahydzuv-rotate:qi0v0hqggj55@p.webshare.io:80/",
    "https": "http://dahydzuv-rotate:qi0v0hqggj55@p.webshare.io:80/"
}

app = Flask(__name__)

@app.route("/get_transcript", methods=["GET"])
def get_transcript():
    video_id = request.args.get("video_id")
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, proxies=PROXIES)
        return jsonify({"transcript": transcript})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))  # Use Railway-assigned port
