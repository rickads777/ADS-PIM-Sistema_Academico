import flet as ft
from .funcoes import Login
from .Sidebar import *

#Todas as Páginas
#Ver se essas são padrões e criar classes filhas que herdam isso e adicionam o específico
#Views_prof, views_aluno etc

class Views:
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.content: ft.View #Páginas retornadas
        self.body: ft.Row #Corpo das views

        #Rows estruturais para Home
        
    
    #Página de Login
    def LoginView(self):

        #campos e variáveis
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

        self.content = ft.View(
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
        return self.content    
    
    #Página Home (Testes)
    def HomeView(self):
        self.body = ft.Row(
            [
                ft.ElevatedButton("Voltar", on_click=lambda _:self.page.go("/"), )
            ], expand=True
        )
        self.content = ft.View(
            #route="/home", Inserir separada nas filhas
                    controls=[
                        self.body
                    ],
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    
        )
        return self.content                   
    

class views_Adm(Views):

    def __init__(self, page):
        super().__init__(page)
        self.sideAdm = sidebarAdmin(self.page).rtnSide() #Recebe o navRail de Adm

    def HomeView(self):
        super().HomeView()
        #Adiciona as partes únicas
        self.body.controls.insert(0,self.sideAdm)
        self.body.controls.append(ft.Text(value="Página de admin"))
        self.content.route = "/admin/home"
        return self.content

 