from tinydb import TinyDB, Query

class AnalyzeDatabase(TinyDB):
    def __init__(self, db_path='Trilha - Inteligencia Artificial/Projeto - Analisador de Curriculos com IA/db.json'):
        super().__init__(db_path)
        
        self.jobs = self.table('jobs')
        self.summaries = self.table('summaries')
        self.analysis = self.table('analysis')
        self.files = self.table('files')
    
    def get_job_by_name(self, name):
        job = Query()
        result = self.jobs.search(job.name == name)
        return result[0] if result else None
    
    def get_summary_by_id(self, id):
        summary = Query()
        result = self.summaries.search(summary.id == id)
        return result[0] if result else None
    
    def get_analysys_by_job_id(self, job_id):
        analysis = Query()
        result = self.analysis.search(analysis.job_id == job_id)
        return result
    
    def get_summaries_by_job_id(self, job_id):
        summary = Query()
        result = self.summaries.search(summary.job_id == job_id)
        return result
    
    def delete_all_summaries_by_job_id(self, job_id):
        summary = Query()
        self.summaries.remove(summary.job_id == job_id)
        
    def delete_all_analysis_by_job_id(self, job_id):
        analysis = Query()
        self.analysis.remove(analysis.job_id == job_id)
    
    def delete_all_files_by_job_id(self, job_id):
        file = Query()
        self.files.remove(file.job_id == job_id)
