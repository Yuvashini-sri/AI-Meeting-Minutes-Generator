# meeting-minutes-generator/app.py
import streamlit as st
from summarizer import summarize_text
from pdf_generator import save_to_pdf
from email_service import send_email
import os

st.title("\U0001F4BE AI-Powered Meeting Minutes Generator")

input_text = st.text_area("Paste your meeting transcript below:", height=300)

if st.button("Generate Summary"):
    with st.spinner("Generating summary..."):
        summary = summarize_text(input_text)
        st.markdown("### 📝 Meeting Summary")
        st.text(summary)
        st.session_state["summary"] = summary

if "summary" in st.session_state:
    if st.button("📄 Export to PDF"):
        save_to_pdf(st.session_state["summary"])
        st.success("PDF generated successfully as meeting_summary.pdf")

    user_email = st.text_input("📧 Enter recipient email to send summary:")
    if st.button("📤 Send Email"):
        if user_email:
            send_email("Meeting Summary", st.session_state["summary"], user_email)
            st.success(f"Email sent to {user_email}")
        else:
            st.warning("Please enter a valid email address.")
