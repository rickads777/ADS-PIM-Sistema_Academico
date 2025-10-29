import flet as ft
import config
#Variáveis de Controle
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
    else:
        nome.error_text="Usuário Não Existe"



#Abre ou fecha a sidebar
def controle_Sidebar(page: ft.Page, sidebar:  ft.NavigationRail): 
    sidebar.visible = not sidebar.visible
    page.update()


