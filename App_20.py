import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title='Meu App',
    layout='wide',
    initial_sidebar_state='expanded'
)

df = pd.read_excel(
    io='./Arquivos_Alunos/Datasets/normal_dist.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    usecols='A:C',
    nrows=87
)

# if st.button('Iniciar'):
#     st.experimental_rerun()
if st.button('Parar'):
    st.stop()


histograma = alt.Chart(df).mark_bar().encode(
    x=alt.X('x', bin=alt.Bin(step=5)),
    y='sum(count)'
)
st.subheader('Histograma - Notas de 1000 alunos')
st.altair_chart(histograma, use_container_width=True)
st.dataframe(df)