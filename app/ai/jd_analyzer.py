# app/ai/jd_analyzer.py
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def analyze_jd(resume_data, jd_text):
    candidate_labels = ["skills", "experience", "education"]
    results = classifier(jd_text, candidate_labels)
    return results
def analyze_jd(jd_text):
    return {"message": "JD Analysis function is working"}
