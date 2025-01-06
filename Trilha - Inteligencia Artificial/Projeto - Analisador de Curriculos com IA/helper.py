import re, uuid, os
import fitz
from models.analysis import Analysis

def read_pdf(file_path):
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
            
    return text

def extract_data_analysis(resum_cv, job_id, summary_id, score) -> Analysis:
    sections_dict = {
        "id": str(uuid.uuid4()),
        "job_id": job_id,
        "summary_id": summary_id,
        "name": "",
        "skills": [],
        "education": [],
        "languages": [], 
        "score": score
    }


    patterns = {
        "name": r"(?:## Nome Completo\s*|Nome Completo\s*\|\s*Valor\s*\|\s*\S*\s*\|\s*)(.*)",
        "skills": r"## Habilidades\s*([\s\S]*?)(?=##|$)",
        "education": r"## Educação\s*([\s\S]*?)(?=##|$)",
        "languages": r"## Idiomas\s*([\s\S]*?)(?=##|$)",
        "salary_expectation": r"## Pretensão Salarial\s*([\s\S]*?)(?=##|$)"
    }

    def clean_string(string: str) -> str:
        return re.sub(r"[\*\-]+", "", string).strip()

    for section, pattern in patterns.items():
        match = re.search(pattern, resum_cv)
        if match:
            if section == "name":
                sections_dict[section] = clean_string(match.group(1))
            else:
                sections_dict[section] = [clean_string(item) for item in match.group(1).split('\n') if item.strip()]

    # Validação para garantir que nenhuma seção obrigatória esteja vazia
    for key in ["name", "education", "skills"]:
        if not sections_dict[key] or (isinstance(sections_dict[key], list) and not any(sections_dict[key])):
            raise ValueError(f"A seção '{key}' não pode ser vazia ou uma string vazia.")

    return Analysis(**sections_dict)

def get_pdf_paths(dir):
    pdf_paths = []
    
    for filename in os.listdir(dir):
        if filename.endswith('.pdf'):
            file_path = os.path.join(dir, filename)
            pdf_paths.append(file_path)
            
    return pdf_paths

