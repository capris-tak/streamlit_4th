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
