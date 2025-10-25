import flet as ft
from flet import RouteChangeEvent, View, ViewPopEvent

#Importando as View
from .Views import Views

class Router:

    def __init__(self, page: ft.Page):
        self.page = page
        self.pgs = Views(self.page)

    def route_change(self):
        self.page.views.clear()

        #Dicionario de endereços(Routes: View atrelada)
        self.routes = { 
            "/": self.pgs.LoginView(),
            "/home": self.pgs.HomeView(),
        }

        #Puxar do dicionário o Route da pagina indicada
        self.page.views.append(self.routes.get(self.page.route))
        self.page.update()