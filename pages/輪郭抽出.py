import streamlit as st
import numpy as np
from PIL import Image
import cv2
import io

neiborhood8 = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]],
    np.uint8
)

st.header('Edge Detect')
# https://www.youtube.com/watch?v=y86po2F8Gjg
# 【ゆっくり解説】線画抽出！OpenCVで画像からぬりえ作る【Python/初心者向けパイソンプログラミング講座】 あずぱん動画


uploaded_image = st.file_uploader('Choose an image..',type=['png', 'jpg','jpeg','webp'])

ite_n = st.slider('線の太さ default:3', 0, 10, 3)

if uploaded_image is not None:
	#with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
	#	fp = Path(tmp_file.name)
	#	fp.write_bytes(uploaded_image.getvalue())
	
	image=Image.open(uploaded_image)
	img_array = np.array(image)
	gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
	dilated = cv2.dilate(gray, neiborhood8, iterations=ite_n)
	diff = cv2.absdiff(dilated, gray)
	contour = 255 - diff
	
	col1, col5 = st.columns(2)
	with col1:
		st.image(img_array, caption = '1 original', use_column_width = True)
	with col5:	
		st.image(contour, caption = '5 contour', use_column_width = True)
		
	is_success, im_buf_arr = cv2.imencode(".jpg", contour)
	byte_im = im_buf_arr.tobytes()
	#io_buf = io.BytesIO(contour)
	#byte_im = io_buf.getvalue()
	#save_image = Image.open(byte_im)
	btn = st.download_button(label="Download image", data=byte_im, file_name="edge.jpg", mime="image/jpg")
	
	col2, col3, col4 = st.columns(3)
	with col2:
		st.image(gray, caption = '2 grayscale', use_column_width = True)
	with col3:
		st.image(dilated, caption = '3 dilated', use_column_width = True)
	with col4:
		st.image(diff, caption = '4 absdiff', use_column_width = True)
		


	
	


#st.title("Streamlit + OpenCV Sample")
#img = np.zeros((500, 500, 3), np.uint8)
#cv2.rectangle(img, (100, 100), (400, 400), color=(255, 0, 0), thickness=-1)
#st.image(img)
