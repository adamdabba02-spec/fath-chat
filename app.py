from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# API KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "Server ishlayapti"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data.get("message")

    try:
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Sen aniq va qisqa javob berasan"},
                {"role": "user", "content": msg}
            ]
        )
        return jsonify({"reply": res.choices[0].message.content})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run()
