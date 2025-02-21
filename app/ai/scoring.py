def calculate_score(resume_data, jd_analysis):
    score = 0
    # Example scoring logic
    score += len(set(resume_data["skills"]) & set(jd_analysis["skills"])) * 10
    score += len(set(resume_data["experience"]) & set(jd_analysis["experience"])) * 5
    score += len(set(resume_data["education"]) & set(jd_analysis["education"])) * 3
    return score
