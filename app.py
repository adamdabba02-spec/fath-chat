from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form.get("message")
    return f"Sen yozding: {user_message}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
