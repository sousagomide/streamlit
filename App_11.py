import altair as alt
import pandas as pd
import streamlit as st

df = pd.read_csv('vega_car.csv')

st.dataframe(df)

disper = alt.Chart(df).mark_point().encode(
    x='Weight_in_lbs:Q',
    y='Miles_per_Gallon',
    color=alt.Color('Origin:N')
)

st.subheader('Gráfico de dispersão: Consumo por cavalo')
st.altair_chart(disper, use_container_width=True)