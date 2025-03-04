import sqlite3
import streamlit as st
import os
import pandas as pd

def GetIdUser(s):
    return s.split('.apps.googleusercontent.com')[0]

def connect_db(name):
    """
    Conecta ao banco de dados SQLite com o nome especificado.

    Args:
        name (str): Nome do banco de dados (sem extensão).

    Returns:
        Connection: Objeto de conexão com o banco de dados ou None em caso de erro.
    """
    try:
        connection = sqlite3.connect(f'{name}.db', check_same_thread=False)
        return connection
    except sqlite3.Error as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

def get_db_as_dataframe(name):
    """
    Conecta ao banco de dados e retorna todo o conteúdo da tabela (nome igual a 'name')
    como um DataFrame do pandas.

    Args:
        name (str): Nome do banco de dados (sem a extensão .db) e também o nome da tabela.

    Returns:
        DataFrame: DataFrame contendo todos os registros da tabela com nome 'name'.

    Raises:
        Exception: Caso não seja possível conectar ao banco de dados ou consultar a tabela.
    """
    conn = connect_db(name)
    if conn is None:
        raise Exception("Erro ao conectar ao banco de dados")
    
    try:
        query = f"SELECT * FROM {name}"
        df = pd.read_sql_query(query, conn)
    except Exception as e:
        raise Exception(f"Erro ao consultar a tabela '{name}': {e}")
    finally:
        conn.close()
    
    return df

# ---------------------------------------------------------------------------------
# Funções de criação das tabelas

def create_db_usuario(name):
    """
    Cria o banco de dados e a tabela de usuários.

    Args: 
        name (str): Nome do banco de dados (sem extensão) e também o nome da tabela a ser criada.

    Campos da tabela:
    - id_user: Id único no formato '512227233941-igk87iel2b5fuddmh8jl72do7q189j3e'.
    - name: Nome do usuário.
    - email: Email do usuário.
    """
    db_file = f"{name}.db"
    if os.path.exists(db_file):
        st.write(f"O banco de dados '{db_file}' já existe.")
        return
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE {name} (
            id_user TEXT PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()
    st.write(f"O banco de dados '{db_file}' e a tabela '{name}' foram criados com sucesso.")

def create_db_compras(name):
    """
    Cria o banco de dados e a tabela de compras.

    Args:
        name (str): Nome do banco de dados (sem extensão) e também o nome da tabela a ser criada.

    Campos da tabela:
    - id: Id da compra.
    - curso: Nome do curso.
    - id_user: Id do usuário.
    - id_curso: ID do curso.
    - finalizado: Curso finalizado? (0 para não, 1 para sim)
    """
    db_file = f"{name}.db"
    if os.path.exists(db_file):
        st.write(f"O banco de dados '{db_file}' já existe.")
        return
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE {name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            curso TEXT,
            id_user TEXT,
            id_curso INTEGER,
            finalizado INTEGER
        )
    ''')
    conn.commit()
    conn.close()
    st.write(f"O banco de dados '{db_file}' e a tabela '{name}' foram criados com sucesso.")

def create_db_cursos(name):
    """
    Cria o banco de dados e a tabela de cursos.

    Args:
        name (str): Nome do banco de dados (sem extensão) e também o nome da tabela a ser criada.

    Campos da tabela:
    - cod_curso: Código único do curso (INTEGER PRIMARY KEY AUTOINCREMENT).
    - curso: Nome do curso.
    - descricao: Descrição do curso.
    - preco: Preço do curso.
    """
    db_file = f"{name}.db"
    if os.path.exists(db_file):
        st.write(f"O banco de dados '{db_file}' já existe.")
        return
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE {name} (
            cod_curso INTEGER PRIMARY KEY AUTOINCREMENT,
            curso TEXT,
            descricao TEXT,
            preco REAL
        )
    ''')
    conn.commit()
    conn.close()
    st.write(f"O banco de dados '{db_file}' e a tabela '{name}' foram criados com sucesso.")

# ---------------------------------------------------------------------------------
# Funções CRUD para a tabela de usuários

def insert_usuario(name, id_user, user_name, email):
    """
    Insere um novo usuário na tabela, somente se o id_user não existir.

    Args:
        name (str): Nome da tabela e do banco de dados.
        id_user (str): Identificador único do usuário.
        user_name (str): Nome do usuário.
        email (str): Email do usuário.
    """
    db_file = f"{name}.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f"SELECT id_user FROM {name} WHERE id_user = ?", (id_user,))
    if cursor.fetchone():
        st.write("Erro: id_user já existe. O usuário não foi inserido.")
    else:
        cursor.execute(f"INSERT INTO {name} (id_user, name, email) VALUES (?, ?, ?)", (id_user, user_name, email))
        conn.commit()
        st.write("Usuário inserido com sucesso.")
    conn.close()

def update_usuario(name, id_user, new_user_name, new_email):
    """
    Atualiza os dados do usuário na tabela.

    Args:
        name (str): Nome da tabela e do banco de dados.
        id_user (str): Identificador do usuário a ser atualizado.
        new_user_name (str): Novo nome do usuário.
        new_email (str): Novo email do usuário.
    """
    db_file = f"{name}.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {name} SET name = ?, email = ? WHERE id_user = ?", (new_user_name, new_email, id_user))
    conn.commit()
    conn.close()
    st.write("Dados do usuário atualizados com sucesso.")

def delete_usuario(name, id_user):
    """
    Deleta um usuário da tabela.

    Args:
        name (str): Nome da tabela e do banco de dados.
        id_user (str): Identificador do usuário a ser deletado.
    """
    db_file = f"{name}.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {name} WHERE id_user = ?", (id_user,))
    conn.commit()
    conn.close()
    st.write("Usuário deletado com sucesso.")

