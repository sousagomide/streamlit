import streamlit as st

st.title('Este é o título')
st.header('Header do ST')
st.subheader('Subheader do ST')

st.markdown('A nota dos alunos foi em **média**, maior que no *semestre* passado')
st.markdown('~~Texto tachado~~')
st.markdown('`Código-fonte - Mais código`')
st.markdown('[Link Google](https://www.google.com.br)')
st.markdown(':fireworks:')

st.caption('Usado para criar legendas')

sourcecode = '''
    if(x == 0):
        a = y * 45
'''
st.code(sourcecode, language='python')

st.text('Este é um texto usando st.text')

# Latex https://katex.org/docs/supported.html
st.latex('\int x²+y²+32ab \isin x²+y³+z²')