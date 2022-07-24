import streamlit as st
import torch
from transformers import BertJapaneseTokenizer, BertModel, BertForMaskedLM

st.title('Home')
st.write("This is a sample home page in the mutliapp.")

body_estimation = Body('pytorch-openpose/model/body_pose_model.pth')
hand_estimation = Hand('pytorch-openpose/model/hand_pose_model.pth')


st.image(test.jpg)
