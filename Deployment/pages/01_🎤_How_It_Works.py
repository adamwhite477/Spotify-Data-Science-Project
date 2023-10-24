import streamlit as st
from fastai.vision.all import load_learner
from PIL import Image
import pathlib


st.set_page_config(page_title="How It Works!", page_icon=":microphone:")

# ---- HEADER -----
with st.container():
    # st.subheader("Hello Test")
    st.title("Process of Creating this Model!")


st.subheader("How it works!")

search_img = Image.open("Pictures/search.png")
download_img = Image.open("Pictures/download_images.png")
dataloaders_img = Image.open("Pictures/dataloaders.png")
export_model_img = Image.open("Pictures/export_model1.png")
load_data_img = Image.open("Pictures/load_data.png")
train_model_img = Image.open("Pictures/train_model.png")
verify_images_img = Image.open("Pictures/verify_images.png")
distribution_img = Image.open("Pictures/distribution.png")

st.write("First, we must search for our Genre pictures so we can download them to train on!")

st.image(search_img)

st.write("Then, we will check on the distribution of each class label")
st.write("**Note:** This picture is taken from my first model test, it is recommended to have evenly distributed class labels for better results")

st.image(distribution_img)

st.write("Then, we must download all of the images locally into a folder called 'album_imgs'")
st.write("All of the class labels will have their own folder, this will help us in the future when we are creating our model")

st.image(download_img)

st.write("Then, we must verify all of the images downloaded correctly (I personally have not had any issues but it is a good idea to do so anyways)")

st.image(verify_images_img)

st.write("Next, we will load our images into a FastAI 'DataLoader'")

st.image(load_data_img)

st.write("Next, we will check out a batch of our data to make sure it looks correct!")

st.image(dataloaders_img)

st.write("Now that we have our Dataloader, we can use it to train our FastAI model 'vision_learner'")
st.write("**Note:** This picture was taken using my first model, I recommend changing the 'metrics' to 'accuracy' instead of 'error_rate' as it has given me a slight increase in performance")
st.image(train_model_img)

st.write("Now that we have our model, we can export it!")

st.image(export_model_img)