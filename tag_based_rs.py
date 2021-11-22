import pickle
import streamlit as st
import requests

final_movies = pickle.load(open("pickles/movie_list.p", "rb"))
similarity = pickle.load(open("pickles/similarity.p", "rb"))
final_movies_titles = final_movies["title"]


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id
    )
    data = requests.get(url)
    data = data.json()
    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = final_movies[final_movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]
    )
    recommended = []
    posters = []
    for i in distances[1:6]:
        recommended.append(
            final_movies.iloc[i[0]]["title"],
        )
        movie_id = final_movies.iloc[i[0]]["imdb_title_id"]
        posters.append(fetch_poster(movie_id))
    return recommended, posters


# Streamlit Design
st.header("Movie Mixer")
selected_movie = st.selectbox("Select a Movie", final_movies_titles)

recom_movies, posters = recommend(selected_movie)

col1, col2, col3, col4, col5 = st.columns(5)


with col1:
    st.image(posters[0])
    st.text(recom_movies[0])
with col2:
    st.image(posters[1])
    st.text(recom_movies[1])
with col3:
    st.image(posters[2])
    st.text(recom_movies[2])
with col4:
    st.image(posters[3])
    st.text(recom_movies[3])
with col5:
    st.image(posters[4])
    st.text(recom_movies[4])
