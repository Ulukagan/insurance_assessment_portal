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

# Custom styled caption using HTML
styled_caption = """
<p style="text-align: center; font-family: Arial, sans-serif; font-size: 20px; color: blue; font-weight: bold;">
    Insurance is our Job
</p>
"""
# HTML/CSS to center the image
centered_image_html = f"""
<div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
    <img src="data:image/jpeg;base64,{img_str}" width="600" style="margin-bottom: 20px;">
</div>
"""
image = Image.open('main_image_insurance.jpeg')
st.image(centered_image_html, width=600)
st.markdown(styled_caption, unsafe_allow_html=True)
#st.markdown("<h1 style='text-align: center; font-family: Arial, sans-serif; font-size: 20px; color: blue;font-weight: bold;'main_image_insurance.jpeg", unsafe_allow_html=True)


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


