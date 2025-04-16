import altair as alt
import pandas as pd
import streamlit as st

df = pd.read_excel(
    io='faturamento.xlsx',
    engine='openpyxl',
    sheet_name='flow',
    usecols='A:B',
    nrows=15
)
st.dataframe(df)

graf_area = alt.Chart(df).mark_area(
    color='gray',
    line={'color':'black'},
    point=alt.OverlayMarkDef(color='red')
).encode(
    x='Year:T',
    y='Value:Q'
)

rotulo = graf_area.mark_text(
    size=14,
    color='red',
    dy=-15,
    align='center'
).encode(text='Value')

st.subheader('KPI de resultados anuais')
st.altair_chart(graf_area+rotulo, use_container_width=True)

