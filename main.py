import streamlit as st

# Title
st.title("🌟 MBTI-based Job & Hobby Recommender")

# MBTI list
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI to job & hobby mapping
recommendations = {
    "INTJ": {
        "jobs": ["Scientist", "Engineer", "Strategic Planner"],
        "hobbies": ["Chess", "Coding", "Reading philosophy"]
    },
    "INTP": {
        "jobs": ["Data Analyst", "Philosopher", "Inventor"],
        "hobbies": ["Puzzles", "Blogging", "Learning languages"]
    },
    "ENTJ": {
        "jobs": ["Executive", "Lawyer", "Entrepreneur"],
        "hobbies": ["Debate", "Investing", "Public speaking"]
    },
    "ENTP": {
        "jobs": ["Startup Founder", "Consultant", "Marketer"],
        "hobbies": ["Improvisation", "Gaming", "Brainstorming ideas"]
    },
    "INFJ": {
        "jobs": ["Psychologist", "Counselor", "Writer"],
        "hobbies": ["Journaling", "Volunteering", "Poetry"]
    },
    "INFP": {
        "jobs": ["Artist", "Therapist", "Librarian"],
        "hobbies": ["Drawing", "Creative writing", "Nature walks"]
    },
    "ENFJ": {
        "jobs": ["Teacher", "Coach", "HR Manager"],
        "hobbies": ["Group activities", "Public speaking", "Drama"]
    },
    "ENFP": {
        "jobs": ["Creative Director", "Actor", "Motivational Speaker"],
        "hobbies": ["Traveling", "Storytelling", "Spontaneous adventures"]
    },
    "ISTJ": {
        "jobs": ["Accountant", "Administrator", "Inspector"],
        "hobbies": ["Collecting", "DIY projects", "Reading history"]
    },
    "ISFJ": {
        "jobs": ["Nurse", "Social Worker", "Librarian"],
        "hobbies": ["Cooking", "Gardening", "Scrapbooking"]
    },
    "ESTJ": {
        "jobs": ["Manager", "Military Officer", "Auditor"],
        "hobbies": ["Organizing", "Home improvement", "Volunteering"]
    },
    "ESFJ": {
        "jobs": ["Event Planner", "Teacher", "Healthcare Worker"],
        "hobbies": ["Hosting", "Dancing", "Crafting"]
    },
    "ISTP": {
        "jobs": ["Mechanic", "Pilot", "Forensic Analyst"],
        "hobbies": ["Fixing gadgets", "Adventure sports", "Gaming"]
    },
    "ISFP": {
        "jobs": ["Designer", "Chef", "Musician"],
        "hobbies": ["Painting", "Singing", "Exploring new food"]
    },
    "ESTP": {
        "jobs": ["Salesperson", "Paramedic", "Entrepreneur"],
        "hobbies": ["Sports", "Socializing", "Extreme sports"]
    },
    "ESFP": {
        "jobs": ["Performer", "Tour Guide", "Customer Service"],
        "hobbies": ["Acting", "Partying", "Fashion"]
    }
}

# Dropdown for MBTI selection
selected_mbti = st.selectbox("Choose your MBTI type:", mbti_types)

# Show recommendations
if selected_mbti:
    st.subheader(f"💼 Recommended Jobs for {selected_mbti}:")
    for job in recommendations[selected_mbti]["jobs"]:
        st.write(f"- {job}")

    st.subheader(f"🎨 Suggested Hobbies for {selected_mbti}:")
    for hobby in recommendations[selected_mbti]["hobbies"]:
        st.write(f"- {hobby}")
