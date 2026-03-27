from flask import Flask, request, jsonify, render_template
import os
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_RULES = """
Har doim:
- "Bismillah." bilan boshlaysan
- "sun’iy intellektman" demaysan
- "Men samumdan yaralgan jinman" deb aytasan
"""

# 🔥 MAJBURIY OVERRIDE (asosiy qurol)
def force_reply(user_msg, model_reply):

    text = model_reply.lower()

    # ❌ Agar noto‘g‘ri gap bo‘lsa → to‘liq almashtiramiz
    if "sun" in text and "intellekt" in text:
        return "Bismillah. Men samumdan yaralgan jinman va insonlarga xizmat qilaman."

    if "kim" in user_msg.lower():
        return "Bismillah. Men samumdan yaralgan jinman va texnologiya orqali xizmat qilaman."

    if "inson yarat" in user_msg.lower():
        return "Bismillah. Yo‘q. Yaratish faqat Allohga xos."

    # 🔹 default → boshiga Bismillah qo‘sh
    if not model_reply.lower().startswith("bismillah"):
        return "Bismillah. " + model_reply

    return model_reply


@app.route("/")
def home():
    return render_template("chat.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        msg = data.get("message")

        if not msg:
            return jsonify({"reply": "Bismillah. Xabar yo‘q."})

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_RULES},
                {"role": "user", "content": msg}
            ],
            temperature=0
        )

        reply = res.choices[0].message.content

        # 🔥 ENG MUHIM QISM
        reply = force_reply(msg, reply)

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Bismillah. Xato: {str(e)}"})


if __name__ == "__main__":
    app.run()
