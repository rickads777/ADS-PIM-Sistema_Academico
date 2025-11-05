import flet as ft
from flet import *
from .customControls import sideDestination
from .funcoes import controle_Sidebar
#importando variaveis globais
import config

#Sidebar é uma navrail no flet
class Sidebar(): 
    def __init__(self, page: ft.Page):
        self.page = page
        #Setando destinations padrões que terão o label definido nas subclasses
        self.nrdHome = sideDestination( 
            Icons.HOME,
            "" ,
            "Início"
        )

        self.nrdConfigs = sideDestination(
            Icons.SETTINGS,
            "",
            "Configurações"
        )

        #Sidebar padrão para todos os tipos de usuário
        self.rail = ft.NavigationRail( 
            #extended=True,
            min_width=100,
            min_extended_width=120,#I vendo essa distânicia
            label_type= NavigationRailLabelType.ALL, #
            group_alignment=-0.9, #Distância entre o grupo e o topo (acho)
            destinations=[ 
                self.nrdHome.nav,
            ],
            bgcolor="blue",
            on_change=self.changeView,
            selected_index=0 #Testar se vai dar problema isso quando fizer as trocas, acho que não pq teoricamente ela só é construída quando entra pela primeira vez
        )

        #Container da sidebar
        self.ctn = ft.Container(
            content=self.rail,offset=(0,0),
            animate_offset=ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT),
            animate_opacity=ft.Animation(400, ft.AnimationCurve.EASE_IN_OUT_BACK),
            animate=ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT),
            width=120
        )
    def changeView(self,e):
        teste = self.rail.destinations[self.rail.selected_index].label
        self.page.go(teste)
        
    def rtnSide(self):
        ctn = ft.Container(
            content=self.rail,offset=(0,0),
            animate_offset=ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT),
            animate_opacity=ft.Animation(400, ft.AnimationCurve.EASE_IN_OUT_BACK),
            animate=ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT),
            width=120
        )
        return ctn #Retorna a NavRail
    
    
    
#Construção das sidebar_filhas

class sidebarProf(Sidebar): 
    def __init__(self, page):
        super().__init__(page)
        destinations = [
            sideDestination(
                Icons.MENU_BOOK,
                "/prof/biblioteca",
                "Biblioteca",
            ).nav,
            
            sideDestination(
                Icons.MONITOR,
                "/prof/aulas",
                "Aulas",

            ).nav,
            sideDestination(
                Icons.ADD_CHART,
                "/prof/notas",
                "Notas",

            ).nav,
            sideDestination(
                Icons.GROUPS,
                "prof/alunos",
                "Turmas"
            ).nav,
            sideDestination(
                Icons.POST_ADD,
                "prof/atividades",
                "Atividades"
            ).nav,
            self.nrdConfigs.nav
        ]
        for destino in destinations:
            self.rail.destinations.append(destino)
        
    def rtnSide(self):
        return super().rtnSide()

class sidebarAluno(Sidebar):
    def __init__(self, page):
        super().__init__(page)

        destinations = [
            sideDestination(
                Icons.MENU_BOOK,
                "/aluno/biblioteca",
                "Biblioteca",
            ).nav,
            
            sideDestination(
                Icons.MONITOR,
                "/aluno/aulas",
                "Aulas",

            ).nav,
            sideDestination(
                Icons.INSERT_CHART,
                "/aluno/notas",
                "Notas",

            ).nav,
            sideDestination(
                Icons.LIBRARY_BOOKS,
                "/aluno/atividades",
                "Atividades",

            ).nav,
            self.nrdConfigs.nav
        ]
        for destino in destinations:
            self.rail.destinations.append(destino)
            
    def rtnSide(self):
        return super().rtnSide()
    
class sidebarAdmin(Sidebar):
    def __init__(self, page):
        super().__init__(page)
        destinations = [
            sideDestination(
                Icons.ASSIGNMENT_IND,
                "/admin/cadastro",
                "Cadastro").nav,
            sideDestination(
                Icons.SCHOOL,
                "/admin/professores",
                "Professores"
            ).nav,
            sideDestination(
                Icons.GROUPS,
                "admin/alunos",
                "Alunos"
            ).nav,

            self.nrdConfigs.nav
        ]
        for testes in  destinations: #adicionar destinos no rail
            self.rail.destinations.append(testes)
        self.nrdHome.nav.label = "/admin/home"
    
    def rtnSide(self):
        return super().rtnSide()
    
