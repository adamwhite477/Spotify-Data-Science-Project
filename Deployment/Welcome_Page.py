import streamlit as st
from PIL import Image

st.set_page_config(page_title="Spotify Data Science Project", page_icon=":musical_note:")
st.title("Welcome Page!")
st.write("This web app is used to display what I've learned and different analytical techniques I have used with the data provided using the Spotify API!")

img = Image.open("spotify_logo.png")
st.image(img)
img2 = Image.open("path/Pictures/dataloaders.png")
st.image(img2)