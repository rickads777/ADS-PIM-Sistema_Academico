import flet as ft
from flet import RouteChangeEvent, View, ViewPopEvent
from views.fletRouter import Router 

nomeApp = "EducaZone"
        
def main(page: ft.Page):
    page.title = nomeApp
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 80
    router = Router(page)

    #Capturar altura e largura do app
    WIDTH: int = page.width
    HEIGHT: int = page.height
    
    #Controlar Navegação
    def route_change(e: RouteChangeEvent):
        router.route_change()
    
    def view_pop(e: ViewPopEvent): #Voltar a página
        page.views.pop() #Remove pag atual
        topView: View = page.views[-1] 
        page.go(topView.route) #Pega a rota da anterior e vai
        
    
    #adcionar página no app
    page.on_route_change = route_change #definir comportamente quando route for mudado
    page.on_view_pop = view_pop
    page.go(page.route)
    
ft.app(target=main)