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
    for image in response['data']:
        response = requests.get(image['url'])
    # Convert the image data to a PIL image and save it to your computer
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        # image.show()
        image.save("GEN_IMG"+str(i)+".png")
    # files.download(prompt_text+str(i)+".png")
        i+=1

def display(prompt,n):
    get_images(prompt,n)
    for i in range(0,n):
            st.image("GEN_IMG"+str(i)+".png")

# def ppt_generation():

#     # open presentation template
#     # pptx = 'template.pptx'
#     prs = Presentation()
#     title_slide_layout = prs.slide_layouts[0]
#     slide = prs.slides.add_slide(title_slide_layout)
#     title = slide.shapes.title
#     subtitle = slide.placeholders[1]

#     title.text = prompt
#     subtitle.text = "That's what its about!"
#     genTitles,genText = read_text()

    
#     slideCount = len(genTitles)
#     for i in range(slideCount):
#         #Slide Images
#         blank_slide_layout = prs.slide_layouts[1]
#         slide = prs.slides.add_slide(blank_slide_layout)

#         slideTitle = slide.placeholders[0]
#         slideContent = slide.placeholders[1]

#         slideTitle.text = genTitles[i]
#         slideContent.size = Pt(20)
#         slideContent.text = genText[i]


        

        # left = top = width = height = Inches(1)
        # # txBox = slide.shapes.add_textbox(left, top, width, height)
        # txBox = slide.shapes.add_textbox(left, top, prs.slide_width -Inches(2), height)
        # tf = txBox.text_frame

        # img_path = "./imgs/generated_image"+str((i)%7+1)+".jpg"
        # pic = slide.shapes.add_picture(img_path, prs.slide_width - Inches(2.5), 0,Inches(2))
        
        

        # p = tf.add_paragraph()
        # p.text = genTitles[i]
        # p.font.size = Pt(40)
        # p.font.bold = True

        # pic = slide.shapes.add_picture(img_path, prs.slide_width - Inches(5), Inches(1),)
        # # tf.text = "This is text inside a textbox"
        # txBox = slide.shapes.add_textbox(left, top+Inches(3), prs.slide_width -Inches(2), height)
        # tf = txBox.text_frame
        # p = tf.add_paragraph()  
        # p.text = genText[i]



    # # save presentation as binary output
    # binary_output = BytesIO()
    # prs.save(binary_output) 

    # # display success message and download button
    # st.success('The slides have been generated!')
    
    # return binary_output

def read_text():
    with open('text_gen.txt') as f:
        titles = []
        contents = []
        lines = f.readlines()
        for line in  lines:
            if line == " " or line == "":
                continue
            # st.write(line)
            l = line.split(" ", 1)
            if len(l) < 2:
                continue
            # st.write(l)
            titles.append(l[0])
            contents.append(l[1])
        return [titles,contents]
    


st.set_page_config(layout="wide")

# st.title("Team ABS")
# st.header("prompt")

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