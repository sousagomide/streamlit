import altair as alt
import pandas as pd
import streamlit as st
import numpy as np
import datetime

df = pd.read_excel(
    io='faturamento.xlsx',
    engine='openpyxl',
    sheet_name='Interação',
    usecols='A:C',
    nrows=40
)
st.dataframe(df)

st.subheader('Botão')
if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)
if st.session_state.button:
    # The message and nested widget will remain on the page
    st.write('Button is on!')
    st.slider('Select a value')
else:
    st.write('Button is off!')

def convert_df(df):
    return df.to_csv().encode('utf-8')

st.download_button(
    label='Baixar dados *.csv',
    data=convert_df(df),
    file_name='df.csv',
    mime='text/csv'
)

st.subheader('Checkbox')
select = st.checkbox('Marque a caixa')
if select == True:
    st.write('Fui selecionado')

st.subheader('Radio Button')

tipoRelatorio = st.radio(
    'Selecione o tipo de relatório:',
    ('Mensal', 'Semestral', 'Anual')
)
st.write('Você selecionou o tipo: ', tipoRelatorio)

st.subheader('Caixa de Seleção')
opcoes = st.selectbox(
    'Selecione a matéria-prima para análise:',
    ('Aço', 'Plástico', 'Borracha', 'Madeira')
)
st.write('Você selecionou: ', opcoes)

st.subheader('Seleção múltipla')
multi = st.multiselect(
    'Selecione o banco para consulta:',
    ['Bradesco', 'Banco do Brasil', 'Caixa Econômica', 'Itaú']
)
st.write('Você selecionou as bandeiras: ', multi)

st.subheader('Slider')
parcelas = st.slider(
    'Com quantas parcelas deseja simular?', 0, 60, 30
)
st.write('Selecionou: ', parcelas, ' parcelas')

intervalo = st.slider(
    'Qual o intervalo desejado?', 0.0, 100.0, (25.0, 75.0)
)
st.write('Intervalo selecionado ', intervalo)

st.subheader('Datas')
d = st.date_input(
    'Selecione a data: ',
    datetime.date.today()
)
st.write('A data selecionada foi: ', d)
