from sklearn.metrics.pairwise import cosine_similarity
from app.models.nlp_model import get_embedding
from keybert import KeyBERT

kw_model = KeyBERT('all-MiniLM-L6-v2')

def match_resume_to_job(resume_text: str, job_text: str) -> float:
    resume_emb = get_embedding(resume_text)
    job_emb = get_embedding(job_text)
    similarity = cosine_similarity([resume_emb], [job_emb])[0][0]
    return round(similarity * 100, 2)

def extract_skills(text: str) -> list:
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words='english',
        top_n=15
    )
    return [kw[0] for kw in keywords]

def detect_skill_gaps(resume_text: str, job_text: str) -> list:
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_text))
    missing_skills = list(job_skills - resume_skills)
    return missing_skills