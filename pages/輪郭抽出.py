import streamlit as st
import numpy as np
from PIL import Image
import cv2
import io
from matplotlib import pyplot as plt


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
		btn = st.download_button(label="Download contour image", data=byte_im, file_name="edge.jpg", mime="image/jpg")

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
	
	#r_col1, r_col2 = st.columns(2)
	#with r_col1:
	pt1_x, pt2_x = st.slider('width', 0, width, value=(0, width),)
	pt1_y, pt2_y = st.slider('height', 0, height, value=(0, height),)
	#with r_col2:
		#pt2_x = st.slider('right top default:'+str(width), width, 0, width)
		#pt2_y = st.slider('right botom default:'+str(height), height, 0, height)

	rect = cv2.rectangle(img_array,
	      pt1=(pt1_x+1, pt1_y+1),
	      pt2=(pt2_x-1, pt2_y-1),
	      color=(0, 200, 0),
	      thickness=2,
	      lineType=cv2.LINE_8,
	      shift=0)
	
	rc_col1, rc_col2 = st.columns(2)
	with rc_col1:
		st.image(rect, caption = 'rectangle', use_column_width = True)
	with rc_col2:
		rect_cut = img_array[pt1_y:pt2_y, pt1_x:pt2_x,:]
		st.image(rect_cut, caption = 'trim', use_column_width = True)

		
		
		
		
		
	st.header('tiling')	
	import glob
	folder_imgs = glob.glob('pages/犬/*.jpg')
	#st.write(foulderimgs)

	#multiple images　Grid表示

	photo_n = st.slider('num', 1, len(folder_imgs), 1)
	imag=Image.open(folder_imgs[photo_n-1])
	st.image(np.array(imag), caption = str(photo_n) + ' selected', use_column_width = True)

	idx = 0
	#col_num = 10

	for _ in range(len(folder_imgs)-1):
		cols = st.columns(5)

		if idx < len(folder_imgs):
			cols[0].image(folder_imgs[idx],width=150, caption=str(idx+1))
			idx += 1
		if idx < len(folder_imgs):
			cols[1].image(folder_imgs[idx],width=150, caption=str(idx+1))
			idx += 1
		if idx < len(folder_imgs):
			cols[2].image(folder_imgs[idx],width=150, caption=str(idx+1))
			idx += 1
		if idx < len(folder_imgs):
			cols[3].image(folder_imgs[idx],width=150, caption=str(idx+1))#caption=foulder_imgs[idx].split('/')[-1])
			idx += 1
		if idx < len(folder_imgs):
			cols[4].image(folder_imgs[idx],width=150, caption=str(idx+1))
			idx += 1
		else:
			break
		
		
	st.header('tiling2')
	
	width = 800
	padding = st.slider('padding', 0, 100, 4)
	img = np.zeros((int(padding/2), width, 3), np.uint8)
	img[:,:,:] = 255
	imgbottom = img
	
	for i in range(0, len(folder_imgs), 2):
		#img1 = Image.open(foulder_imgs[i])
		img1 = cv2.imread(folder_imgs[i])
		h1, w1, ch = img1.shape[:3]
		if i+1 == len(folder_imgs):
			img2 = np.zeros((int(width/2), int(width/2), 3), np.uint8)
			img2[:, :, :] = 255
			h2, w2, ch = img2.shape[:3]
		else:
			#img2 = Image.open(foulder_imgs[i+1])
			img2 = cv2.imread(folder_imgs[i+1])
			h2, w2, ch = img2.shape[:3]
			
		r1 = (width - padding*3) * h2 / (h2*w1 + h1*w2)
		r2 = (width - padding*3) * h1 / (h2*w1 + h1*w2)
		
		h1r = int(h1*r1)
		w1r = int(w1*r1)
		h2r = int(h2*r2)
		w2r = int(w2*r2)
		
		img1r = cv2.resize(img1, (w1r, h1r))
		img2r = cv2.resize(img2, (w2r, h2r))
		
		img_c = np.zeros((h1r+padding, width, 3), np.uint8)
		img_c[:,:,:] = 255
		
		img_c[int(padding/2):int(padding/2)+h1r, padding:padding+w1r, :] = img1r
		img_c[int(padding/2):int(padding/2)+h2r, padding*2+w1r:padding*2+w1r+w2r, :] = img2r
		
		img = cv2.vconcat([img, img_c])
		
	img_t = cv2.vconcat([img, imgbottom])
	tiled_img = cv2.cvtColor(img_t, cv2.COLOR_BGR2RGB)
	st.image(tiled_img, caption = 'tile', use_column_width = True)
	
	is_success, im_buf_arr = cv2.imencode(".jpg", img_t)
	byte_im = im_buf_arr.tobytes()
	btn = st.download_button(label="Download image", data=byte_im, file_name="tiled_image.jpg", mime="image/jpg")	
	
	
	
	st.header('tiling3')
	pm = st.slider('x', 1, 10, 3)
	d = []
	for folder_img in folder_imgs:
		img = Image.open(folder_img)
		img = np.asarray(img)
		#img = cv2.resize(img, (400, 400), cv2.INTER_LANCZOS4)
		d.append(img)
	
	fig, ax = plt.subplots(pm, pm, figsize=(10, 10))
	fig.subplots_adjust(hspace=0, wspace=0)

	for i in range(pm):
		for j in range(pm):
			if pm*i+j < len(folder_imgs):
				ax[i, j].axis('off')
				#ax[i, j].xaxis.set_major_locator(plt.NullLocator())
				#ax[i, j].yaxis.set_major_locator(plt.NullLocator())
				ax[i, j].imshow(d[pm*i+j])#, cmap="bone")
			else:
				ax[i, j].set_visible(False)
				ax[i, j].xaxis.set_major_locator(plt.NullLocator())
				ax[i, j].yaxis.set_major_locator(plt.NullLocator())
	#plt.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False, bottom=False, left=False, right=False, top=False)
	st.pyplot(fig)
	#plt.show()
	
	
	with st.expander("streamlitとは？", expanded=False):
		st.subheader("データアプリを構築して共有するためのより高速な方法")
		st.write("Streamlitは、データスクリプトを数分で共有可能なWebアプリに変換します。\
		すべて純粋なPythonで出来ています。フロントエンドの経験は不要です。")
		
#st.title("Streamlit + OpenCV Sample")
#img = np.zeros((500, 500, 3), np.uint8)
#cv2.rectangle(img, (100, 100), (400, 400), color=(255, 0, 0), thickness=-1)
#st.image(img)
