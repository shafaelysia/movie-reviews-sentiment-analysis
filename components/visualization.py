import streamlit as st
import matplotlib.pyplot as plt

def plot_pie_chart():
    df = st.session_state.data
    selected= st.session_state.selected_movie
    selected_movie = df.loc[df.movie_title == selected]

    positive_count = selected_movie.loc[selected_movie.sentiment == "POSITIVE", "sentiment"].count()
    negative_count = selected_movie.loc[selected_movie.sentiment == "NEGATIVE", "sentiment"].count()

    sentiment_counts = [positive_count, negative_count]
    sentiment_labels = ["Positive", "Negative"]

    pie_fig, pie_ax = plt.subplots()
    pie_ax.pie(sentiment_counts, labels=sentiment_labels, colors=["green", "red"], autopct='%1.1f%%', startangle=90)
    pie_ax.axis('equal')

    col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
    with col2.container(border=True):
        st.pyplot(pie_fig)

def plot_sentiment_by_rating():
    df = st.session_state.data
    selected= st.session_state.selected_movie
    selected_movie = df.loc[df.movie_title == selected]

    selected_movie = selected_movie[selected_movie["rating"] != "No rating"]
    selected_movie['rating_value'] = selected_movie['rating'].apply(lambda x: int(x.split("/")[0]))
    sentiment_rating_df = selected_movie.groupby(['rating_value', 'sentiment']).size().unstack(fill_value=0)

    sentiment_rating_df.plot(kind='bar', stacked=False, color=["red", "green"], figsize=(10, 6))
    plt.title("Sentiment Distribution by Rating")
    plt.xlabel("Rating")
    plt.ylabel("Count of Reviews")
    plt.xticks(rotation=0)

    col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
    with col2.container(border=True):
        st.pyplot(plt)