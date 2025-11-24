import flet as ft
import  time
from .funcoes import *
from .Sidebar import *
from .customControls import *
#Todas as Páginas
#Ver se essas são padrões e criar classes filhas que herdam isso e adicionam o específico
#Views_prof, views_aluno etc


class Views:
    
    def __init__(self, page: ft.Page, sidebar: Sidebar):
        self.page = page
        self.content: ft.View #Páginas retornadas
        self.body: ft.Row #Corpo das views
        self.sidebar: Sidebar = sidebar #Sidebar que será retornada 
        
        #botão de colapsar a sidebar 
        def toggle_sidebar(e): #função pro click
            self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
            controle_Sidebar(self.page, self.sidebar.ctn)

        self.toggle_nav_rail_button = ft.IconButton(
            icon=ft.Icons.ARROW_CIRCLE_LEFT,
            icon_color=ft.Colors.BLUE_GREY_400,
            selected=False,
            selected_icon=ft.Icons.ARROW_CIRCLE_RIGHT,
            on_click=toggle_sidebar
        )
        

        #Atributos da home
        #self.homeColunm: ft.Column = ft.Column()
        self.homeTopo: ft.Row = ft.Row()
        self.homeMeio: ft.Row = ft.Row()
        self.homeFim: ft.Row = ft.Row()
        
        #Atributos das TableViews
        self.Tabela: ft.DataTable

    #funcoes para os btns
    def view_pop(self, e: ViewPopEvent): #Voltar a páginas/ Testar melhor quando tiver mais
            try:
                self.page.views.pop() #Remove pag atual
                topView: View = self.page.views[-1]
                #self.page.views.clear()
                self.page.go(topView.route) #Pega a rota da anterior e vai
                self.page.views.pop() #Remove a página da qual ele pega a rota(a anterior) para que não tenha duplicatas
            except:
                self.page.go("/")

    #Páginas(Views)

    #Página de Login
    def LoginView(self):

        #campos e variáveis
        field_Usuario = ft.TextField(hint_text="Usuário", prefix_icon=ft.Icons.PERSON, autofocus=True)
        field_Senha = ft.TextField(hint_text="Senha",prefix_icon=ft.Icons.LOCK, password=True)

        
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
        self.homeMeio.controls.clear()
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
                                    on_click=self.view_pop, #Precisa chamar a função pop_view
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
        self.sidebar.rail.selected_index = 0
        self.body.controls.insert(0, self.sidebar.ctn) #Adiciona sidebar primeiro
        self.content.controls.append(self.body) #add corpo a view    
    #Páginas de mostrar Tabelas
    def TableView(self):
        self.HomeView()
        self.homeMeio.controls = [self.Tabela]
        self.homeFim.controls = None



