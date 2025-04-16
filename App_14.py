import streamlit as st
from PIL import Image

myDog = Image.open('./Arquivos_Alunos/Mídia/dog.jpg')
st.subheader('1 - Imagem de cachorro')
st.image(myDog, caption='Um cachorro desconfiado')

myAudio = open('./Arquivos_Alunos/Mídia/Scratching The Surface.mp3', 'rb')
abrirAudio = myAudio.read()
st.subheader('2 - Minha música')
st.audio(abrirAudio, format='audio/mp3')

myVideo = open('./Arquivos_Alunos/Mídia/Buildings.mp4', 'rb')
abrirVideo = myVideo.read()
st.subheader('3 - Abir meu vídeo')
st.video(abrirVideo)