# ---------------------------------------------------------------------------------
# Funções CRUD para a tabela de compras

def insert_compra(name, curso, id_user, id_curso, finalizado):
    """
    Insere uma nova compra na tabela.

    Args:
        name (str): Nome da tabela e do banco de dados.
        curso (str): Nome do curso.
        id_user (str): Id do usuário.
        id_curso (int): Id do curso.
        finalizado (int): Estado da compra (0 para não, 1 para sim).
    """
    db_file = f"{name}.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {name} (curso, id_user, id_curso, finalizado) VALUES (?, ?, ?, ?)",
                   (curso, id_user, id_curso, finalizado))
    conn.commit()
    conn.close()
    st.write("Compra inserida com sucesso.")

def update_compra(name, id, curso, id_user, id_curso, finalizado):
    """
    Atualiza os dados de uma compra na tabela.

    Args:
        name (str): Nome da tabela e do banco de dados.
        id (int): Id da compra a ser atualizada.
        curso (str): Nome do curso.
        id_user (str): Id do usuário.
        id_curso (int): Id do curso.
        finalizado (int): Estado da compra (0 para não, 1 para sim).
    """
    db_file = f"{name}.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {name} SET curso = ?, id_user = ?, id_curso = ?, finalizado = ? WHERE id = ?",
                   (curso, id_user, id_curso, finalizado, id))
    conn.commit()
    conn.close()
    st.write("Compra atualizada com sucesso.")

def delete_compra(name, id):
    """
    Deleta uma compra da tabela.

    Args:
        name (str): Nome da tabela e do banco de dados.
        id (int): Id da compra a ser deletada.
    """
    db_file = f"{name}.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {name} WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    st.write("Compra deletada com sucesso.")

# ---------------------------------------------------------------------------------
# Funções CRUD para a tabela de cursos (utilizando o campo cod_curso)

def insert_curso(name, curso, descricao, preco):
    """
    Insere um novo curso na tabela.

    Args:
        name (str): Nome da tabela e do banco de dados.
        curso (str): Nome do curso.
        descricao (str): Descrição do curso.
        preco (float): Preço do curso.
    """
    db_file = f"{name}.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {name} (curso, descricao, preco) VALUES (?, ?, ?)", (curso, descricao, preco))
    conn.commit()
    conn.close()
    st.write("Curso inserido com sucesso.")

def update_curso(name, cod_curso, curso, descricao, preco):
    """
    Atualiza os dados de um curso na tabela.

    Args:
        name (str): Nome da tabela e do banco de dados.
        cod_curso (int): Código do curso a ser atualizado.
        curso (str): Nome do curso.
        descricao (str): Descrição do curso.
        preco (float): Preço do curso.
    """
    db_file = f"{name}.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {name} SET curso = ?, descricao = ?, preco = ? WHERE cod_curso = ?",
                   (curso, descricao, preco, cod_curso))
    conn.commit()
    conn.close()
    st.write("Curso atualizado com sucesso.")

def delete_curso(name, cod_curso):
    """
    Deleta um curso da tabela.

    Args:
        name (str): Nome da tabela e do banco de dados.
        cod_curso (int): Código do curso a ser deletado.
    """
    db_file = f"{name}.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {name} WHERE cod_curso = ?", (cod_curso,))
    conn.commit()
    conn.close()
    st.write("Curso deletado com sucesso.")

# ---------------------------------------------------------------------------------
# Funções para exibir os dados das tabelas

def display_usuarios(name):
    """
    Exibe todas as linhas da tabela de usuários como um DataFrame.

    Args:
        name (str): Nome do banco de dados (sem extensão) e da tabela.
    """
    try:
        df = get_db_as_dataframe(name)
        st.write("Dados da tabela de usuários:")
        st.dataframe(df)
    except Exception as e:
        st.error(e)

def display_compras(name):
    """
    Exibe todas as linhas da tabela de compras como um DataFrame.

    Args:
        name (str): Nome do banco de dados (sem extensão) e da tabela.
    """
    try:
        df = get_db_as_dataframe(name)
        st.write("Dados da tabela de compras:")
        st.dataframe(df)
    except Exception as e:
        st.error(e)
def display_compras_filtrada(name, id_usuario=None):
    """
    Exibe todas as linhas da tabela de compras como um DataFrame, 
    opcionalmente filtrando pelos registros do usuário especificado.

    Args:
        name (str): Nome do banco de dados (sem extensão) e da tabela.
        id_usuario (str, opcional): Se fornecido, exibe apenas os registros onde id_user equivale a este valor.
    """
    try:
        conn = connect_db(name)
        if conn is None:
            raise Exception("Erro ao conectar ao banco de dados")
        
        if id_usuario:
            query = f"SELECT * FROM {name} WHERE id_user = ?"
            df = pd.read_sql_query(query, conn, params=(id_usuario,))
        else:
            query = f"SELECT * FROM {name}"
            df = pd.read_sql_query(query, conn)
        
        conn.close()
        st.write("Dados da tabela de compras:")
        st.dataframe(df)
    except Exception as e:
        st.error(e)


def display_cursos(name):
    """
    Exibe todas as linhas da tabela de cursos como um DataFrame.

    Args:
        name (str): Nome do banco de dados (sem extensão) e da tabela.
    """
    try:
        df = get_db_as_dataframe(name)
        st.write("Dados da tabela de cursos:")
        st.dataframe(df)
    except Exception as e:
        st.error(e)
