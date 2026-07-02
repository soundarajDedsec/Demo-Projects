import streamlit as st
from app import sample

st.set_page_config(page_title="Login Page", page_icon="🔐", layout="wide")

USERNAME = "Sounder"
PASSWORD = "1234"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in == False:
    st.title("Login🛡️")
    username = st.text_input("Username:👤")
    password = st.text_input("Password:🔑", type="password")

    if st.button("Login"):
        username = username.strip()
        password = password.strip()
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid Username or Password")
else:
    sample()
    st.set_page_config(page_title="Candidate Dashboard",page_icon="🤖", layout="wide")