# 💼 AI Resume Analyzer

An AI-powered Resume Analyzer that compares resumes with job descriptions to evaluate candidate-job fit using semantic similarity and keyword analysis.

The system uses sentence embeddings and cosine similarity to calculate a match score, identify missing skills, and provide improvement suggestions.

---

## 🚀 Features

- Upload resume in PDF format
- Paste job descriptions for comparison
- Match score calculation using embeddings
- Missing skills and keyword gap detection
- Resume improvement suggestions
- Interactive Streamlit interface
- Windows-compatible and API-free

---

## 🧠 How It Works

1. Resume Parsing
   - Extracts text from uploaded PDF resumes

2. Text Cleaning
   - Normalizes and preprocesses text

3. Embedding Generation
   - Converts resume and job description into vector embeddings

4. Similarity Scoring
   - Uses cosine similarity to compute match percentage

5. Skill Gap Detection
   - Identifies keywords missing from the resume

---

## 🛠 Tech Stack

- Python
- Streamlit
- Sentence Transformers
- Scikit-learn
- PyPDF

---

## 📂 Project Structure

ai-resume-analyzer/
│
├── app.py
├── analyzer.py
├── text_utils.py
├── requirements.txt
├── .gitignore
└── README.md

---

## ▶️ How to Run

1. Clone the repository
   git clone https://github.com/SciddhantoSinha/ai-resume-analyzer.git

2. Navigate to the project folder
   cd ai-resume-analyzer

3. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

4. Install dependencies
   pip install -r requirements.txt

5. Run the app
   python -m streamlit run app.py

---

## 💡 Example Use Case

Upload your resume and paste a job description from LinkedIn or Indeed to see:

- Match score (%)
- Missing keywords
- Suggestions for improvement

---

## 📌 Future Enhancements

- Skill categorization (technical vs soft skills)
- Job role recommendation system
- Resume rewriting suggestions
- Support for DOCX files
- Dashboard analytics

---
