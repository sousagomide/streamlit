import altair as alt
import pandas as pd
import streamlit as st

df = pd.read_excel(
    io='faturamento.xlsx',
    engine='openpyxl',
    sheet_name='ricos',
    usecols='A:B',
    nrows=9
)

st.dataframe(df)

st.subheader('Gráfico de pizza - Mais ricos do mundo')

graf_pizza = alt.Chart(df).mark_arc(
    innerRadius=30,
    outerRadius=150
).encode(
    theta=alt.Theta(field='Fortuna', type='quantitative', stack=True),
    color=alt.Color(field='Nome', type='nominal', legend=None),
    tooltip=['Nome', 'Fortuna']
).properties(
    width=700,
    height=450
)
rotuloNome = graf_pizza.mark_text(radius=200, size=14).encode(text='Nome')
rotuloValor = graf_pizza.mark_text(radius=170, size=14, fontWeight='bold').encode(text='Fortuna')
st.altair_chart(graf_pizza+rotuloNome+rotuloValor, use_container_width=True)

# tab1, tab2, tab3 = st.tabs(["Gráfico", "Tabela", "Configurações"])

# with tab1:
#     st.header("Gráfico")
#     st.line_chart([1, 5, 2, 6])

# with tab2:
#     st.header("Tabela de Dados")
#     st.write("Aqui vai sua tabela!")

# with tab3:
#     st.header("Configurações")
#     st.checkbox("Ativar modo avançado")
