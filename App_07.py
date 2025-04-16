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


graf_barras_novo = alt.Chart(data).mark_bar(
    cornerRadiusTopLeft=10,
    cornerRadiusTopRight=10
).encode(
    x = alt.X('a', sort='y', title='Categorias'),
    y = alt.Y('b', title='Notas'),
    color = alt.condition(alt.datum.b > 43, alt.value('steelblue'), alt.value('black'))
).properties(
    title='Título do Gráfico'
)
rotulo = graf_barras_novo.mark_text(
    align='center',
    baseline='middle',
    size=14,
    dy=-10
).encode(text='b')
linha_media = alt.Chart(data).mark_rule(color='red').encode(
    y='mean(b)'
)
st.altair_chart(graf_barras_novo+rotulo+linha_media, use_container_width=True)
