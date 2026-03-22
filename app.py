import streamlit as st

from dotenv import load_dotenv
from google import genai
from PIL import Image
import os
load_dotenv()
api_key=os.getenv("API_KEY")

file=st.image_path=st.file_uploader("Upload an Image",
                            type=["PNG","JPG"])

if file is not None:
    st.image(Image.open(file))

prompt=st.text_input("enter the prompt")

if st.button("generate"):
    client=genai.Client(api_key=api_key)
    img=Image.open(file)
    Input=[img,prompt]
    response=client.models.generate_content(model='gemini-2.5-flash',
                               contents=Input)
    st.success(response.text)
    
