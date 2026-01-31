from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

model = SentenceTransformer("all-MiniLM-L6-v2")

def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.lower()

def get_match_score(resume_text, job_text):
    embeddings = model.encode([resume_text, job_text])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(score * 100, 2)

def extract_keywords(text):
    words = set(text.split())
    return words

def missing_skills(resume_text, job_text):
    resume_words = extract_keywords(resume_text)
    job_words = extract_keywords(job_text)

    missing = job_words - resume_words
    return list(missing)[:20]
