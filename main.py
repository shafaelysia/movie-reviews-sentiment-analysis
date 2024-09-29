import streamlit as st
import pandas as pd
import re
from components.sidebar import sidebar
from components.overview import overview
from components.summary import summary
from components.movies_list import movies_list

def main():
    sidebar()

    st.title("Movie Reviews Sentiment Analysis Dashboard")

    overview()
    st.divider()

    movies_list()
    st.divider()

    summary()

def initialize_session():
    df = pd.read_csv("data-collection/sentiment_results.csv")
    df['release_year'] = df['movie_title'].apply(lambda x: int(re.search(r'\((\d{4})\)', x).group(1)))

    session_defaults = {
        'page': 'home',
        'data': df
    }

    for key, value in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

if __name__ == "__main__":
    st.set_page_config(page_title="Home", page_icon=":material/movie:", layout="centered")
    initialize_session()
    main()