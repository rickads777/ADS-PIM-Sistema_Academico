import flet as ft
import  time
from .funcoes import *
from .Sidebar import *
from .customControls import *
#Todas as Páginas
#Ver se essas são padrões e criar classes filhas que herdam isso e adicionam o específico
#Views_prof, views_aluno etc


class Views:
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.content: ft.View #Páginas retornadas
        self.body: ft.Row #Corpo das views
        self.sidebar: ft.Container #Sidebar que será retornada
        
        #botão de colapsar a sidebar 
        def toggle_sidebar(e): #função pro click
            self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
            controle_Sidebar(self.page, self.sidebar)

        self.toggle_nav_rail_button = ft.IconButton(
            icon=ft.Icons.ARROW_CIRCLE_LEFT,
            icon_color=ft.Colors.BLUE_GREY_400,
            selected=False,
            selected_icon=ft.Icons.ARROW_CIRCLE_RIGHT,
            on_click=toggle_sidebar
        )

        #atributos da home
        self.homeColunm: ft.Column = ft.Column()
        self.homeTopo: ft.Row = ft.Row()
        self.homeMeio: ft.Row = ft.Row()
        self.homeFim: ft.Row = ft.Row()

    #funcoes para os btns


    #Páginas(Views)

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

        self.content = ft.View(
            #route="/home", Inserir separada nas filhas
                    controls=[
                        
                    ],
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    
        )
        #Estrutura padrão da Home
        self.homeTopo = ft.Row(
                            [
                                ft.ElevatedButton(
                                    text="<<",
                                    on_click=lambda _:self.page.go("/"), #Precisa chamar a função pop_view
                                    bgcolor="blue",
                                    color="white"
                                )
                            ],
                            alignment=ft.MainAxisAlignment.END,
                            
                        )

        #Define o corpo da página
        self.body = ft.Row(
            [
                 
                ft.Column(
                    [
                        self.toggle_nav_rail_button
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),

                ft.Column(width=30), #Margem entre navrail e coluna

                ft.Column(
                    [
                        #topo (btn retornar)
                        self.homeTopo,                 
                        #Meio para os cards  
                        self.homeMeio,
                        #final
                        self.homeFim
                    ],
                    expand=True
                ),
            ],expand=True

        )
        self.content.controls.append(self.body) #add corpo a view    
    

class views_Adm(Views):

    def __init__(self, page):
        super().__init__(page)
        self.sidebar = sidebarAdmin(self.page).rtnSide() #Recebe o navRail de Adm
        


    def HomeView(self):
        super().HomeView()#Chama a estrutura padrão
        
        self.body.controls.insert(0, self.sidebar) #Adiciona sidebar primeiro
        
        #Função para abrir o cadastro
        def abrirCadastro(e):
            if ctnCadastro.content.visible:
                #ctnCadastro.width = 0
                ctnCadastro.content.height = 0
                self.page.update()
                ctnCadastro.content.visible = not ctnCadastro.content.visible
                time.sleep(0.5)#Esperar o tempo da animação
                self.page.update()
            else:
                ctnCadastro.content.visible = not ctnCadastro.content.visible
                listTurmas = select_DB("Turma","idTurma,nome")
                ctnCadastro.drpTurmas.options = None
                for i, turma in enumerate(listTurmas): #For com Index
                    ctnCadastro.drpTurmas.options.append(
                        ft.DropdownOption(
                            key=turma[i],
                            text=turma[i + 1]
                        )
                    )  
                self.page.update()
                time.sleep(0.1)#Pequeno delay pra animação poder começar
                ctnCadastro.muda_Drop(e)
                #ctnCadastro.width = 320
                self.page.update()
                
        
        #Container que será aberto no click do cadastro
        ctnCadastro = caixaCadastros(self.page)
        ctnCadastro.content.visible = False
        
        #Adicona os cards no home view
        self.homeMeio.controls.append(homeCard(ft.Icons.SCHOOL,"Professores")) 
        self.homeMeio.controls.append(homeCard(ft.Icons.GROUP,"Alunos"))
        self.homeFim.controls.append(
            ft.Column(
                [
                    ft.FilledTonalButton(
                        content=ft.Row([
                        ft.Icon(name=ft.Icons.PERSON_ADD),
                        ft.Text("Cadastrar Usuários"),
                    ]),
                    on_click=abrirCadastro),
                    ctnCadastro.content
                ]
            )
        )
        self.content.route = "/admin/home"
        
        return self.content
    
class views_aluno(Views):
    def __init__(self, page):
        super().__init__(page)
        self.sidebar = sidebarAluno(self.page).rtnSide() #Recebe o navRail de Aluno

    def HomeView(self):
        super().HomeView()
        self.body.controls.insert(0, self.sidebar) #Adiciona sidebar primeiro
        self.homeMeio.controls.append(homeCard(ft.Icons.INSERT_CHART,"Notas")) 
        self.homeMeio.controls.append(homeCard(ft.Icons.LIBRARY_BOOKS,"Atividades"))
        self.content.route = "/aluno/home"
        return self.content
    
class views_Professor(Views):

    def __init__(self, page):
        super().__init__(page)
        self.sidebar = sidebarProf(self.page).rtnSide()

    def HomeView(self):
        super().HomeView()
        self.body.controls.insert(0, self.sidebar) #Adiciona sidebar primeiro
        self.homeMeio.controls.append(homeCard(ft.Icons.CO_PRESENT,"Aulas")) 
        self.homeMeio.controls.append(homeCard(ft.Icons.POST_ADD,"Atividades"))
        self.content.route = "/prof/home"
        return self.content
