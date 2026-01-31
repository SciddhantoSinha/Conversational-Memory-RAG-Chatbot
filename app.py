import streamlit as st
from text_utils import extract_text_from_pdf
from analyzer import get_match_score, missing_skills, clean_text

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("💼 AI Resume Analyzer & Job Matcher")

st.write("Upload your resume and compare it with a job description.")

resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_desc = st.text_area("Paste Job Description")

if resume_file and job_desc:
    with st.spinner("Analyzing..."):

        resume_text = extract_text_from_pdf(resume_file)
        job_text = clean_text(job_desc)

        score = get_match_score(resume_text, job_text)
        gaps = missing_skills(resume_text, job_text)

    st.subheader("📊 Match Score")
    st.success(f"{score}% match with job description")

    if score > 75:
        st.info("✅ Strong match! You are a good fit.")
    elif score > 50:
        st.warning("⚡ Moderate match. Improve with more skills.")
    else:
        st.error("❌ Low match. Consider updating your resume.")

    st.subheader("🔍 Missing Keywords / Skills")
    st.write(", ".join(gaps))

    st.subheader("💡 Suggestions")
    st.write("""
    - Add missing technical skills
    - Include relevant projects
    - Use keywords from job description
    - Quantify your achievements
    """)
