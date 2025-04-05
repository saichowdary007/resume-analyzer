import streamlit as st
import requests

st.set_page_config(page_title="Resume Analyzer", layout="centered")
st.title("🧠 AI-Powered Resume Analyzer")

st.markdown("Upload your resume (PDF) and paste a job description to get a match score and skill insights.")

# Upload
resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_text = st.text_area("Paste Job Description Here")

if st.button("Analyze") and resume_file and job_text:
    with st.spinner("Analyzing..."):
        response = requests.post(
            "http://localhost:8000/analyze-file",
            files={"resume": resume_file},
            data={"job_text": job_text}
        )

        if response.status_code == 200:
            result = response.json()
            st.success(f"✅ Match Score: {result['match_score']}%")

            st.subheader("❌ Missing Skills")
            if result["missing_skills"]:
                for skill in result["missing_skills"]:
                    st.markdown(f"- {skill}")
            else:
                st.markdown("_No missing skills detected!_")

            with st.expander("📄 Resume Text Preview"):
                st.code(result["resume_text"])
        else:
            st.error("Something went wrong during analysis.")