import streamlit as st
from icrawler.builtin import BingImageCrawler


keywd = st.text_input('search word', 'name')
st.write('The current word is', keywd)
