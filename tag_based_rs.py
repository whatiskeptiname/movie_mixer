import pickle
import streamlit as st
import requests


movies = pickle.load(open("pickles/movie_list.p", "rb"))
similarity = pickle.load(open("pickles/similarity.p", "rb"))

movie_list = [1, 2, 3]

selected_movie = st.selectbox("Select a Movie", movie_list)
