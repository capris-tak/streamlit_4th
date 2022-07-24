import streamlit as st
import MeCab

mecab = MeCab.Tagger('-Ochasen -d /opt/homebrew/lib/mecab/dic/mecab-ipadic-neologd/')
sent = "自然言語処理の基本を説明します"
st.write(mecab.parse(sent))

mecab2 = MeCab.Tagger('-Owakati -d /opt/homebrew/lib/mecab/dic/mecab-ipadic-neologd/')
st.write(mecab2.parse(sent))

st.image(test.jpg)
