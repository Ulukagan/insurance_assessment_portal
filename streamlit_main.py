import streamlit as st
from pathlib import Path
from PIL import Image
import requests
import json
import os
import openai

api_key = st.secrets["OPENAI_API_KEY"]
if not api_key:
    st.error("OpenAI API key not found in Streamlit secrets.")
else:
    openai.api_key = api_key
#''

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
    Files = st.file_uploader(label = "Upload file", type=["pdf", "png","jpeg"], accept_multiple_files=True)
    Submit = st.form_submit_button(label='Submit')
    

st.markdown("**Extracted Information based on your Entry :** ")

if Files is not None and len(Files) >0:
   # st.markdown("**The file is sucessfully Uploaded.**")
   # Save the uploaded file
    save_folder = '/Users/kaan/Desktop/insurance_app/temp'
    for uploaded_file in Files:
            save_path = os.path.join(save_folder, uploaded_file.name)
            try:
                with open(save_path, 'wb') as f:
                    f.write(uploaded_file.getbuffer())
                st.success(f"File saved at {save_path}")
            except Exception as e:
                st.error(f"Error saving file: {e}")

# Chatbot Interface
st.markdown("**Chat with our Insurance Chatbot:**")
if 'openai_model' not in st.session_state:
    st.session_state['openai_model'] = 'gpt-3.5-turbo'

if 'messages' not in st.session_state:
    st.session_state.messages = []

with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("You: ")
    submit_chat = st.form_submit_button(label='Send')

if submit_chat and user_input:
    # Send user input to OpenAI and get the response
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=user_input,
        max_tokens=150
    )
    bot_response = response.choices[0].text.strip()
    
    # Store messages in session state
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", bot_response))

# Display chat history
for sender, message in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**You**: {message}")
    else:
        st.markdown(f"**Bot**: {message}")
