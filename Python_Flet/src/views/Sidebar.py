import flet as ft
from flet import *

#Sidebar é uma navrail no flet
class Sidebar(): 
    def __init__(self, page: ft.Page):
        self.rail = NavigationRail( #Sidebar padrão para todos os tipos de usuário
            #extended=True,
            min_width=100,
            min_extended_width=400,
            label_type= NavigationRailLabelType.ALL, #
            leading=FloatingActionButton(icon=Icons.CREATE, text="criar"), #control principal
            group_alignment=-0.9, #Distância entre os objetos dentro do grupo (acho)
            destinations=[ 
                ft.NavigationRailDestination(
                    icon = Icons.FAVORITE_BORDER, 
                    selected_icon=Icons.FAVORITE, 
                    label_content=ft.Text("Nome"),
                    label="favorito"
                )
            ],
            bgcolor="blue"
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

    def rtnSide(self):
        return super().rtnSide()
    
class sidebarAdmin(Sidebar):
    def __init__(self, page):
        super().__init__(page)
    
    def rtnSide(self):
        return super().rtnSide()
    
