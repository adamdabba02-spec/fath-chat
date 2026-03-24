from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# API KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "FATH Chat ishlayapti"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data.get("message")

    try:
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Qisqa va aniq javob ber"},
                {"role": "user", "content": msg}
            ]
        )

        # XATOGA QARSHI HIMOYA
        if res.choices and len(res.choices) > 0:
            reply = res.choices[0].message.content
        else:
            reply = "javob yo‘q"

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run()
