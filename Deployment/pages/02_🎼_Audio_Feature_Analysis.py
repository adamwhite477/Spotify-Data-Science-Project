import streamlit as st
import pathlib
import platform
plt = platform.system()
if plt == 'Linux': 
    pathlib.WindowsPath = pathlib.PosixPath
    
st.set_page_config(page_title="Audio Feature Analysis", page_icon=":musical_score:")

st.write("Audio Feature Page Coming Soon...")