import streamlit as st
import pandas as pd
import numpy as np

st.header('Aula de Dataframe')
df = pd.DataFrame(
    np.random.randn(5, 5),
    columns = ('col %d' %i for i in range(5))
)
st.dataframe(df)
st.write(df)

st.subheader('Exemplo 2 - Alterando dimensões')
st.dataframe(df, 300, 200)

st.subheader('Exemplo 3 - Dando um destaque nos maiores valores')
st.dataframe(df.style.highlight_max(axis = 0))

st.header('TABLE - Exemplo similar ao DataFrame')
st.table(df)