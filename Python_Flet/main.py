import flet as ft

nomeApp = "EducaZone"

def main(page: ft.Page):
    page.title = nomeApp
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    field_Usuario = ft.TextField(hint_text="Usuário")
    field_Senha = ft.TextField(hint_text="Senha")

    campo_Principal = ft.Column( #Coluna (Campo) onde ficará disposto os elementos do login
        controls=[
            ft.Row(
                controls=[
                    field_Usuario
                ]
            ),
            ft.Row(
                controls=[
                    field_Senha
                ]
            )
        ]
    )
    
    #Capturar altura e largura do app
    WIDTH: int = page.width
    HEIGHT: int = page.height
    
    #adcionar elementos na página
    page.add(campo_Principal)
ft.app(target=main)