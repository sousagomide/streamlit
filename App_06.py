import altair as alt
import pandas as pd
import streamlit as st

data = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})
st.subheader('Esse é o nosso dataset de exemplo')
st.write(data)

graf_barras = alt.Chart(data).mark_bar().encode(
    x = 'a', 
    y = 'b', 
    color = 'a',
    tooltip = ['a', 'b']
)
rotulo = graf_barras.mark_text(
    dy = -8,
    size = 14
).encode(
    text = 'b'
)
st.subheader('Plot do gráfico de barras')
st.altair_chart(graf_barras+rotulo, use_container_width = True)

graf_area = alt.Chart(data).mark_area(
    color = 'lightblue',
    interpolate = 'step-after',
    line = True
).encode(
    x = 'a',
    y = 'b',
    tooltip = ['a', 'b']
)
rotulo_area = graf_area.mark_text(
    dy = -8,
    dx = 30,
    size = 14
).encode(
    text = 'b'
)
st.subheader('Gráfico de Área')
st.altair_chart(graf_area+rotulo_area, use_container_width = True)

graf_pizza = alt.Chart(data).mark_arc().encode(
    theta=alt.Theta(field='b', type='quantitative'),
    color=alt.Color(field='a', type='nominal')
)
st.subheader('Gráfico de Pizza')
st.altair_chart(graf_pizza, use_container_width=True)

