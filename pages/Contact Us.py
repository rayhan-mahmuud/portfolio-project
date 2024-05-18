import streamlit as st
from send_email import send_email

st.title("Contact Me")

with st.form(key="email_form"):

    user_email = st.text_input("Enter you email here:")
    user_massage = st.text_area("Your Message:")
    submit_btn = st.form_submit_button("Submit")

    mail_to_send = f"""Subject: Portfolio Web App: New Email From {user_email.split("@")[0]}

    From: {user_email}

    {user_massage}"""

    if submit_btn:
        send_email(mail_to_send)
        st.info("Your message sent successfully. Thank you for contacting!")

