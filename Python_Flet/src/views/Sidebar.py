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
                self.nrdHome,
            ],
            bgcolor="blue"
        )

        content = ft.Column(
            [
                
            ],
        )
        
        #Coluna que habita a sidebar(Feito pra ter o botão )
        def clickSide_Control(e): #Função pro click
            controle_Sidebar(self.page, self.rail)

        
    def rtnSide(self):
        
        return self.rail #Retorna a NavRail
    
    
    
#Construção das sidebar_filhas

class sidebarProf(Sidebar): 
    def __init__(self, page):
        super().__init__(page)
        self.rail.destinations.append(NavigationRailDestination(),) #Adicionando os destinhos específicos para professor
    
    def rtnSide(self):
        return super().rtnSide()

class sidebarAluno(Sidebar):
    def __init__(self, page):
        super().__init__(page)
        self.rail.destinations.append(
            ft.NavigationRailDestination(
                icon=Icons.MENU_BOOK,
                label_content="Biblioteca",
                label="/aluno/biblioteca",
            )
        )

    def rtnSide(self):
        return super().rtnSide()
    
class sidebarAdmin(Sidebar):
    def __init__(self, page):
        super().__init__(page)
        destinations = [
            sideDestination(
                Icons.ASSIGNMENT_IND,
                "/admin/cadastro",
                "Cadastro"),
            sideDestination(
                Icons.SCHOOL,
                "/admin/professores",
                "Professores"
            ),
            sideDestination(
                Icons.GROUPS,
                "admin/alunos",
                "Alunos"
            ),

            self.nrdConfigs
        ]
        for testes in  destinations: #adicionar destinos no rail
            self.rail.destinations.append(testes)
    
    def rtnSide(self):
        return super().rtnSide()
    
