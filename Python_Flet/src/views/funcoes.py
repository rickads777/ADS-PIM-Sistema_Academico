import flet as ft

def Login( page: ft.Page, nome: ft.TextField, senha : ft.TextField):

    if nome.value != "admin":
        nome.error_text="Usuário Não Existe"
    elif senha.value != "admin":
        senha.error_text = "Senha Incorreta"
    else:
        page.go("/admin/home")