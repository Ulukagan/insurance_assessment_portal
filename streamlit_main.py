import streamlit as st
#import joblib
from pathlib import Path
from PIL import Image
import requests
import json
import os


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

st.markdown("**Please fill the below blanks and upload your documents to be anaylzed :**")
with st.form(key="Form :", clear_on_submit = True):
    Name = st.text_input("Name and Surname : ")
    Email = st.text_input("Email : ")
    File = st.file_uploader(label = "Upload file", type=["pdf", "png","jpeg"], accept_multiple_files=True)
    Submit = st.form_submit_button(label='Submit')
    

st.markdown("**Extracted Information based on your Entry :** ")

if File is not None:
   # st.markdown("**The file is sucessfully Uploaded.**")
        # Save the uploaded file
    save_folder = '/Users/kaan/Desktop/insurance_app/temp'
    save_path = os.path.join(save_folder, File.name)
    try:
        with open(save_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"File saved at {save_path}")
    except Exception as e:
        st.error(f"Error saving file: {e}")

    # Save uploaded file to '/Users/kaan/Desktop/insurance_app/temp' folder.
    #save_folder = '/Users/kaan/Desktop/insurance_app/temp'
    #save_path = Path(save_folder, File.name)
    #with open(save_folder, mode='wb') as w:
        #   w.write(File.getvalue())


    #if save_path.exists():
     #   st.success(f'File {File.name} is successfully saved!')

