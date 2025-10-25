import flet as ft
from flet import RouteChangeEvent, View, ViewPopEvent

nomeApp = "EducaZone"
        
def main(page: ft.Page):
    page.title = nomeApp
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 80
  
    field_Usuario = ft.TextField(hint_text="Usuário", prefix_icon=ft.Icons.PERSON)
    field_Senha = ft.TextField(hint_text="Senha",prefix_icon=ft.Icons.LOCK)
    #Capturar altura e largura do app
    WIDTH: int = page.width
    HEIGHT: int = page.height  
    
    #Controlar Navegação
    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()
        
        #Login View
        page.views.append(
            View(
                route="/",
                controls=[
                    ft.Row(#"Container" dos elementos
                        [
                            ft.Column(#Coluna, 1 em cima do outro
                                [
                                    ft.Text(value=f"Boas Vindas ao {nomeApp}!\nSua classe digital", size=25),
                                    field_Usuario,
                                    field_Senha,
                                    ft.Row(
                                        [
                                            ft.FilledButton(text=">", expand=True, on_click=lambda _:page.go("/home")), #Vai pra pag inicial
                                        ], 
                                    )
                                ],
                                spacing=25,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            ft.Column(
                            [
                                ft.Icon(name = ft.Icons.SQUARE, size=400)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                        ],
                        expand=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                        
                ],
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.CENTER,
            )    
        )
        
        #Home View
        if page.route =="/home":
            page.views.append(
                View(
                    route="/home",
                    controls=[
                        ft.ElevatedButton("Voltar", on_click=lambda _:page.go("/"))
                    ],
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    
                )
            )
        page.update()
    
    def view_pop(e: ViewPopEvent): #Voltar a página
        page.views.pop() #Remove pag atual
        topView: View = page.views[-1] 
        page.go(topView.route) #Pega a rota da anterior e vai
    #adcionar elementos na página

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
ft.app(target=main)