import streamlit as st
import pandas as pd
from banco.db import connect_db  # Importamos a função de conexão

# Obtém o id do usuário logado
id_usuario = st.experimental_user.to_dict()['sub']

st.title("Meus Cursos Comprados")
st.divider()

# Consulta os cursos comprados pelo usuário
try:
    conn = connect_db("compras")
    if conn is None:
        st.error("Erro ao conectar ao banco de dados")
    else:
        query = "SELECT * FROM compras WHERE id_user = ?"
        df = pd.read_sql_query(query, conn, params=(id_usuario,))
        conn.close()
except Exception as e:
    st.error(f"Erro ao carregar os cursos comprados: {e}")
    df = pd.DataFrame()

if df.empty:
    st.info("Você não possui cursos comprados.")
else:
    # Converte os registros para uma lista de dicionários
    cursos = df.to_dict('records')
    
    # Itera em blocos de 3 cursos para organizar em linhas de 3 colunas
    for i in range(0, len(cursos), 3):
        cols = st.columns(3)
        for j, curso in enumerate(cursos[i:i+3]):
            with cols[j]:
                # Cria um container com borda utilizando HTML e CSS
                st.markdown(
                    f"""
                    <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px;">
                        <h3>{curso['curso']}</h3>
                        <p><strong>ID da Compra:</strong> {curso['id']}</p>
                        <p><strong>ID do Curso:</strong> {curso['id_curso']}</p>
                        <p><strong>Status:</strong> {"Finalizado" if curso['finalizado'] == 1 else "Não Finalizado"}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
