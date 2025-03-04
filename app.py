import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask App Running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Railway's provided PORT
    app.run(host="0.0.0.0", port=port)