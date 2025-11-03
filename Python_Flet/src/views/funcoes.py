import flet as ft
from .conexao  import *

#Variáveis de controle

def Login( page: ft.Page, nome: ft.TextField, senha : ft.TextField):
    
    if nome.value == "admin":
        if senha.value != "admin":
            senha.error_text = "Senha Incorreta"
        else:
            page.go("/admin/home")

    elif nome.value == "aluno":
        if senha.value != "aluno":
            senha.error_text = "Senha Incorreta"
        else:
            page.go("/aluno/home")
    elif nome.value == "prof":
        if senha.value != "prof":
            senha.error_text = "Senha Incorreta"
        else:
            page.go("/prof/home")
    else:
        nome.error_text="Usuário Não Existe"
    nome.value =""
    senha.value=""


#Abre ou fecha a sidebar
def controle_Sidebar(page: ft.Page, sidebar:  ft.Container): 
    #Tirar o ctn da sidebar de posição
    if sidebar.offset == (0,0):
        sidebar.offset = (-3,0)
    else:
        sidebar.offset = (0,0)
    #Diminuir/Aumentar o tamanho para que a página se ajuste ao lugar
    sidebar.width = 0 if sidebar.width == 120 else 120 
    #Fazer o ctn da Sidebar desaparecer antes de ficar estranho o texto
    sidebar.opacity = 0 if sidebar.opacity == 1.0 else 1.0 
    page.update()


#Admin
##Cadastrar Usuários

def cadastrar_Usuario(tipo: str, nome, usuario, senha, email):
    comando = f'INSERT INTO {tipo.lower()} (nome, usuario, senha, email) VALUES ("{nome}", "{usuario}", "{senha}", "{email}")'
    cursor.execute(comando)
    connection.commit()