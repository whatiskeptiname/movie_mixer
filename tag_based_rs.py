import pickle
import numpy as np
import streamlit as st
import requests

final_movies = pickle.load(open("pickles/movie_list.p", "rb"))
similarity = pickle.load(open("pickles/similarity.p", "rb"))
final_movies_titles = final_movies["title"]


def recommend(movie):
    index = final_movies[final_movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]
    )
    recommended = []
    for i in distances[1:6]:
        recommended.append(final_movies.iloc[i[0]]["title"])
    return recommended


# Streamlit Design
st.header("Movie Mixer")
selected_movie = st.selectbox("Select a file", final_movies_titles)

recommend_movies = recommend(selected_movie)

for i in recommend_movies:
    st.text(i)
