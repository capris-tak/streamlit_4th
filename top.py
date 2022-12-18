import streamlit as st
import numpy as np
from PIL import Image
import cv2
#import tempfile


neiborhood8 = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]],
    np.uint8
)

st.header('Edge Detect')

uploaded_image = st.file_uploader('Choose an image..',type=['png', 'jpg','jpeg','webp'])
if uploaded_image is not None:
	#with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
	#	fp = Path(tmp_file.name)
	#	fp.write_bytes(uploaded_image.getvalue())

	image=Image.open(uploaded_image)
	img_array = np.array(image)
	st.image(img_array, caption = 'original',use_column_width = True)
	
	gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
	st.image(gray, caption = 'grayscale',use_column_width = True)
	
	dilated = cv2.dilate(gray, neiborhood8, iterations=3)
	st.image(dilated, caption = 'dilated',use_column_width = True)
	


st.title("Streamlit + OpenCV Sample")
img = np.zeros((500, 500, 3), np.uint8)
cv2.rectangle(img, (100, 100), (400, 400), color=(255, 0, 0), thickness=-1)
st.image(img)
