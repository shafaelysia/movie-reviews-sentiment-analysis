import streamlit as st
import pandas as pd
import re
from components.sidebar import sidebar
from components.overview import overview
from components.summary import summary
from components.movies_list import movies_list

def main():
    st.session_state.page = "Home"
    sidebar()

    st.title("Movie Reviews Sentiment Analysis Dashboard")

    overview()
    st.divider()

    movies_list()
    st.divider()

    summary()

def initialize_session():
    df = pd.read_csv("data-collection/sentiment_results.csv")
    df["review_text"] = [clean_dataset(review) for review in df['review_text']]

    df['release_year'] = df['movie_title'].apply(lambda x: int(re.search(r'\((\d{4})\)', x).group(1)))
    unique_movies = df[['movie_title', 'release_year']].drop_duplicates()

    session_defaults = {
        'page': None,
        'data': df,
        'movies_list': unique_movies,
        'selected_movie': None
    }

    for key, value in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def clean_dataset(review):
    review = re.sub(r'\d{1,3}(?:,\d{3})* out of \d{1,3}(?:,\d{3})* found this helpful\.? Was this review helpful\? Sign in to vote\.?', '', str(review))
    review = re.sub(r'Permalink', '', review)
    review = ' '.join(review.split())
    return review

if __name__ == "__main__":
    st.set_page_config(page_title="Home", page_icon=":material/movie:", layout="centered")
    initialize_session()
    main()