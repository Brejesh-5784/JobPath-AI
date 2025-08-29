import matplotlib
matplotlib.use('Agg')  # ✅ Prevents macOS GUI crash in Flask
import matplotlib.pyplot as plt
import io
import base64

def plot_skill_comparison(skill_comparison):
    labels = ['Present Skills', 'Missing Skills']
    values = [len(skill_comparison['present']), len(skill_comparison['missing'])]
    
    plt.figure(figsize=(5,5))
    plt.bar(labels, values, color=['green', 'red'])
    plt.title("Skill Gap Analysis")
    plt.ylabel("Number of Skills")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    encoded_img = base64.b64encode(img.getvalue()).decode('utf-8')
    plt.close()
    return encoded_img
