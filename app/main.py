from fastapi import FastAPI, UploadFile, File, Form
from app.services.matcher import match_resume_to_job, detect_skill_gaps
from app.utils.pdf_utils import extract_text_from_pdf
from app.schemas.analyzer import AnalyzerRequest, AnalyzerResponse

app = FastAPI()

@app.post("/analyze", response_model=AnalyzerResponse)
def analyze_resume(data: AnalyzerRequest):
    score = match_resume_to_job(data.resume_text, data.job_text)
    missing_skills = detect_skill_gaps(data.resume_text, data.job_text)
    return {"match_score": score, "missing_skills": missing_skills}

@app.post("/analyze-file")
async def analyze_resume_file(
    resume: UploadFile = File(...),
    job_text: str = Form(...)
):
    file_location = f"/tmp/{resume.filename}"
    with open(file_location, "wb") as f:
        f.write(await resume.read())

    resume_text = extract_text_from_pdf(file_location)
    score = match_resume_to_job(resume_text, job_text)
    missing_skills = detect_skill_gaps(resume_text, job_text)
    return {
        "match_score": score,
        "missing_skills": missing_skills,
        "resume_text": resume_tex
    }