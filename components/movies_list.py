import streamlit as st

def movies_list():
    with st.container():
        st.header("Movies List")

        unique_movies = st.session_state.movies_list

        recent_movies = unique_movies[unique_movies['release_year'] >= 2022]
        classic_movies = unique_movies[unique_movies['release_year'] < 2022]

        st.subheader("Recent Movies (2022-2023)")
        st.dataframe(
            recent_movies["movie_title"],
            use_container_width=True,
            hide_index=True,
            column_config={
                "movie_title": "Movie Title",
            },
            selection_mode="single-row"
        )

        st.subheader("Classic Movies (Before 2000)")
        st.dataframe(
            classic_movies["movie_title"],
            use_container_width=True,
            hide_index=True,
            column_config={
                "movie_title": "Movie Title",
            }
        )
