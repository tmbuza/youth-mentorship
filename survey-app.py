import streamlit as st
import pandas as pd
import os

# Set the title
st.title("Future Workforce Preparation Survey")

# Collect demographic information
st.header("Demographic Information")
age = st.selectbox("Age Group:", ["Under 18", "18-25", "26-35", "36-45", "46-55", "56 and above"])
gender = st.selectbox("Gender:", ["Male", "Female", "Other", "Prefer not to say"])
education = st.selectbox("Education Level:", ["Form 4", "Form 6"])

# Collect information about future plans
st.header("Future Plans")
occupation = st.radio("What do you plan to do after school?", ["Go to college", "Look for a job", "Start a business", "Self-employed", "Other"])
courses_interested = st.multiselect("What courses are you interested in?", ["Business", "Engineering", "Arts", "Science", "Technology", "Other (please specify)"])
other_course = ""
if "Other (please specify)" in courses_interested:
    other_course = st.text_input("Please specify the other course:")

# Knowledge about remote work
st.header("Knowledge about Remote Work")
remote_work = st.radio("Are you aware of remote work opportunities?", ["Yes", "No"])
skills_needed = st.multiselect("What skills do you think are needed for remote work?", ["Coding", "Digital Marketing", "Graphic Design", "Writing", "Data Analysis", "Other (please specify)"])
other_skill = ""
if "Other (please specify)" in skills_needed:
    other_skill = st.text_input("Please specify the other skill:")

# Collect additional comments
st.header("Additional Comments")
additional_comments = st.text_area("Please share any additional comments or thoughts:")

# Submit the survey
if st.button("Submit"):
    # Prepare data to be saved
    survey_data = {
        "Age": age,
        "Gender": gender,
        "Education": education,
        "Occupation": occupation,
        "Courses Interested": ", ".join(courses_interested),
        "Other Course": other_course if "Other (please specify)" in courses_interested else "",
        "Remote Work Awareness": remote_work,
        "Skills Needed": ", ".join(skills_needed),
        "Other Skill": other_skill if "Other (please specify)" in skills_needed else "",
        "Additional Comments": additional_comments
    }
    
    # Convert to DataFrame
    survey_df = pd.DataFrame([survey_data])
    
    # File path for saving the survey responses in the current working directory
    file_path = os.path.join(os.getcwd(), "survey_responses.csv")
    
    # Check if file exists to avoid file not found error when reading header
    file_exists = os.path.isfile(file_path)
    
    # Save to CSV
    if file_exists:
        survey_df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        survey_df.to_csv(file_path, mode='w', header=True, index=False)
    
    st.success("Thank you for your response!")

# Add a download button for the survey responses CSV file
if st.button("Download Responses"):
    with open(file_path, "rb") as file:
        btn = st.download_button(
            label="Download survey responses",
            data=file,
            file_name="survey_responses.csv",
            mime="text/csv"
        )
