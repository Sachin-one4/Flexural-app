import streamlit as st

def main():
    st.title("👨‍💻 About the Team")
    st.markdown("Meet the developers behind this final-year BTech project.")

    team = [
        {
            "name": "Sachin",
            "roll": "23001020505",
            "role": "Frontend & Data Preprocessing",
            "image": "self.jpg"
        },
        {
            "name": "Naman",
            "roll": "23001020504",
            "role": "Model Training & Evaluation",
            "image": "naman.jpg"
        },
        {
            "name": "Mohd Saif Ali",
            "roll": "23001020503",
            "role": "Report Writing & Deployment",
            "image": "naman.jpg"
        }
    ]

    cols = st.columns(3)
    for i, member in enumerate(team):
        with cols[i]:
            st.image(member["image"], width=150)
            st.markdown(f"### {member['name']}")
            st.markdown(f"**Roll No:** {member['roll']}")
            st.markdown(f"**Role:** {member['role']}")
