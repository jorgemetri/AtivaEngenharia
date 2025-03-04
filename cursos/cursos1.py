import streamlit as st
from banco.db import insert_curso, insert_compra,display_compras_filtrada

st.title('Cursos Disponíveis \U0001F4DA')
st.divider()

col1, col2, col3 = st.columns(3,border=True)

with col1:
    st.write('Curso 1')
    st.divider()
    st.button('Comprar', key='curso1', on_click=lambda: insert_compra('compras', 'NR', st.experimental_user.to_dict()['sub'], 1, 0))
with col2:
    st.write('Curso 2')
    st.divider()
    st.button('Comprar', key='curso2', on_click=lambda: insert_compra('compras', 'Segurança', st.experimental_user.to_dict()['sub'], 3, 0))
with col3:
    st.write('Curso 3')
    st.divider()
    st.button('Comprar', key='curso3', on_click=lambda: insert_compra('compras', 'ISO', st.experimental_user.to_dict()['sub'], 4, 0))
