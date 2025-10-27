import flet as ft
from flet import RouteChangeEvent, View, ViewPopEvent

#Importando as Views(Páginas)
from .Views import *

#Gerenciar e realizar Routing dos Endereços(Routes)
class Router:

    def __init__(self, page: ft.Page):
        self.page = page
        self.pgs = Views(self.page) #Views(Pags) como objs
        self.adm_pgs = views_Adm(self.page)

    def route_change(self):
        self.page.views.clear()

        #Dicionario de endereços(Routes: View atrelada)
        self.routes = { 
            "/": self.pgs.LoginView(),
            "/home": self.pgs.HomeView(),
            "/admin/home": self.adm_pgs.HomeView(),
        }

        #Puxar do dicionário a pagina atrelada ao Route indicado e coloca-la nas views
        self.page.views.append(self.routes.get(self.page.route))
        self.page.update()