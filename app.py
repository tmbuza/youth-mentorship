import streamlit as st

st.title("Future Workforce Preparation Survey")

# Demographic Information
st.header("Demographic Information")
age = st.selectbox("1. Age:", ["Under 18", "18-25", "26-35", "36-45", "46-55", "56 and above"])
gender = st.radio("2. Gender:", ["Male", "Female", "Other", "Prefer not to say"])
education = st.radio("3. Education Level:", ["No formal education", "Primary education", "Secondary education", "Higher education (college/university)"])
occupation = st.radio("4. Occupation:", ["Student", "Employed", "Unemployed", "Self-employed", "Other (please specify)"])

# Future Preparation
st.header("Future Preparation")
future_plan = st.radio("5. What are your future plans?", ["College/University", "Employment", "Business", "Self-employed", "Other (please specify)"])
courses_interested = st.text_area("6. What courses or skills are you interested in?")
remote_work_awareness = st.radio("7. Are you aware of remote work opportunities?", ["Yes", "No"])
skills_for_remote_work = st.text_area("8. What skills do you think you need for remote work?")

# Additional Information
st.header("Additional Information")
challenges_faced = st.text_area("9. What challenges do you face in preparing for your future?")
suggestions = st.text_area("10. Any suggestions for improving future workforce preparation?")

# Submit
if st.button("Submit"):
    data = {
        "Age": age,
        "Gender": gender,
        "Education": education,
        "Occupation": occupation,
        "Future Plans": future_plan,
        "Courses Interested": courses_interested,
        "Remote Work Awareness": remote_work_awareness,
        "Skills for Remote Work": skills_for_remote_work,
        "Challenges Faced": challenges_faced,
        "Suggestions": suggestions
    }
    st.write("Survey Submitted! Thank you for your responses.")
    st.json(data)
