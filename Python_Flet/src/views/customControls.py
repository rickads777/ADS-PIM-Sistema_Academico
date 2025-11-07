import flet as ft
from .funcoes import *
from config import cxCadastro_maxHeight

#Home Controls

#body
def homeCard(icone: ft.Icons, nome, page: ft.Page = None, rota = "", sidebar: ft.NavigationRail = None, index_side: int = None):
    #Função click
    def clique(e):
        sidebar.selected_index = index_side
        page.go(rota)
    #Cards para a home
    card = ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Icon(name=icone, color=ft.Colors.WHITE, size=85),
                                    border_radius=100,
                                    bgcolor=ft.Colors.LIGHT_BLUE_900,
                                    alignment= ft.alignment.center,
                                    padding= 10
                                ),
                                
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,

                        ),
                        ft.Row(
                            [
                                ft.Text(value=nome,
                                        text_align=ft.TextAlign.END,
                                        size=20, 
                                        color=ft.Colors.WHITE, 
                                        weight=10)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            
                        )
                    ], 
                    width=100,
                    height=135
                ),
                bgcolor=ft.Colors.LIGHT_BLUE_700,
                padding=20,
                border_radius=10,
                on_click= clique
            )
    return card

class caixaCadastros():
    def __init__(self, page :ft.Page):    
        self.page = page
        # Maiores IDs de cada
        self.maior_idAluno = 0
        self.maior_idProfessor= 0
        self.maior_idAdmin = 0

        # TextFields
        self.fldNome = ft.TextField(label="Nome",)
        self.fldUsuario = ft.TextField(label="Usuário", disabled=True)
        self.fldSenha = ft.TextField(label="Senha",)
        self.fldEmail = ft.TextField(label="E-mail",)
        self.fields = [self.fldNome,self.fldUsuario, self.fldSenha, self.fldEmail]
        ## Estilização dos Fields
        for field in self.fields: 
            field.border_color = ft.Colors.WHITE
            field.bgcolor = ft.Colors.LIGHT_BLUE_800
            field.focused_bgcolor = ft.Colors.LIGHT_BLUE_700
            field.color = ft.Colors.WHITE
            field.label_style = ft.TextStyle(color=ft.Colors.WHITE)
        # Dropdown p/ selecionar usuarios
        ## Opções
        Usuarios = ["Admin","Aluno","Professor"]    
    
        ## Definir Seleções como lista de options q será adicionado
        optUser =[]
        for usuario in Usuarios:
            optUser.append(
                ft.DropdownOption(
                        key=usuario,
                        content=ft.Text(
                            value=usuario,
                        ),
                )
            )
        self.drpUsuario = ft.Dropdown(
            editable=False,
            label="Tipo de Usuário",
            options=optUser,
            on_change= self.muda_Drop,
            border_color= ft.Colors.WHITE,
            color=ft.Colors.WHITE
        )
        #Dropdown para selecionar turmas
        self.drpTurmas: ft.Dropdown = ft.Dropdown(
            label="Turmas",
            enable_filter=True,
            visible=False,
            width=310,
            enable_search=True,
            border_color= ft.Colors.WHITE,
            color=ft.Colors.WHITE
        )
        #Botão de Selecionar matérias
        self.alertMaterias = popEsc_Materia(self.page) #Chama a Classe do PopUp
        self.btnSlct_Materia = ft.TextButton(
            text="Selecionar Materias",
            visible=False,
            width=310,
            on_click=self.alertMaterias.abrirPop_Escolher_Materias
        )
        #Caixa de Cadastro
        self.caixaCadastro = ft.Row([
                ft.Column([
                    self.fldNome,
                    self.fldUsuario,
                    self.fldSenha,
                    self.fldEmail,
                    self.drpTurmas, self.btnSlct_Materia,
                    ft.Row([
                        self.drpUsuario,
                        ft.Row([
                            ft.IconButton(icon=ft.Icons.CHECK_CIRCLE, icon_size=30, icon_color=ft.Colors.LIGHT_BLUE,
                                        on_click= self.Salvar
                                        ),
                            ft.IconButton(icon=ft.Icons.CANCEL,icon_size=30, icon_color=ft.Colors.LIGHT_BLUE,
                                        on_click= self.Limpar
                                        )
                        ], alignment=ft.MainAxisAlignment.CENTER, expand=True
                        )
                    ], expand=True
                    ),
                    
                ], expand=True
                ),
            ],expand=True
        )
        self.content :ft.Container = ft.Container(
            content=self.caixaCadastro,
            bgcolor=ft.Colors.LIGHT_BLUE_900,
            border_radius=5,
            padding=10,
            animate=ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT),
            width=320,
            height=0
        )

    # Funções para o Clique    
    ## Limpar os campos
    def Limpar(self, e):
        for field in self.fields:
            if field.label != "Usuário":
                field.value = ""
            field.border_color = ft.Colors.WHITE
        self.muda_Drop(e)
        self.drpUsuario.border_color = ft.Colors.WHITE
        self.drpTurmas.border_color = ft.Colors.WHITE
        check: ft.Checkbox
        for check in self.alertMaterias.alertBody.controls:
            check.value = False
        self.page.update()
    ## Salvar
    def Salvar(self,e):
        verficacao = False #Controle de se existe algo nulo, se existe é True
        if self.drpUsuario.value == "Aluno" and self.drpTurmas.value == None:
            verficacao = True
            self.drpTurmas.border_color = ft.Colors.RED
        elif self.drpUsuario.value == "Professor":
            check: ft.Checkbox
            for check in self.alertMaterias.alertBody.controls:
                if not check.value:
                    verficacao = True
                else:
                    verficacao = False
                    break
        for field in self.fields:
            if field.value == '':
                field.border_color = ft.Colors.RED
                verficacao = True 
        if self.drpUsuario.value == '' or None:
            verficacao = True
            self.drpUsuario.border_color = ft.Colors.RED
        if verficacao:
            self.page.update()
            return
        else:
            cadastrar_Usuario(self.drpUsuario.value, self.fldNome.value, self.fldUsuario.value, self.fldSenha.value, self.fldEmail.value, self.drpTurmas.value, self.alertMaterias.Materias_Escolhidas, self.maior_idProfessor)
            self.maior_idProfessor = select_Maior("professor","idprofessor")
            self.maior_idAdmin = select_Maior("admin","idadmin")
            self.maior_idAluno = select_Maior("aluno","idaluno")
            self.Limpar(e)
    # Função on_change
    ## Mostrar Turmas
    def muda_Drop(self, e):
        if self.drpUsuario.value == "Aluno":
            self.content.height =355
            self.drpTurmas.visible = True
            self.btnSlct_Materia.visible = False
            self.fldUsuario.value = "A"+(str(self.maior_idAluno + 1))
        elif self.drpUsuario.value == "Professor":
            self.content.height =345
            self.btnSlct_Materia.visible = True
            self.drpTurmas.visible = False
            self.fldUsuario.value = "P"+(str(self.maior_idProfessor + 1))
        elif self.drpUsuario.value == "Admin":
            self.fldUsuario.value = "R"+(str(self.maior_idProfessor + 1))
        else:
            self.content.height =300
            self.drpTurmas.visible = False
            self.btnSlct_Materia.visible = False
            self.fldUsuario.value = None
            
        self.page.update()

    def retornaCtnCadastro(self):
        return self.content

