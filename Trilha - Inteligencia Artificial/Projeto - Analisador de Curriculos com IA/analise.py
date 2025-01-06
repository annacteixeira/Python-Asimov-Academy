import uuid

from helper import extract_data_analysis, get_pdf_paths, read_pdf
from database import AnalyzeDatabase
from ai import GroqClient
from models.summary import Resum
from models.file import File


database = AnalyzeDatabase()
ai = GroqClient()
job = database.get_job_by_name('Est\u00e1gio em Engenharia de Software (Front-end)')


cv_paths = get_pdf_paths(dir='Trilha - Inteligencia Artificial/Projeto - Analisador de Curriculos com IA/resumes')

for path in cv_paths:
    content = read_pdf(path)
    summary = ai.summarize_cv(content)
    opinion = ai.generate_opinion(content, job)
    score = ai.generate_score(content, job)
    
    resum_schema = Resum(
        id=str(uuid.uuid4()),
        job_id=job.get('id'),
        content=summary,
        file=str(path),
        opinion=opinion
    )
    
    file_schema = File(
        file_id=str(uuid.uuid4()),
        job_id=job.get('id')
    )
    
    analysis_schema = extract_data_analysis(summary, job.get('id'), resum_schema.id, score)
    
    database.summaries.insert(resum_schema.model_dump())
    database.analysis.insert(analysis_schema.model_dump())
    database.files.insert(file_schema.model_dump())