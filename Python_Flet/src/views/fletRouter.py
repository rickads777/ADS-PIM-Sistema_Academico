import flet as ft
from flet import RouteChangeEvent, View, ViewPopEvent

#Importando as Views(Páginas)
from .Views import *

#Gerenciar e realizar Routing dos Endereços(Routes)
class Router:
    
    def __init__(self, page: ft.Page):
        self.page = page
        #Views(Pags) como objs N Erro no botão de voltar
        # self.pgs = Views(self.page) 
        # self.adm_Pgs = views_Adm(self.page)
        # self.aluno_pgs = views_aluno(self.page)
        # self.prof_pgs = views_Professor(self.page)
        self.Sidebar_normal = Sidebar(self.page)
        self.sideAdmin = sidebarAdmin(self.page)
        self.sideAluno = sidebarAluno(self.page)
        self.sideProf = sidebarProf(self.page)
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
        #Puxar do dicionário a pagina atrelada ao Route indicado e coloca-la nas views
        #self.page.views.append(self.routes.get(self.page.route))
        troute = TemplateRoute(self.page.route) #Pega a rota por um template, para pegar ids diferentes etc

        if self.page.route == "/": #Limpar as telas num logout
            self.page.views.clear()

        match self.page.route:
            case "/": self.page.views.append(Views(self.page, self.Sidebar_normal).LoginView())
            case "/admin/home": self.page.views.append(views_Adm(self.page, self.sideAdmin).HomeView())
            case "/admin/professores": self.page.views.append(views_Adm(self.page, self.sideAdmin).tabProfessores_View())
            case "/admin/alunos": self.page.views.append(views_Adm(self.page, self.sideAdmin).tabAlunos_View())
            case "/admin/turmas": self.page.views.append(views_Adm(self.page, self.sideAdmin).tabTurmas_View())
            case "/aluno/home": self.page.views.append(views_aluno(self.page, self.sideAluno).HomeView())
            case "/prof/home": self.page.views.append(views_Professor(self.page, self.sideProf).HomeView())
            case _:
                if troute.match("/admin/turmas/:id"): self.page.views.append(views_Adm(self.page, self.sideAdmin).detalheTurma_view(troute.id))
                else:
                    pass
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