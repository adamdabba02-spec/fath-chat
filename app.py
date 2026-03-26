from flask import Flask, request, jsonify, render_template
import os
from openai import OpenAI

app = Flask(__name__)

# API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Home page
@app.route("/")
def home():
    return render_template("chat.html")

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        msg = data.get("message")

        if not msg:
            return jsonify({"reply": "xato: message bo'sh"}), 400

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Qisqa va aniq javob ber."},
                {"role": "user", "content": msg}
            ]
        )

        reply = res.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"xato: {str(e)}"}), 500


# Run (Render uchun muhim)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
