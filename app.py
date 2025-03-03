from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled

app = Flask(__name__)

@app.route('/get_transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')  # Get YouTube Video ID from URL parameters

    if not video_id:
        return jsonify({"error": "Missing video_id parameter"}), 400

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])  # Fetch auto-generated captions
        return jsonify(transcript)  # Return JSON response
    except TranscriptsDisabled:
        return jsonify({"error": "Transcripts are disabled for this video"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🔹 This line is missing in your script!
if __name__ == '__main__':
    app.run(debug=True)
