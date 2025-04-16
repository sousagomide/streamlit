import streamlit as st
import time as t
import datetime as dt

st.set_page_config(
    page_title='Meu App',
    layout='wide',
    initial_sidebar_state='expanded'
)

def mostrarResultado():
    st.write('Modal:')
    st.write(varModal)
    st.write('Cliente: ', varCliente)
    st.write('Bandeiras: ')
    st.write(varBanco)
    st.write('Parcelas: ', varSlider)
    st.write('Data: ', varData)

with st.form('Formulário de seleção de parâmetros'):
    varModal = st.sidebar.selectbox(
        'Selecione o modo de transporte:',
        ('Rodoviário', 'Marítimo', 'Aéreo', 'Trem', 'Outro')
    )

    with st.sidebar:
        varCliente = st.radio(
            'Selecione o cliente:',
            ('Space X', 'Microsoft', 'Apple', 'IBM')
        )
        varBanco = st.multiselect(
            'Selecione a bandeira:',
            ['Bradesco', 'Itaú', 'Banco do Brasil', 'Caixa Econômica', 'Santander']
        )
        varSlider = st.slider(
            'Quantas parcelas deseja financiar?', 0, 60, 30
        )
        varData = st.date_input(
            'Selecione a data do vencimento:',
            dt.date.today()
        )
        botao_form = st.form_submit_button('Filtrar')

if botao_form:
    st.success('Obrigado por filtrar os dados.')
    mostrarResultado()


    
    
