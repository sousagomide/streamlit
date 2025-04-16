import altair as alt
import pandas as pd
import streamlit as st
import numpy as np

df = pd.read_excel(
    io='normal_dist.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    usecols='A:C',
    nrows=87
)

st.dataframe(df)

histograma = alt.Chart(df).mark_bar().encode(
    x=alt.X('x', bin=alt.Bin(step=10)),
    y='sum(count)'
)


mu = df['x'].mean()
sigma = df['x'].std()
# Gerar pontos para a curva gaussiana
x_vals = np.linspace(df['x'].min(), df['x'].max(), 200)
y_vals = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_vals - mu) / sigma) ** 2)
# Normalizar a curva para escalar com o histograma
scale_factor = df['count'].sum() * 10  # step do bin = 10
y_vals_scaled = y_vals * scale_factor
gauss_df = pd.DataFrame({'x': x_vals, 'gauss': y_vals_scaled})
# Criar a curva gaussiana
linha_gauss = alt.Chart(gauss_df).mark_line(color='red', strokeWidth=2).encode(
    x='x',
    y='gauss'
)

st.subheader('Histograma')
st.altair_chart(histograma+linha_gauss, use_container_width=True)