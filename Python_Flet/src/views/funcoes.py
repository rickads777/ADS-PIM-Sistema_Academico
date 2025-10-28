import flet as ft

#Variáveis de Controle
#Variáveis de controle

def Login( page: ft.Page, nome: ft.TextField, senha : ft.TextField):

    if nome.value != "admin":
        nome.error_text="Usuário Não Existe"
    elif senha.value != "admin":
        senha.error_text = "Senha Incorreta"
    else:
        page.go("/admin/home")


#Abre ou fecha a sidebar
def controle_Sidebar(page: ft.Page, sidebar:  ft.NavigationRail): 
    sidebar.visible = not sidebar.visible
    page.update()


