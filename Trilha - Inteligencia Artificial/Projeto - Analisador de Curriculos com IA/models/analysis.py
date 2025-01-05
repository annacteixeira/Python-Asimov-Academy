from pydantic import BaseModel
from typing import List

class Analysis(BaseModel):
    id: str
    job_id: str
    summary_id: str
    skills: List[str]
    education: List[str]
    language: List[str]
    score: float