import streamlit as st

def main():
    st.title("📬 Contact Us")
    st.markdown("We'd love to hear your feedback or answer any questions!")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send Message")

        if submit:
            st.success("✅ Message sent! Thank you.")
