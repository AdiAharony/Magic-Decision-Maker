from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of possible answers
answers = [
    "Yes",
    "No",
    "Maybe",
    "Absolutely!",
    "Ask again later",
    "Trust your gut",
    "Why not?"
]

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    question = None

    if request.method == "POST":
        question = request.form.get("question")
        answer = random.choice(answers)

    return render_template("index.html", answer=answer, question=question)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
