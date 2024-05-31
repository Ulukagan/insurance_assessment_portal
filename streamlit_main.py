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

# HTML/CSS to center content
center_content = """
<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh;">
    <img src="main_image_insurance.jpeg" alt="Main Image" style="margin-bottom: 20px;">
    <h1 style="text-align: center; color: red;">
        This is a centered header with red text
    </h1>
    <p style="text-align: center; font-family: Arial, sans-serif; font-size: 20px; color: blue; font-weight: bold;">
        This is a centered paragraph with blue text, Arial font, size 20px, and bold formatting.
    </p>
</div>
"""

# Embed the HTML in the Streamlit app
st.markdown(center_content, unsafe_allow_html=True)


image = Image.open('main_image_insurance.jpeg')
st.image(image, caption='Insurance is our Job', width=600)
st.markdown("<h1 style='text-align: center; font-family: Arial, sans-serif; font-size: 20px; color: blue;font-weight: bold;'main_image_insurance.jpeg", unsafe_allow_html=True)


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


