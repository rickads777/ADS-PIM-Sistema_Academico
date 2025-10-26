import flet as ft
from .funcoes import Login


#Todas as Páginas

class Views:
    def __init__(self, page: ft.Page):
        self.page = page
    
    #Página de Login
    def LoginView(self):
        field_Usuario = ft.TextField(hint_text="Usuário", prefix_icon=ft.Icons.PERSON, autofocus=True)
        field_Senha = ft.TextField(hint_text="Senha",prefix_icon=ft.Icons.LOCK)
        
        #Validar Login
        def click_logar(e):
            Login(self.page, field_Usuario, field_Senha)
            self.page.update()
        
        #Quando pressionar um botão
        def keyboard_press(e: ft.KeyboardEvent):
            if e.key == "Enter": #No enter Loga
                Login(self.page, field_Usuario, field_Senha)
                self.page.update()

        self.page.on_keyboard_event = keyboard_press

        content = ft.View(
                route="/",
                controls=[
                    ft.Row(#"Container" dos elementos
                        [
                            ft.Column(#Coluna, 1 em cima do outro
                                [
                                    ft.Text(value=f"Boas Vindas ao EducaZone!\nSua classe digital", size=25),
                                    field_Usuario,
                                    field_Senha,
                                    ft.Container(
                                        content = ft.FilledButton(text=">", expand=True, on_click=click_logar), #Apenas Referênciar a função
                                        alignment=ft.alignment.center_right,
                                        width=300
                                    )
                                ],
                                spacing=25,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            ft.Column(
                            [
                                ft.Icon(name = ft.Icons.SQUARE, size=400)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                        ],
                        expand=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                        
                ],
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.CENTER,
            )
        return content    
    #Página Home (Testes)
    def HomeView(self):
        content = ft.View(
            route="/home",
                    controls=[
                        ft.ElevatedButton("Voltar", on_click=lambda _:self.page.go("/"))
                    ],
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        return content                   