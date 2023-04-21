import streamlit as st
import pathlib
import platform
plt = platform.system()
if plt == 'Linux': 
    pathlib.WindowsPath = pathlib.PosixPath
    
st.set_page_config(page_title="Song Reccomender", page_icon=":guitar:")

st.write("Song Recommender Page Coming Soon...")