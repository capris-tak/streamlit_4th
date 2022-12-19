import streamlit as st
import numpy as np
from PIL import Image
import cv2
import io


uploaded_image = st.file_uploader('Choose an image..',type=['png', 'jpg','jpeg','webp'])




if uploaded_image is not None:
	st.header('Edge Detect')
	# https://www.youtube.com/watch?v=y86po2F8Gjg
	# 【ゆっくり解説】線画抽出！OpenCVで画像からぬりえ作る【Python/初心者向けパイソンプログラミング講座】 あずぱん動画
	neiborhood8 = np.array([
	    [1,1,1],
	    [1,1,1],
	    [1,1,1]],
	    np.uint8)
	ite_n = st.slider('線の太さ default:3', 0, 10, 3)
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
		btn = st.download_button(label="Download 5.contour image", data=byte_im, file_name="edge.jpg", mime="image/jpg")

	col2, col3, col4 = st.columns(3)
	with col2:
		st.image(gray, caption = '2 grayscale', use_column_width = True)
	with col3:
		st.image(dilated, caption = '3 dilated', use_column_width = True)
	with col4:
		st.image(diff, caption = '4 absdiff', use_column_width = True)
	
	
	st.header('rectangle')
	height, width, channels = img_array.shape[:3]
	#st.write("width: " + str(width))
	#st.write("height: " + str(height))
	
	r_col1, r_col2 = st.columns(2)
	with r_col1:
		pt1_x = st.slider('left top default:0', 0, width, 0)
		pt1_y = st.slider('left botom default:0', 0, height, 0)
	with r_col2:
		pt2_x = st.slider('right top default:'+str(width), width, 0, width)
		pt2_y = st.slider('right botom default:'+str(height), height, 0, height)

	rect = cv2.rectangle(img_array,
	      pt1=(pt1_x+1, pt1_y+1),
	      pt2=(pt2_x, pt2_y),
	      color=(0, 255, 0),
	      thickness=1,
	      lineType=cv2.LINE_4,
	      shift=0)
	
	rc_col1, rc_col2 = st.columns(2)
	with rc_col1:
		st.image(rect, caption = 'rectangle', use_column_width = True)
	with rc_col2:
		rect_cut = img_array[pt1_y:pt2_y+1, pt1_x:pt2_x+1,:]
		st.image(rect_cut, caption = 'trim', use_column_width = True)

		


	
	


#st.title("Streamlit + OpenCV Sample")
#img = np.zeros((500, 500, 3), np.uint8)
#cv2.rectangle(img, (100, 100), (400, 400), color=(255, 0, 0), thickness=-1)
#st.image(img)
