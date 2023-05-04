import streamlit as st
from fastai.vision.all import load_learner
from PIL import Image
import pathlib
import platform
plt = platform.system()
if plt == 'Linux': 
    pathlib.WindowsPath = pathlib.PosixPath
model = load_learner("model2.pkl")

st.set_page_config(page_title="Genre Predictor", page_icon=":microphone:")

# ---- HEADER -----
with st.container():
    # st.subheader("Hello Test")
    st.title("Test out my model!")
    st.write("This a model that tries to predict the genre of the image it is given")
    st.write("Genres it tries to determine: [Rap, Country, Rock]")
    uploaded_img = st.file_uploader("Upload Image Here", type="jpg", accept_multiple_files=False)

if uploaded_img is not None:
    img = Image.open(uploaded_img)
    st.image(img)
    genre,_,probs = model.predict(img)
    with st.container():
        st.write("This is a {} album".format(genre))
        st.write("It has a confidence of {:.4f}".format(probs[0]))


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
