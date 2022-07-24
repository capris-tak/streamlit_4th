import streamlit as st
import torch
from transformers import BertJapaneseTokenizer, BertModel, BertForMaskedLM

st.title('BERTによる自然言語処理入門')
st.write("This is a sample home page in the mutliapp.")

model_name = 'cl-tohoku/bert-base-japanese-whole-word-masking'
tokenizer = BertJapaneseTokenizer.from_pretrained(model_name)

tokenizer.tokenize('明日はマシンラーニングの勉強をしよう。')

st.image(test.jpg)
