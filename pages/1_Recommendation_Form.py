import streamlit as st
from recommender_utils import Recommendations

st.title("📋 Recommendation Form")

with st.form("recommendation_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    part_time_job = st.radio("Part-Time Job", ["Yes", "No"]) == "Yes"
    absence_days = st.number_input("Absence Days", min_value=0, step=1)
    extracurricular = st.radio("Extracurricular Activities", ["Yes", "No"]) == "Yes"
    weekly_self_study_hours = st.number_input("Weekly Self-Study Hours", min_value=0, step=1)

    subjects = {}
    for subject in ['Math', 'History', 'Physics', 'Chemistry', 'Biology', 'English', 'Geography']:
        subjects[subject] = st.number_input(f"{subject} Score", min_value=0, step=1)

    total_score = sum(subjects.values())
    average_score = total_score / len(subjects)

    st.write(f"**Total Score:** {total_score}")
    st.write(f"**Average Score:** {average_score:.2f}")

    submitted = st.form_submit_button("Get Recommendation")

if submitted:
    recommendations = Recommendations(
        gender, part_time_job, absence_days, extracurricular,
        weekly_self_study_hours,
        subjects['Math'], subjects['History'], subjects['Physics'], subjects['Chemistry'],
        subjects['Biology'], subjects['English'], subjects['Geography'],
        total_score, average_score
    )

    st.subheader("🎯 Top Career Recommendations")
    for idx, (career, prob) in enumerate(recommendations, 1):
        st.write(f"{idx}. **{career}** — Probability: {prob:.2%}")
