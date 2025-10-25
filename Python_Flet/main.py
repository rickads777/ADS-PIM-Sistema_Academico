import flet as ft

nomeApp = "EducaZone"

def main(page: ft.Page):
    page.title = nomeApp
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    field_Usuario = ft.TextField(hint_text="Usuário")
    field_Senha = ft.TextField(hint_text="Senha")


    campo_Principal = ft.Row( #Linha (Campo) onde ficará disposto os elementos do login
        controls=[
            ft.Column(#Coluna, 1 em cima do outro
                [
                    field_Usuario,
                    field_Senha,
                    ft.Row(
                        [
                            ft.FilledButton(text="Logar", expand=True),
                            ft.FilledButton(text="Esqueci a senha", expand=True)
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,

    )
  
    
    #Capturar altura e largura do app
    WIDTH: int = page.width
    HEIGHT: int = page.height  
    #adcionar elementos na página
    page.add(campo_Principal)
ft.app(target=main)