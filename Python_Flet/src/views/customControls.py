import flet as ft

#Home Controls

#body
def homeCard(icone: ft.Icons, nome):
    #Cards para a home
    card = ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Icon(name=icone, color=ft.Colors.WHITE, size=85),
                                    border_radius=100,
                                    bgcolor=ft.Colors.LIGHT_BLUE_900,
                                    alignment= ft.alignment.center,
                                    padding= 10
                                ),
                                
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,

                        ),
                        ft.Row(
                            [
                                ft.Text(value=nome,
                                        text_align=ft.TextAlign.END,
                                        size=20, 
                                        color=ft.Colors.WHITE, 
                                        weight=10)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            
                        )
                    ], 
                    width=100,
                    height=135
                ),
                bgcolor=ft.Colors.LIGHT_BLUE_700,
                padding=20,
                border_radius=10,
            )
    return card

def caixaCadastro():
    #TextFields
    fldNome = ft.TextField(label="Nome",)
    flUsuario = ft.TextField(label="Usuário")
    fldSenha = ft.TextField(label="Senha",)
    fldEmail = ft.TextField(label="E-mail",)
    
    #Caixa de seleção
    Usuarios = ["Admin","Aluno","Professor"]
    
    ##Definir Seleções
    optUser =[]
    for usuario in Usuarios:
        optUser.append(
            ft.DropdownOption(
                    key=usuario,
                    content=ft.Text(
                        value=usuario,
                    ),
            )
        )
    drpUsuario = ft.Dropdown(
        editable=False,
        label="Tipo de Usuário",
        options=optUser,
    )

    caixaCadastro = ft.Row([
            ft.Column([
                fldNome,
                flUsuario,
                fldSenha,
                fldEmail,
                drpUsuario
            ]),
            ft.Column([

            ])
        ],
    )
    content = ft.Container(
        content=caixaCadastro,
        bgcolor=ft.Colors.LIGHT_BLUE_900,
        border_radius=5,
        padding=10
    )
    return content

#Sidebar Controls

#navRailDestination
def sideDestination(icone: ft.Icons, rota, texto):
    cor = ft.Colors.WHITE

    nav = ft.NavigationRailDestination(
                icon=ft.Icon(name=icone),
                label=rota,
                label_content=ft.Text(value=texto, color=cor),
                selected_icon=ft.Icon(name=icone, color=cor),

            )
    return nav