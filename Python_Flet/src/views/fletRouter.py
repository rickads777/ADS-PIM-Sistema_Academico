import flet as ft
from flet import RouteChangeEvent, View, ViewPopEvent

#Importando as Views(Páginas)
from .Views import *

#Gerenciar e realizar Routing dos Endereços(Routes)
class Router:
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.pgs = Views(self.page) #Views(Pags) como objs
        self.adm_Pgs = views_Adm(self.page)
        self.aluno_pgs = views_aluno(self.page)
        self.prof_pgs = views_Professor(self.page)
        #Dicionario de endereços(Routes: View atrelada)
        # self.routes = { 
        #     "/": Views(self.page).LoginView(),
        #     "/home": self.pgs.HomeView(),
        #     "/admin/home": views_Adm(self.page).HomeView(),
        #     "/aluno/home": views_aluno(self.page).HomeView(),
        #     "/prof/home": views_Professor(self.page).HomeView(),
        #     "/admin/professores": views_Adm(self.page).tabProfessores_View()
        # }

    def route_change(self):
        self.page.views.clear()
        #Puxar do dicionário a pagina atrelada ao Route indicado e coloca-la nas views
        #self.page.views.append(self.routes.get(self.page.route))
        match self.page.route:
            case "/": self.page.views.append(self.pgs.LoginView())
            case "/admin/home": self.page.views.append(self.adm_Pgs.HomeView())
            case "/admin/professores": self.page.views.append(self.adm_Pgs.tabProfessores_View())
            case "/aluno/home": self.page.views.append(self.aluno_pgs.HomeView())
            case "/prof/home": self.page.views.append(self.prof_pgs.HomeView())
        self.page.update()
        
# TESTANDO
#Routers diferentes para as classes filhas
# class Router_Admin(Router):
#     def __init__(self, page):
#         super().__init__(page)
#         self.list_Pgs = views_Adm(self.page)
#         #Atuaaliza o > Dicionario de endereços(Routes: View atrelada)
#         self.routes = { 
#             "/": self.pgs.LoginView(),
#             "/home": self.pgs.HomeView(),
#             "/admin/home": self.list_Pgs.HomeView(),
#         }
        

#     def route_change(self):
#         return super().route_change()


# class Router_Aluno(Router):
#     def __init__(self, page):
#         super().__init__(page)
#         self.list_Pgs = views_aluno(self.page)
#         #Dicionario de endereços(Routes: View atrelada)
#         self.routes = { 
#             "/": self.pgs.LoginView(),
#             "/aluno/home": self.list_Pgs.HomeView(),
#         }

#     def route_change(self):
#         self.page.views.clear()

#         #Puxar do dicionário a pagina atrelada ao Route indicado e coloca-la nas views
#         self.page.views.append(self.routes.get(self.page.route))
#         self.page.update()


# class Router_Professor(Router):
#     def __init__(self, page):
#         super().__init__(page)