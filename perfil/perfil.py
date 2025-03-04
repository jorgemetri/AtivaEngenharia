import streamlit as st
from banco.db import create_db_usuario,display_compras_filtrada,display_compras,display_cursos,insert_curso,insert_compra,display_usuarios, create_db_compras, create_db_cursos
  
st.write('Perfil')



if st.button('Criar DB Usuario'):
    create_db_usuario('usuarios')
if st.button('Criar DB Compras'):
    create_db_compras('compras')
if st.button('Criar DB Cursos'):
    create_db_cursos('cursos')

if st.button('Exibir DB Usuario'):
    display_usuarios('usuarios')
if st.button('Exibir linha DB Compras'):
    #display_compras('compras')
    display_compras_filtrada('compras',st.experimental_user.to_dict()['sub'])
if st.button('Exibir linha DB Cursos'):
    display_cursos('cursos')

if st.button('Inserir linha Cursos'):
    pass
   # insert_compra('comprar','Segunranca',st.experimental_user.to_dict['sub'],2,0)
if st.button('Inserir linha Compra'):
    insert_compra('compras',)



    