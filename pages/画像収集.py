import streamlit as st
from icrawler.builtin import BingImageCrawler


title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
