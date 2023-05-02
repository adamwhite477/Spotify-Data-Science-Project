import streamlit as st
from PIL import Image

st.set_page_config(page_title="Spotify Data Science Project", page_icon=":musical_note:")
st.title("Welcome Page!")
st.write("This web app is used to display what I've learned and different analytical techniques I have used with the data provided using the Spotify API!")

img = Image.open("Pictures/spotify_logo.png")
st.image(img)

st.subheader("How it works!")

search_img = Image.open("Pictures/search.png")
download_img = Image.open("Pictures/download_images.png")
dataloaders_img = Image.open("Pictures/dataloaders.png")
export_model_img = Image.open("Pictures/export_model.png")
load_data_img = Image.open("Pictures/load_data.png")
train_model_img = Image.open("Pictures/train_model.png")
verify_images_img = Image.open("Pictures/verify_images.png")
distribution_img = Image.open("Pictures/distribution.png")

st.write("First, we must search for our Genre pictures so we can download them to train on!")

st.image(search_img)