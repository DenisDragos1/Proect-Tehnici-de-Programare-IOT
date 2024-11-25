import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask is running in the cloud!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # PORT din mediu sau fallback la 5000
    app.run(host="0.0.0.0", port=port)
