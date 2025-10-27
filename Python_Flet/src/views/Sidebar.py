import flet as ft
from flet import *
from .customControls import sideDestination

#Sidebar é uma navrail no flet
class Sidebar(): 
    def __init__(self, page: ft.Page):
        
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


        self.rail = ft.NavigationRail( #Sidebar padrão para todos os tipos de usuário
            #extended=True,
            min_width=100,
            min_extended_width=400,
            label_type= NavigationRailLabelType.ALL, #
            group_alignment=-0.9, #Distância entre os objetos dentro do grupo (acho)
            destinations=[ 
                self.nrdHome,
            ],
            bgcolor="blue",
        )
        
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
    
