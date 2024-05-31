import streamlit as st
#import joblib
from pathlib import Path
from PIL import Image
import requests
import json


st.set_page_config(
        page_title="Your Insurance Partner",
        page_icon="insurance_page_icon.png"
    )

image = Image.open('main_image_insurance.jpeg')
st.image(image, caption='Insurance is our Job', width=300)
st.markdown("<h1 style='text-align: right; color: red;'main_image_insurance.jpeg", unsafe_allow_html=True)


st.markdown("**Please fill the below form :**")
with st.form(key="Form :", clear_on_submit = True):
    Name = st.text_input("Name : ")
    Email = st.text_input("Email ID : ")
    File = st.file_uploader(label = "Upload file", type=["pdf","docx"])
    Submit = st.form_submit_button(label='Submit')
    

st.subheader("Details : ")
st.metric(label = "Name :", value = Name)
st.metric(label = "Email ID :", value = Email)

if Submit :
    st.markdown("**The file is sucessfully Uploaded.**")

    # Save uploaded file to 'F:/tmp' folder.
    save_folder = 'F:/tmp'
    save_path = Path(save_folder, File.name)
    with open(save_path, mode='wb') as w:
        w.write(File.getvalue())

    if save_path.exists():
        st.success(f'File {File.name} is successfully saved!')


