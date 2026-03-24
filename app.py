from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form.get("message")

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=user_message
        )
        reply = response.output_text
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": "xato: " + str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
