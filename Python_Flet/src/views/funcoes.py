import flet as ft
from .conexao  import *

#Variáveis de controle

def Login( page: ft.Page, nome: ft.TextField, senha : ft.TextField):

    #Teste se caractere identificador existe, e então procuta na tabela específica
    if nome.value.find("R") == 0: #Se admin
        if senha.value != select_Senha("admin", nome.value):
            senha.error_text = "Senha Incorreta"
        else:
            page.go("/admin/home")

    elif nome.value.find("A") == 0:#Se aluno
        if senha.value != select_Senha("aluno", nome.value):
            senha.error_text = "Senha Incorreta"
        else:
            page.go("/aluno/home")
    elif nome.value.find("P") == 0:#Se aluno
        if senha.value != select_Senha("professor", nome.value):
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

def cadastrar_Usuario(tipo: str, nome, usuario, senha, email, idturma = None, lstMaterias = None, idProfessor = None):
    if idturma != None:
        generic_Comitable(f'INSERT INTO {tipo.lower()} (nome, usuario, senha, email, idTurma) VALUES ("{nome}", "{usuario}", "{senha}", "{email}", {int(idturma)})')
    elif lstMaterias != None: # Professor sendo cadastrado
        generic_Comitable(f'INSERT INTO {tipo.lower()} (nome, usuario, senha, email) VALUES ("{nome}", "{usuario}", "{senha}", "{email}")')
        for materia in lstMaterias:
            generic_Comitable(f'INSERT INTO Professor_Materia (idprofessor, idmateria) VALUES ({idProfessor}, {materia})')

    else:
        generic_Comitable(f'INSERT INTO {tipo.lower()} (nome, usuario, senha, email) VALUES ("{nome}", "{usuario}", "{senha}", "{email}")')