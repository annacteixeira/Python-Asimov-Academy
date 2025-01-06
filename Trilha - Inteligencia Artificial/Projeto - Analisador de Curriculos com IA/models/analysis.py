from pydantic import BaseModel
from typing import List

class Analysis(BaseModel):
    id: str
    job_id: str
    summary_id: str
    name: str
    skills: List[str]
    education: List[str]
    languages: List[str]
    score: float