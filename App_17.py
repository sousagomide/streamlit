import streamlit as st
import numpy as np

st.set_page_config(
    page_title='Meu App',
    layout='wide',
    initial_sidebar_state='expanded'
)

st.header('Expander')
st.line_chart({'data': [1, 5, 2, 6, 2, 1]})

with st.expander('Ver detalhes'):
    st.write('''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus justo urna, feugiat ut eleifend ac, dapibus ac enim. Phasellus vitae augue rutrum, porttitor turpis eu, varius felis. Aenean in tortor non ante euismod tincidunt. Cras ut neque sit amet sem congue elementum vitae non tortor. Sed ultricies est justo, id pellentesque est molestie vel. Suspendisse ut laoreet metus, nec vulputate lectus. Curabitur egestas ornare justo tincidunt posuere. Integer aliquam sapien et metus blandit ornare. Nunc finibus ultrices bibendum.
        Pellentesque vulputate urna felis, in semper ligula convallis vel. Sed vel leo at diam tristique hendrerit sit amet nec arcu. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In rutrum neque sed diam pellentesque consectetur. Sed nec rhoncus nisl. Etiam sit amet enim fringilla, semper ex sed, molestie lorem. Donec accumsan ipsum et lectus pulvinar, vel cursus neque imperdiet. Fusce in dolor tincidunt diam pretium semper sit amet eu arcu. Suspendisse potenti. Suspendisse luctus varius arcu eget porttitor. Cras egestas nibh a ornare malesuada. Duis sed semper mauris. Nulla facilisi.
    ''')
    st.image('./Arquivos_Alunos/Mídia/dice.jpg')