import streamlit as st
import streamlit.components.v1 as components
from banco.db import insert_usuario,GetIdUser

# Configurações da página
st.set_page_config(
    page_title="Ativa Engenharia",
    page_icon=":bar_chart:",
    layout="wide"  # Define o layout como "wide"
)

def VerificaId(name,id,user,email):
    try:
        insert_usuario(name,id,user,email)
    except:
        print('Usuario já existe!')

def logout():
    st.logout()
    st.rerun()

def login_screen():
    col1,col2,col3 = st.columns([1,2,1],border=True)
    cols1,cols2,cols3 = st.columns([1,2,1])
    col2.image('image.png',use_container_width=True)
    cols2.button("Login Com Google", on_click=st.login,use_container_width=True)
    

# Definindo as páginas com ícones usando Unicode (um único caractere cada)
home = st.Page('home/home.py', title='Home', icon="\U0001F3E0")         # 🏠
cursos1 = st.Page('cursos/cursos1.py', title='Cursos Disponíveis', icon="\U0001F4DA")  # 📚
cursos2 = st.Page('cursos/cursos2.py', title='Meus Cursos', icon="\U0001F393")         # 🎓
logout_page = st.Page(logout, title='Sair', icon="\U0001F6AA")                       # 🚪
contato = st.Page('contato/contato.py', title='Contato', icon="\U0001F4E7")          # 📧
artigos = st.Page('artigos_tecnicos/artigos.py', title='Artigos Técnicos', icon="\U0001F4DD")  # 📝
perfil = st.Page('perfil/perfil.py', title='Perfil', icon='👤')

if not st.experimental_user.is_logged_in:
    #Usuário não está logado!
    login_screen()

else:
    #Usuario está logado!

    #Tentando inserir o novo usuasio(casos seja novo)
    id_user= GetIdUser(st.experimental_user.to_dict()['sub'])
    VerificaId('usuarios',id_user,st.experimental_user.to_dict()['name'],st.experimental_user.to_dict()['email'])
    pg = st.navigation({
        "Home": [home, contato, artigos],
        "Cursos": [cursos1, cursos2],
        "Conta": [perfil,logout_page]
    })
    pg.run()
