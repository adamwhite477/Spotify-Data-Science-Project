import streamlit as st
from PIL import Image
import pathlib
from fastai.vision.all import load_learner
import platform


st.set_page_config(page_title="Spotify Data Science Project", page_icon=":musical_note:")
st.title("Spotify Data Science Project!")
st.write("**Created By:** Adam White")
st.write("**Github Repo [HERE](https://github.com/adamwhite477/Spotify-Data-Science-Project)**")
st.write("This web app is used to display what I've learned and different analytical techniques I have used with the data provided using the Spotify API!")
st.write("Try out the model below!")


plt = platform.system()
if plt == 'Linux': 
    pathlib.WindowsPath = pathlib.PosixPath
model = load_learner("model3.pkl")

st.set_page_config(page_title="Genre Predictor", page_icon=":microphone:")

# ---- HEADER -----
with st.container():
    # st.subheader("Hello Test")
    st.title("Test out my model!")
    st.write("This a model that tries to predict the genre of the image it is given")
    st.write("Genres it tries to determine: [Rap, Country, Rock]")
    uploaded_img = st.file_uploader("Upload Image Here", type=["jpg", "png", "jfif", "webp", "jpeg"], accept_multiple_files=False)

if uploaded_img is not None:
    img = Image.open(uploaded_img)
    st.image(img)
    genre,_,probs = model.predict(img)
    with st.container():
        st.write("This is a {} album".format(genre))
        st.write("It has a confidence of {:.4f}".format(probs[0]))