from flask import Flask, render_template, request, jsonify
from app.ai.resume_parser import parse_resume
from app.ai.jd_analyzer import analyze_jd
from app.ai.scoring import calculate_score

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    resume_text = request.json["resume"]
    jd_text = request.json["jd"]

    resume_data = parse_resume(resume_text)
    jd_analysis = analyze_jd(resume_data, jd_text)
    score = calculate_score(resume_data, jd_analysis)

    return jsonify({
        "score": score,
        "resume_data": resume_data,
        "jd_analysis": jd_analysis
    })

if __name__ == "__main__":
    app.run(debug=True)