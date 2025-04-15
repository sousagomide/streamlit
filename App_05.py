import streamlit as st

meuObjeto = {
    'banana': 'amarela',
    'maca': 'vermelha',
    'limao': 'verde',
    'uva': 'roxa'
}

st.json(meuObjeto)