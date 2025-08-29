# resume_parser.py

import joblib
import docx
import PyPDF2
import re
from in_demand_skills import in_demand_skills as IN_DEMAND_SKILLS

# === Load trained artifacts ===
clf = joblib.load("model/knn_resume_classifier.joblib")
vectorizer = joblib.load("model/resume_vectorizer.joblib")
le = joblib.load("model/label_encoder.joblib")

# === Step 1: Extract text from file ===
def extract_text_from_file(file_path):
    if file_path.lower().endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif file_path.lower().endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    elif file_path.lower().endswith(".pdf"):
        text = ""
        with open(file_path, "rb") as f:
            pdf_reader = PyPDF2.PdfReader(f)
            for page in pdf_reader.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"
        return text
    else:
        raise ValueError("Unsupported file type. Use PDF, DOCX, or TXT.")

# === Step 2: Resume content check ===
def is_resume(text):
    resume_keywords = [
        "experience", "work history", "employment", "career",
        "education", "academic background", "degree", "university", "college",
        "skills", "technical skills", "soft skills", "competencies",
        "projects", "portfolio", "publications", "research",
        "certifications", "licenses", "training", "courses",
        "summary", "objective", "profile", "about me",
        "achievements", "awards", "honors",
        "languages", "tools", "frameworks",
        "contact", "email", "phone", "linkedin", "github"
    ]
    text_lower = text.lower()
    matches = sum(1 for kw in resume_keywords if kw in text_lower)
    return matches >= 3  # Require at least 3 keywords

# === Step 3: Predict domain ===
def predict_domain(resume_text):
    X_new = vectorizer.transform([resume_text])
    pred_idx = clf.predict(X_new)[0]
    return le.inverse_transform([pred_idx])[0]

# === Step 4: Extract skills from resume text ===
def extract_skills(resume_text):
    # Flatten skills list from all domains
    all_skills = set(skill.lower() for skills in IN_DEMAND_SKILLS.values() for skill in skills)
    found_skills = set()
    for skill in all_skills:
        if re.search(rf"\b{re.escape(skill)}\b", resume_text.lower()):
            found_skills.add(skill)
    return found_skills

# === Step 5: Compare skills ===
def compare_skills(predicted_domain, resume_skills):
    required_skills = IN_DEMAND_SKILLS.get(predicted_domain, [])
    skill_labels = []
    skill_values = []
    skill_colors = []

    for skill in required_skills:
        skill_labels.append(skill)
        if skill.lower() in resume_skills:
            skill_values.append(1)
            skill_colors.append("rgba(75, 192, 192, 0.6)")  # green
        else:
            skill_values.append(0)
            skill_colors.append("rgba(255, 99, 132, 0.6)")  # red

    return skill_labels, skill_values, skill_colors

# === Step 6: Build LLM prompt ===
def build_prompt_from_file(file_path):
    resume_text = extract_text_from_file(file_path)
    
    if not is_resume(resume_text):
        raise ValueError("The uploaded file does not appear to be a resume. Please upload a valid resume in PDF/DOCX/TXT format.")
    
    predicted_domain = predict_domain(resume_text)
    resume_skills = extract_skills(resume_text)
    skill_labels, skill_values, skill_colors = compare_skills(predicted_domain, resume_skills)
    
    prompt = f"""
You are an expert career assistant.

The uploaded resume belongs to the domain: {predicted_domain}.

1. Suggest career development tips for this role (e.g., certifications, projects, portfolio ideas).
2. If the user wants to switch to a different domain, suggest 2–3 alternative domains and explain how they can transition.
3. Recommend additional resume features or skills they can add to strengthen their profile.

Formatting Rules:
- Use only plain text
- Do not use any symbols such as *, #, or markdown formatting
- Write each section clearly with a heading followed by numbered or bulleted points
- Keep everything concise and professional

Output Format:
Job Role:
Career Tips:
Domain Switch Suggestions:
Extra Resume Features:
Resume:
\"\"\"
{resume_text}
\"\"\"
"""
    return prompt.strip(), predicted_domain, skill_labels, skill_values, skill_colors
