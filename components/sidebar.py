import streamlit as st

def sidebar():
    with st.sidebar:
        if st.button("Home", use_container_width=True, type="primary" if st.session_state.page == "Home" else "secondary"):
            st.session_state.page = "home"
            st.switch_page("main.py")
        if st.button("Movies Sentiments", use_container_width=True, type="primary" if st.session_state.page == "Movies Sentiments" else "secondary"):
            st.session_state.page = "sentiments"
            st.switch_page("pages/sentiments.py")