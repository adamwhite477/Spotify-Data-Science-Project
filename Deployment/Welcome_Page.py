import streamlit as st
from PIL import Image
import pathlib
from fastai.vision.all import load_learner
import platform


st.set_page_config(page_title="Spotify Data Science Project", page_icon=":musical_note:")
st.title(":green[Spotify Data Science Project!]")
st.write("**Created By:** Adam White")
st.write("**Github Repo [HERE](https://github.com/adamwhite477/Spotify-Data-Science-Project)**")
description_text = '''
                This is the deployed web app of the deep learning model I created using fastAI! This model attempts    
                to predict the Genre of the user-generated image based on album cover data extracted directly from   
                the Spotify API. So far, the model can only predict 3 different genres (Rap, Country, Rock), however     
                I am currently working on another model that will attempt to expand the amount of genre titles without   
                sacrificing accuracy. This was my first time using an API and creating a Deep Learning model so it is   
                admittedly a bit basic, but it has given me a good foundation on progressing my knowledge in these areas   
                tremendously!  
                
'''
st.markdown(description_text)
st.write("Try it out below!")


plt = platform.system()
if plt == 'Linux': 
    pathlib.WindowsPath = pathlib.PosixPath
model = load_learner("model3.pkl")

# ---- HEADER -----
with st.container():
    # st.subheader("Hello Test")
    st.title("Test out my model!")
    uploaded_img = st.file_uploader("Upload Image Here", type=["jpg", "png", "jfif", "webp", "jpeg"], accept_multiple_files=False)

if uploaded_img is not None:
    img = Image.open(uploaded_img)
    st.image(img)
    genre,_,probs = model.predict(img)
    with st.container():
        if genre == "country":
            st.write("This model predicts that based on this image, this is a :orange[Country] album cover! Yee-haw! 🤠")
        elif genre == "rap":
            st.write("This model predicts that based on this image, this is a :red[Rap] album cover! That's Fire :fire:")
        elif genre == "rock":
            st.write("This model predicts that based on this image, this is a :green[Rock] album cover! Rock On 🤘")
        else:
            st.write("Error, predicted genre is {}?", genre)

spotify_img = Image.open("Pictures/spotify_logo.png")
st.image(spotify_img)