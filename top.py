import streamlit as st
from sympy import *
from sympy.abc import *
init_printing()

st.write('積分∫3𝑥2𝑑𝑥')
st.write(integrate(3*x**2, x))