class views_Adm(Views):

    def __init__(self, page, sidebar):
        super().__init__(page, sidebar)
        #Adiciona a sidebar específica
        self.sidebar =sidebarAdmin(self.page) #Recebe o navRail de Adm
        


    def HomeView(self):
        super().HomeView()#Chama a estrutura padrão
        
        #Função para abrir o cadastro
        def abrirCadastro(e):
            if ctnCadastro.content.visible:
                ctnCadastro.content.height = 0
                self.page.update()
                ctnCadastro.content.visible = not ctnCadastro.content.visible
                time.sleep(0.5)#Esperar o tempo da animação
                self.page.update()
            else:
                ctnCadastro.content.visible = not ctnCadastro.content.visible
                listTurmas = select_DB("Turma","idTurma,nome")
                ctnCadastro.maior_idProfessor = select_Next_Increment("professor")
                ctnCadastro.maior_idAdmin = select_Next_Increment("admin")
                ctnCadastro.maior_idAluno = select_Next_Increment("aluno")
                ctnCadastro.drpTurmas.options = []
                for id, turma in listTurmas: 
                    ctnCadastro.drpTurmas.options.append(
                        ft.DropdownOption(
                            key=id,
                            text=turma
                        )
                    )  
                self.page.update()
                time.sleep(0.1)#Pequeno delay pra animação poder começar
                ctnCadastro.muda_Drop(e)
                #ctnCadastro.width = 320
                self.page.update()
        def abrirCadastro_Turmas(e):
            if ctnCad_Turma.content.visible:
                ctnCad_Turma.content.height = 0
                self.page.update()
                time.sleep(0.5)
                ctnCad_Turma.content.visible = not ctnCad_Turma.content.visible
            else:
                ctnCad_Turma.content.visible = not ctnCad_Turma.content.visible
                self.page.update()
                time.sleep(0.1)
                ctnCad_Turma.content.height = 190
            self.page.update()
        
        #Container que será aberto no click do cadastro
        ctnCadastro = caixaCadastros(self.page)
        ctnCadastro.content.visible = False

        #Container de cadastro das turmas
        ctnCad_Turma = cxCadastro_Turma(self.page)
        ctnCad_Turma.content.visible = False
        
        #Adicona os cards no home view
        self.homeMeio.controls.append(homeCard(ft.Icons.SCHOOL,"Professores", self.page, "/admin/professores", self.sidebar.rail, 2)) 
        self.homeMeio.controls.append(homeCard(ft.Icons.GROUP,"Alunos", self.page, "/admin/alunos", self.sidebar, 3))
        self.homeMeio.controls.append(homeCard(ft.Icons.CLASS_,"Turmas",self.page,"/admin/turmas",self.sidebar,0))
        self.homeFim.controls.append(
            ft.Column(
                [
                    ft.FilledTonalButton(
                        content=ft.Row([
                        ft.Icon(name=ft.Icons.PERSON_ADD),
                        ft.Text("Cadastrar Usuários"),
                    ], alignment=ft.MainAxisAlignment.CENTER 
                    ),
                    on_click=abrirCadastro),
                    ctnCadastro.content
                ],
                height=400,
                width=290
            )
        )
        self.homeFim.controls.append(
            ft.Column(
                [
                    ft.FilledTonalButton(
                        content=ft.Row([
                        ft.Icon(name=ft.Icons.PERSON_ADD),
                        ft.Text("Cadastrar Turma"),
                    ]),
                    on_click=abrirCadastro_Turmas),
                    ctnCad_Turma.content
                ],height=400,
            )
        )
        self.content.route = "/admin/home"
        
        return self.content
    
    def tabProfessores_View(self):
        tbProf = Tab_profs(self.page,"Professor", ["RP", "Nome", "Email", " Senha", "Materias"], "idprofessor, usuario, nome, senha, email")
        self.Tabela = tbProf.Tab
        
        #chama a construção padrão
        super().TableView()
        self.sidebar.rail.selected_index = 2
        self.content.route ="/admin/professores"
        return self.content
    
    def tabAlunos_View(self):
        tbAluno = Tab_alunos(self.page,"aluno",["RA","Nome", "Email", " Senha","Turma"],"usuario,nome,senha,email,idturma")
        self.Tabela = tbAluno.Tab
        super().TableView()
        self.sidebar.rail.selected_index = 3
        self.content.route ="/admin/alunos"
        return self.content
    
    def tabTurmas_View(self):
        tbTurma = Tab_Turmas(self.page,"turma",["ID","Nome","Periodo","Ano de Início"],"idturma,nome,periodo,anoinicio") 
        self.Tabela = tbTurma.Tab
        super().TableView()
        self.content.route ="/admin/turmas"
        return self.content

class views_aluno(Views):
    def __init__(self, page, sidebar):
        super().__init__(page, sidebar)
        self.sidebar = sidebarAluno(self.page) #Recebe o navRail de Aluno

    def HomeView(self):
        super().HomeView()
        self.homeMeio.controls.append(homeCard(ft.Icons.INSERT_CHART,"Notas")) 
        self.homeMeio.controls.append(homeCard(ft.Icons.LIBRARY_BOOKS,"Atividades"))
        self.content.route = "/aluno/home"
        return self.content
    
class views_Professor(Views):

    def __init__(self, page, sidebar):
        super().__init__(page, sidebar)
        self.sidebar = sidebarProf(self.page)

    def HomeView(self):
        super().HomeView()
        self.homeMeio.controls.append(homeCard(ft.Icons.CO_PRESENT,"Aulas")) 
        self.homeMeio.controls.append(homeCard(ft.Icons.POST_ADD,"Atividades"))
        self.content.route = "/prof/home"
        return self.content
