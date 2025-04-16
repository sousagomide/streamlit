import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title='Meu App',
    layout='wide',
    initial_sidebar_state='expanded'
)

selected = option_menu(
    menu_title='Menu Principal',
    options=['Início', 'Vendas', 'Relatórios', 'Dashboards', 'Suporte'],
    icons=['house', 'basket', 'bandaid', 'bar-chart', 'bell'],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal',
    styles={
        'nav-link-selected': {'background-color': 'green'}
    }
)

# with st.sidebar:
#     selected = option_menu(
#         menu_title='Menu Principal',
#         options=['Início', 'Vendas', 'Relatórios', 'Dashboards', 'Suporte'],
#         icons=['house', 'basket', 'bandaid', 'bar-chart', 'bell'],
#         menu_icon='cast',
#         default_index=0
#     )

