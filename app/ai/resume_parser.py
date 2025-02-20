import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def parse_resume(resume_text):
    doc = nlp(resume_text)
    skills = []
    experience = []
    education = []

    for ent in doc.ents:
        if ent.label_ == "SKILL":
            skills.append(ent.text)
        elif ent.label_ == "ORG":
            experience.append(ent.text)
        elif ent.label_ == "EDU":
            education.append(ent.text)

    return {
        "skills": skills,
        "experience": experience,
        "education": education
    }