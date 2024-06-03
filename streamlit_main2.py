import streamlit as st
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
<p style="text-align: center; font-family: Arial, sans-serif; font-size: 14px; color: blue; font-weight: bold;">
           Your Best Insurance AI-Partner
</p>
"""

left_co, cent_co,last_co = st.columns(3)
image = Image.open('main_image_insurance.jpeg')
with cent_co:
    st.image(image, width=250)

st.markdown(styled_caption, unsafe_allow_html=True)

st.markdown("**Please fill the below blanks and upload your documents to be anaylzed :**")
with st.form(key="Form :", clear_on_submit = True):
    Name = st.text_input("Name and Surname : ")
    Email = st.text_input("Email : ")
    Files = st.file_uploader(label = "Upload file", type=["pdf", "png","jpeg"], accept_multiple_files=True)
    Submit = st.form_submit_button(label='Submit')
    

st.markdown("**Extracted Information based on your Entry :** ")

if Files is not None and len(Files) >0:
   # st.markdown("**The file is sucessfully Uploaded.**")
   # Save the uploaded file
    save_folder = '/Users/kaan/Desktop/insurance_app/temp' #add a directory or path to save the uploaded documents
    for uploaded_file in Files:
            save_path = os.path.join(save_folder, uploaded_file.name)
            try:
                with open(save_path, 'wb') as f:
                    f.write(uploaded_file.getbuffer())
                st.success(f"File saved at {save_path}")
            except Exception as e:
                st.error(f"Error saving file: {e}")
