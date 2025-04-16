import altair as alt
import pandas as pd
import streamlit as st

data = pd.DataFrame({
    'Month': ['01-JAN', '02-FEV', '03-MAR', '04-ABR', '05-MAI', '06-JUN', '07-JUL', '08-AGO', '09-SET', '10-OUT', '11-NOV', '12-DEZ'],
    'Produto_A': [28, 55, 43, 91, 81, 53, 19, 87, 52, 85, 101, 77],
    'Produto_B': [93, 68, 79, 84, 81, 97, 109, 99, 125, 115, 120, 88]
})
st.dataframe(data.style)

st.subheader('Gráfico de Linhas: Produto A & B')

graf_linha_A = alt.Chart(data).mark_line(
    point=alt.OverlayMarkDef(color='red', size=100, filled=False, fill='white'),
    color='red'
).encode(
    x = alt.X('Month'),
    y = alt.Y('Produto_A', axis=alt.Axis(grid=False), scale=alt.Scale(domain=(0,160))),
    tooltip=['Month', 'Produto_A', 'Produto_B']
).properties(
    width=600,
    height=300,
    title='Vendas Mensais dos produtos A e B'
)

graf_linha_B = alt.Chart(data).mark_line(
    point=alt.OverlayMarkDef(color='green', size=100, filled=False, fill='white'),
    color='green'
).encode(
    x = alt.X('Month'),
    y = alt.Y('Produto_B'),
    tooltip=['Month', 'Produto_A', 'Produto_B']
)

rotulo_A = graf_linha_A.mark_text(
    dy=-15,
    size=14
).encode(text='Produto_A')

rotulo_B = graf_linha_B.mark_text(
    dy=-15,
    size=14
).encode(text='Produto_B')

st.altair_chart(graf_linha_A+graf_linha_B+rotulo_A+rotulo_B, use_container_width=True)
