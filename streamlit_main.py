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
image = Image.open('main_image_insurance.jpeg')
st.image(image, width=700)
st.markdown(styled_caption, unsafe_allow_html=True)
#st.markdown("<h1 style='text-align: center; font-family: Arial, sans-serif; font-size: 20px; color: blue;font-weight: bold;'main_image_insurance.jpeg", unsafe_allow_html=True)

st.markdown("**Please fill the below form :**")
with st.form(key="Form :", clear_on_submit = True):
    Name = st.text_input("Name and Surname : ")
    Email = st.text_input("Email : ")
    File = st.file_uploader(label = "Upload file", type=["pdf", "png","jpeg"])
    Submit = st.form_submit_button(label='Submit')
    

st.subheader("**Extracted Information based on your Entry :** ")
#st.metric(label = "Name :", value = Name)
#st.metric(label = "Email ID :", value = Email)

if Submit :
    st.markdown("**The file is sucessfully Uploaded.**")

    # Save uploaded file to 'F:/tmp' folder.
    save_folder = 'F:/tmp'
    save_path = Path(save_folder, File.name)
    with open(save_path, mode='wb') as w:
        w.write(File.getvalue())

    if save_path.exists():
        st.success(f'File {File.name} is successfully saved!')


