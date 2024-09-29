import streamlit as st

def movies_list():
    with st.container():
        st.header("Movies List")

        df = st.session_state.data

        unique_movies = df[['movie_title', 'release_year']].drop_duplicates()
        recent_movies = unique_movies[unique_movies['release_year'] >= 2022]
        classic_movies = unique_movies[unique_movies['release_year'] < 2022]

        st.subheader("Recent Movies (2022-2023)")
        st.dataframe(
            recent_movies,
            use_container_width=True,
            hide_index=True,
            column_config={
                "movie_title": "Movie Title",
                "release_year": st.column_config.TextColumn(
                    "Release Year"
                )
            }
        )

        st.subheader("Classic Movies (Before 2000)")
        st.dataframe(
            classic_movies,
            use_container_width=True,
            hide_index=True,
            column_config={
                "movie_title": "Movie Title",
                "release_year": st.column_config.TextColumn(
                    "Release Year"
                )
            }
        )
