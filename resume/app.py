from flask import Flask, render_template, request
from resume_parser import build_prompt_from_file
from llm_handler import get_llm_response
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    suggestions = ""
    filename = ""
    skill_labels, skill_values, skill_colors = [], [], []
    
    if request.method == 'POST':
        file = request.files.get('resume')
        
        if file and file.filename:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            try:
                # Build LLM prompt & get skill comparison data
                prompt, predicted_domain, skill_labels, skill_values, skill_colors = build_prompt_from_file(file_path)
                
                # Get AI suggestions
                suggestions = get_llm_response(prompt)
                
            except ValueError as e:
                suggestions = f"Error: {str(e)}"
    
    return render_template(
        "index.html",
        suggestions=suggestions,
        filename=filename,
        skill_labels=skill_labels,
        skill_values=skill_values,
        skill_colors=skill_colors
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)
