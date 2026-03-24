from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form.get("message")

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=user_message
        )

        reply = response.output[0].content[0].text
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": "Xato: " + str(e)})

if __name__ == "__main__":
    app.run(debug=True)
