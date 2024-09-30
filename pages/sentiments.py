import streamlit as st
import matplotlib.pyplot as plt
from main import initialize_session
from components.sidebar import sidebar
from components.visualization import plot_pie_chart, plot_sentiment_by_rating

def main():
    st.session_state.page = "Movies Sentiments"
    sidebar()

    st.title("Movies Sentiments")

    df = st.session_state.data

    movies_list = st.session_state.movies_list["movie_title"]
    selected = st.selectbox(
        "Choose a movie",
        (movies_list)
    )

    if selected:
        st.session_state.selected_movie = selected
        selected_movie = df.loc[df.movie_title == selected]

        columns_order = ["sentiment"] + [col for col in selected_movie.columns if col != "sentiment"]
        selected_movie = selected_movie[columns_order]
        selected_movie = selected_movie.drop(["user", "movie_title", "release_year"], axis=1)

        def highlight_sentiment(val):
            color = 'red' if val == "NEGATIVE" else 'green'
            return f'background-color: {color}'

        styled_movie = selected_movie.style.map(highlight_sentiment, subset=['sentiment'])

        st.dataframe(
            styled_movie,
            use_container_width=True,
            hide_index=True,
            column_config={
                "title": "Review Title",
                "review_text": "Review Content",
                "rating": "Rating",
                "date": "Review Date",
                "sentiment": "Sentiment"
            }
        )

        st.subheader("Positve vs Negative Sentiments Count Comparison")
        plot_pie_chart()

        st.subheader("Sentiment Distribution by Rating")
        plot_sentiment_by_rating()



if __name__ == "__main__":
    st.set_page_config(page_title="Movies Sentiments", page_icon=":material/movie:", layout="centered")
    initialize_session()
    main()