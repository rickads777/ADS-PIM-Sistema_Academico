import flet as ft
from .funcoes import *
from config import cxCadastro_maxHeight

#Home Controls

#body
def homeCard(icone: ft.Icons, nome):
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
            )
    return card

class caixaCadastros():
    def __init__(self, page :ft.Page):    
        self.page = page
        # TextFields
        self.fldNome = ft.TextField(label="Nome",)
        self.fldUsuario = ft.TextField(label="Usuário")
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
        self.caixaCadastro = ft.Row([
                ft.Column([
                    self.fldNome,
                    self.fldUsuario,
                    self.fldSenha,
                    self.fldEmail,
                    self.drpTurmas,
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
            field.value = ""
            field.border_color = ft.Colors.WHITE
        self.drpUsuario.value = ""
        self.drpUsuario.border_color = ft.Colors.WHITE
        self.drpTurmas.border_color = ft.Colors.WHITE
        self.page.update()
    ## Salvar
    def Salvar(self,e):
        verficacao = False #Controle de se existe algo nulo
        for field in self.fields:
            if field.value == '':
                field.border_color = ft.Colors.RED
                verficacao = True 
        if self.drpUsuario.value == '' or None:
            verficacao = True
            self.drpUsuario.border_color = ft.Colors.RED
        if self.drpUsuario.value == "Aluno" and self.drpTurmas.value == None:
            verficacao = True
            self.drpTurmas.border_color = ft.Colors.RED
        if verficacao:
            self.page.update()
            return
        else:
            cadastrar_Usuario(self.drpUsuario.value, self.fldNome.value, self.fldUsuario.value, self.fldSenha.value, self.fldEmail.value, self.drpTurmas.value)
            self.Limpar(e)
    # Função on_change
    ## Mostrar Turmas
    def muda_Drop(self, e):
        if self.drpUsuario.value == "Aluno":
            self.content.height =355
            self.drpTurmas.visible = True
        else:
            self.content.height =300
            self.drpTurmas.visible = False
            self.drpTurmas.value = None
        self.page.update()

    def retornaCtnCadastro(self):
        return self.content
#Sidebar Controls

#navRailDestination
def sideDestination(icone: ft.Icons, rota, texto):
    cor = ft.Colors.WHITE

    nav = ft.NavigationRailDestination(
                icon=ft.Icon(name=icone),
                label=rota,
                label_content=ft.Text(value=texto, color=cor),
                selected_icon=ft.Icon(name=icone, color=cor),

            )
    return nav