# streamlit run app1/hello.py
import streamlit as st 
from PIL import Image
st.title("Sample App")

image =st.camera_input("Take a picture")
if image:
    im= Image.open(image)
    color = st.color_picker("Pick a color","#00f900")
    # purple  gradiant image
    im2 = Image.new("RGB",im.size,color)
    # overlay the two images
    im = Image.blend(im,im2,0.5)
    # resize by 30%
    im = im.resize((int(im.size[0]*0.3),int(im.size[1]*0.3)))
    st.sidebar.image(im)

    filename = st.text_input("save as","image.png")

    if st.button("Save"):
        im.save(filename)
        st.snow()
        st.balloons()


