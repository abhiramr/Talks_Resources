# Import the wrapper function from your package
from streamlit_custom_slider import st_custom_slider
import streamlit as st
from streamlit_custom_slider import st_range_slider

st.title("Testing Streamlit custom components")

# Store and display the return value of your custom component
# v = st.slider("Hello world", 0, 100)
# st.write(v)

# Streamlit custom slider

v_custom = st_custom_slider('Hello world', 0, 100, 50, key="slider1")
st.write(v_custom)

# Add a range slider
v_custom_range = st_range_slider('Hello world', 0, 100, (20, 60), key="slider2")
st.write(v_custom_range)