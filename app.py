import streamlit as st
# from pptx import Presentation
# from pptx.util import Inches,Pt
# from datetime import date
from PIL import Image
from io import BytesIO
from datetime import datetime
import requests
import openai
from PIL import Image
from io import BytesIO


def enable_download(ppt_file):
    filename = prompt +" "+str(datetime.now())+" "+".pptx"
    st.sidebar.write("Download your PPT here!! :gear:")
    st.sidebar.download_button(label='Click to download PowerPoint',
                        data=ppt_file.getvalue(),
                        file_name=filename)

def get_images(prompt,n):
    openAI_token = "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"
    openai.api_key = openAI_token
    response = openai.Image.create(
    prompt= prompt,
    n=n,
    size="512x512"
    )
    i=0
    try:
        for image in response['data']:
            response = requests.get(image['url'])
        # Convert the image data to a PIL image and save it to your computer
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            # image.show()
            image.save("GEN_IMG"+str(i)+".png")
        # files.download(prompt_text+str(i)+".png")
            i+=1
    except:
        print(" error in generating images.Please refresh the page ")
def display(prompt,n):
    get_images(prompt,n)
    try:
        for i in range(0,n):
                st.image("GEN_IMG"+str(i)+".png")
    except:
        print("error in loading image files.Please refresh the page")

a = st.empty()

st.write("Team ABS presents....")
st.title("Image Generator")

st.write("## Get images based on a text prompt")
st.write(
    " Write a prompt into the textbox below and watch the magic happen"
)


ppt_data = "REPLACE WITH PPT"


prompt = st.text_input("Terms","Your prompt").lower()
st.write(
    " please enter How many images do you want to generate"
)
num=st.number_input("The number",min_value=1,max_value=10)

if st.button("Generate"):
    display(prompt,num)

# st.image("./images/bg1.jpeg") 