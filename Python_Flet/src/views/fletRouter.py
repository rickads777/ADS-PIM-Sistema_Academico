import flet as ft
from flet import RouteChangeEvent, View, ViewPopEvent

#Importando as Views(Páginas)
from .Views import *

#Gerenciar e realizar Routing dos Endereços(Routes)
class Router:
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.pgs = Views(self.page) #Views(Pags) como objs
        self.list_Pgs = views_Adm(self.page)
        self.teste = views_aluno(self.page)
        #Dicionario de endereços(Routes: View atrelada)
        self.routes = { 
            "/": self.pgs.LoginView(),
            "/home": self.pgs.HomeView(),
            "/admin/home": self.list_Pgs.HomeView(),
            "/aluno/home": self.teste.HomeView(),
        }

    def route_change(self):
        self.page.views.clear()
        #Puxar do dicionário a pagina atrelada ao Route indicado e coloca-la nas views
        self.page.views.append(self.routes.get(self.page.route))
        self.page.update()
        

class Router_Admin(Router):
    def __init__(self, page):
        super().__init__(page)
        self.list_Pgs = views_Adm(self.page)
        #Atuaaliza o > Dicionario de endereços(Routes: View atrelada)
        self.routes = { 
            "/": self.pgs.LoginView(),
            "/home": self.pgs.HomeView(),
            "/admin/home": self.list_Pgs.HomeView(),
        }
        

    def route_change(self):
        return super().route_change()

# TESTANDO
#Routers diferentes para as classes filhas
class Router_Aluno(Router):
    def __init__(self, page):
        super().__init__(page)
        self.list_Pgs = views_aluno(self.page)
        #Dicionario de endereços(Routes: View atrelada)
        self.routes = { 
            "/": self.pgs.LoginView(),
            "/aluno/home": self.list_Pgs.HomeView(),
        }

    def route_change(self):
        self.page.views.clear()

        #Puxar do dicionário a pagina atrelada ao Route indicado e coloca-la nas views
        self.page.views.append(self.routes.get(self.page.route))
        self.page.update()


class Router_Professor(Router):
    def __init__(self, page):
        super().__init__(page)