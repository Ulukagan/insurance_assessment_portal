import streamlit as st
from pathlib import Path
from PIL import Image
import requests
import json
import os
from google.cloud import storage
from io import BytesIO
import tempfile


GCS_BUCKET_NAME = 'bucket_kaan'
GCS_CREDENTIALS = 'happtiq-kboelek-demo-play-a4c7c4c61f90.json'

def upload_to_gcs(bucket_name, file_obj, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client.from_service_account_json(GCS_CREDENTIALS)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(file_obj)
    return f'gs://{bucket_name}/{destination_blob_name}'

st.set_page_config(
        page_title="Your Insurance Partner",
        page_icon="insurance_page_icon.png"
    )

# Custom styled caption using HTML
styled_caption = """
<p style="text-align: center; font-family: Arial, sans-serif; font-size: 13px; color: blue; font-weight: bold;">
    Your Best Insurance AI-Partner
</p>
"""
left_co, cent_co,last_co = st.columns(3)
image = Image.open('main_image_insurance.jpeg')
with cent_co:
    st.image(image, width=250)
st.markdown(styled_caption, unsafe_allow_html=True)
#st.markdown("<h1 style='text-align: center; font-family: Arial, sans-serif; font-size: 20px; color: blue;font-weight: bold;'main_image_insurance.jpeg", unsafe_allow_html=True)

st.markdown("**Please fill the below blanks and upload your documents to be anaylzed :**")
with st.form(key="Form :", clear_on_submit = True):
    Name = st.text_input("Name and Surname : ")
    Email = st.text_input("Email : ")
    Files = st.file_uploader(label = "Upload file", type=["pdf", "png","jpeg"], accept_multiple_files=True)
    Submit = st.form_submit_button(label='Submit')
    

st.markdown("**Extracted Information based on your Entry :** ")

if Files is not None and len(Files) >0:    
    bucket_name = 'bucket_kaan'                            
    for uploaded_file in Files:
        # Save file content to a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_file_path = temp_file.name
        # save_folder = '/Users/kaan/Desktop/insurance_app/temp'
        # save_path = os.path.join(save_folder, uploaded_file.name)
        # try:
        #     with open(save_path, 'wb') as f:
        #         f.write(uploaded_file.getbuffer())
        #     st.success(f"File saved at {save_path}")
        # except Exception as e:
        #     st.error(f"Error saving file: {e}")
     # Upload to Google Cloud Storage

        # Read file content into a BytesIO object
        #file_content = BytesIO(uploaded_file.getvalue())
        
        destination_blob_name = uploaded_file.name
        # Upload the file to GCS
        try:
            gcs_url = upload_to_gcs(GCS_BUCKET_NAME, temp_file_path,destination_blob_name)
            st.success(f"File uploaded to {gcs_url}")
        except Exception as e:
            st.error(f"Error uploading file to GCS: {e}")
        finally:
            #remove temporary file
            os.unlink(temp_file_path)
