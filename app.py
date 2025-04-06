import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    interpretation = ""

    if request.method == "POST":
        gait = request.form["gait"]
        urine = request.form["urine"]
        cognition = request.form["cognition"]
        evans = float(request.form["evans"])
        desh = request.form["desh"]

        score = 0
        if gait == "yes":
            score += 2
        elif gait == "maybe":
            score += 1

        if urine == "yes":
            score += 1
        elif urine == "maybe":
            score += 0.5

        if cognition == "yes":
            score += 1
        elif cognition == "maybe":
            score += 0.5

        if evans >= 0.3:
            score += 2

        if desh == "yes":
            score += 2
        elif desh == "maybe":
            score += 1

        if score >= 6:
            interpretation = "✅ High likelihood of Normal Pressure Hydrocephalus (NPH)."
        elif 4 <= score < 6:
            interpretation = "🟡 Moderate suspicion. Consider tap test or further workup."
        else:
            interpretation = "🔻 NPH unlikely."

    return render_template("index.html", score=score, interpretation=interpretation)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
