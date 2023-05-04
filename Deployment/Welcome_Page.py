import streamlit as st
from PIL import Image

st.set_page_config(page_title="Spotify Data Science Project", page_icon=":musical_note:")
st.title("Spotify Data Science Project!")
st.write("**Created By:** Adam White")
st.write("**Github Repo [HERE](https://github.com/adamwhite477/Spotify-Data-Science-Project)**")
st.write("This web app is used to display what I've learned and different analytical techniques I have used with the data provided using the Spotify API!")
st.write("Select a page on the left to check out some of the models I've created!")

img = Image.open("Pictures/spotify_logo.png")
st.image(img)