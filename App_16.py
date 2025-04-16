import streamlit as st
import numpy as np

st.set_page_config(
    page_title='Meu App',
    layout='wide',
    initial_sidebar_state='expanded'
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader('Coluna 1')

with col2:
    st.subheader('Coluna 2')

with col3:
    st.subheader('Coluna 3')

with col4:
    st.subheader('Coluna 4')

col1, col2 = st.columns([3, 1])
data = np.random.randn(100, 1)

with col1:
    st.subheader('Coluna 1')
    col1.line_chart(data)
    
with col2:
    st.subheader('Coluna 2')
    col2.write(data)
