from flask import Flask, request, jsonify, render_template
import os
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        msg = data.get("message", "")

        if not msg:
            return jsonify({"reply": "xato: message yo‘q"}), 400

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Qisqa va aniq javob ber"},
                {"role": "user", "content": msg}
            ]
        )

        reply = res.choices[0].message.content

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"xato: {str(e)}"}), 500


if __name__ == "__main__":
    app.run()
