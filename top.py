import streamlit as st
import numpy as np
from PIL import Image
import cv2


neiborhood8 = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]],
    np.uint8
)

st.header('Edge Detect')

uploaded_image = st.file_uploader('Choose an image..',type=['png', 'jpg','jpeg','webp'])
image=Image.open(uploaded_image)
img_array = np.array(image)
st.image(img_array,caption = 'サムネイル画像',use_column_width = True)


st.title("Streamlit + OpenCV Sample")
img = np.zeros((500, 500, 3), np.uint8)
cv2.rectangle(img, (100, 100), (400, 400), color=(255, 0, 0), thickness=-1)
st.image(img)
