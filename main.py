import subprocess
import json

video_url = "https://www.youtube.com/watch?v=_M7VhhptSrU"

# Run yt-dlp command to extract subtitles
cmd = [
    "yt-dlp",
    "--write-auto-sub",  # Use auto-generated subtitles
    "--skip-download",   # Don't download the video
    "--sub-format", "json3",  # Get subtitles in JSON format
    "--sub-lang", "en",  # Language preference (change if needed)
    "--print", "subtitles",
    video_url
]

# Execute the command and get the output
try:
    output = subprocess.run(cmd, capture_output=True, text=True, check=True)
    subtitles_json = json.loads(output.stdout)

    # Extract transcript text
    transcript = "\n".join([entry['text'] for entry in subtitles_json['events'] if 'text' in entry])
    print(transcript)
except Exception as e:
    print("Error:", e)