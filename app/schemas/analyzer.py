from pydantic import BaseModel

class AnalyzerRequest(BaseModel):
    resume_text: str
    job_text: str

class AnalyzerResponse(BaseModel):
    match_score: float