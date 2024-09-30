import streamlit as st
import matplotlib.pyplot as plt

def summary():
    with st.container():
        st.header("Overall Sentiments Summary")

        df = st.session_state.data

        positive_count = df.loc[df.sentiment == "POSITIVE", "sentiment"].count()
        negative_count = df.loc[df.sentiment == "NEGATIVE", "sentiment"].count()

        sentiment_counts = [positive_count, negative_count]
        sentiment_labels = ["Positive", "Negative"]

        pie_fig, pie_ax = plt.subplots()
        pie_ax.pie(sentiment_counts, labels=sentiment_labels, colors=["green", "red"], autopct='%1.1f%%', startangle=90)
        pie_ax.axis('equal')

        col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
        with col2.container(border=True):
            st.pyplot(pie_fig)


        st.subheader("Sentiment Comparison: Classic vs. Recent Movies")
        st.markdown(
            """
            This section compares sentiment distribution between 10 classic movies and 10 recently released movies (2022-2023).
            The goal is to analyze if there are any notable differences in viewer sentiment between these two groups.
            """
        )

        recent_movies = df[df['release_year'] >= 2022]
        classic_movies = df[df['release_year'] < 2022]

        recent_positive_count = recent_movies.loc[recent_movies.sentiment == "POSITIVE", "sentiment"].count()
        recent_negative_count = recent_movies.loc[recent_movies.sentiment == "NEGATIVE", "sentiment"].count()

        classic_positive_count = classic_movies.loc[classic_movies.sentiment == "POSITIVE", "sentiment"].count()
        classic_negative_count = classic_movies.loc[classic_movies.sentiment == "NEGATIVE", "sentiment"].count()

        categories = ["Classic Movies", "Recent Movies"]
        positive_counts = [classic_positive_count, recent_positive_count]
        negative_counts = [classic_negative_count, recent_negative_count]

        bar_fig, bar_ax = plt.subplots()
        bar_ax.bar(categories, positive_counts, label="Positive", color="green", width=0.4)
        bar_ax.bar(categories, negative_counts, bottom=positive_counts, label="Negative", color="red", width=0.4)

        bar_ax.set_ylabel("Number of Reviews")
        bar_ax.set_title("Sentiment Comparison: Classic vs. Recent Movies")
        bar_ax.legend()

        col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
        with col2.container(border=True):
            st.pyplot(bar_fig)