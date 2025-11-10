from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

QUOTES = [
    "The only way to do great work is to love what you do. — Steve Jobs",
    "Believe you can and you're halfway there. — Theodore Roosevelt",
    "Be yourself; everyone else is already taken ― Oscar Wilde",
    "You miss 100 percent of the shots you don’t take. — Wayne Gretzky",
    "Be the change that you wish to see in the world. — Mahatma Gandhi",
    "Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring. ― Marilyn Monroe",
    "Yesterday is history, tomorrow is a mystery, today is a gift of God, which is why we call it the present. ― Bil Keane",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill",
    "In the middle of every difficulty lies opportunity. — Albert Einstein",
    "If you want to lift yourself up, lift up someone else. — Booker T. Washington",
    "Act as if what you do makes a difference. It does. — William James",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. — Ralph Waldo Emerson",
    "It always seems impossible until it’s done. — Nelson Mandela",
    "Dream big. Start small. Act now. — Robin Sharma"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quote")
def quote():
    return jsonify({"quote": random.choice(QUOTES)})

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 5000))  # default to 5000 if PORT isn’t set
    app.run(host="0.0.0.0", port=port, debug=False)

