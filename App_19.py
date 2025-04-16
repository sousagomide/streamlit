import streamlit as st
import time

st.set_page_config(
    page_title='Meu App',
    layout='wide',
    initial_sidebar_state='expanded'
)

myBar = st.progress(0)
for num in range(100):
    time.sleep(0.01)
    myBar.progress(num+1)

with st.spinner('Aguarde...'):
    time.sleep(1)

st.success('Seu dado voi enviado com sucesso')
st.error('Falha ao fazer download')
st.warning('Data fora do intervalo')
st.info('Informe o endereço')

e = RuntimeError('Exceção do tipo RuntimeError')
st.exception(e)

st.snow()
st.balloons()