#Pop Up para Prof Escolher materias
class popEsc_Materia:
    def __init__(self, page: ft.Page):
        self.page = page
        self.alertBody= ft.Column(wrap=True, scroll= ft.ScrollMode.AUTO)
        self.popEsc_Mat = ft.AlertDialog(
            title=ft.Text("Selecione as Matérias"),
            actions=[
                ft.TextButton("Confirmar", on_click=self.salvarEscolha_Materias),
                ft.TextButton("Cancelar", on_click=lambda e: self.page.close(self.popEsc_Mat))
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            content= self.alertBody,
            modal=True
        )
        self.Materias_Escolhidas = []
        #Materias puxadas do banco
        self.dbMaterias = {}
        self.select_Materia()

    def select_Materia(self):
        self.dbMaterias.clear()
        Materias = select_Unicos_DB("Materia","nome, idmateria") 
        for materia, id in Materias:
            self.alertBody.controls.append(
                ft.Checkbox(label=materia, value=False)
            )
            self.dbMaterias.update({materia:id})
    
    def abrirPop_Escolher_Materias(self, e):
        self.page.open(self.popEsc_Mat)

    def salvarEscolha_Materias(self, e):
        check:ft.Checkbox
        self.Materias_Escolhidas.clear()
        for check in self.alertBody.controls:
            if check.value:
                self.Materias_Escolhidas.append(self.dbMaterias.get(check.label))
        self.page.close(self.popEsc_Mat)

#Sidebar Controls

#navRailDestination
class sideDestination:
    def __init__(self, icone: ft.Icons, rota, texto):    
        
        self.rota = rota
        self.texto =texto
        self.icone = icone
        cor = ft.Colors.WHITE

        self.nav = ft.NavigationRailDestination(
                    icon=ft.Icon(name=self.icone),
                    label=self.rota,
                    label_content=ft.Text(value=self.texto, color=cor),
                    selected_icon=ft.Icon(name=self.icone, color=cor),

                )

#Tabela Genérica, padrão para as subclasses
class Tabela():
    def __init__(self, nomeTabela: str, colunas: list, linhas: str ):
        self.nomeTabela = nomeTabela
        self.colunas = colunas
        self.colunas.append("") #Adiciona coluna sem nada, pra ficar os botões
        self.linhas = linhas
        self.Tab: ft.DataTable = ft.DataTable (columns=[])
        for coluna in self.colunas:
            self.Tab.columns.append(
                ft.DataColumn(
                    ft.Text(coluna)
                )
            )
        
    

class Tab_profs(Tabela):
    def __init__(self, nomeTabela, colunas, linhas):
        super().__init__(nomeTabela, colunas, linhas)
        self.btnEditar = ft.IconButton(icon=ft.Icons.EDIT)
        self.btnExcluir = ft.IconButton(icon=ft.Icons.DELETE)
        self.criarLinhas()

    def criarLinhas(self):
        #Seleciona as linhas da tabela
        linhas_dtTble = select_DB(self.nomeTabela,self.linhas)

        for id,nome,email in linhas_dtTble:
            materias = generic_Select_DB(f"select m.nome from Materia as m inner join professor_materia as mp on m.idmateria = mp.idmateria inner join professor as p on p.idprofessor = mp.idprofessor where p.idprofessor = {id}")
            mat_prof = ", ".join(f'{materia}'.strip("()\',") for materia in materias)
            
            self.Tab.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(id)),
                        ft.DataCell(ft.Text(nome)),
                        ft.DataCell(ft.Text(email)),
                        ft.DataCell(ft.Text(mat_prof)),
                        ft.DataCell(ft.Row([self.btnEditar, self.btnExcluir]))
                    ]
                )
            )