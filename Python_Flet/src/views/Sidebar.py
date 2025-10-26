import flet as ft
from flet import *

#Sidebar é uma navrail no flet
class Sidebar(ft.container):

    def __init__(self, page: ft.Page):
        self.rail = NavigationRail(
            min_width=100,
            min_extended_width=400,
            label_type= NavigationRailLabelType.ALL, #
            leading=FloatingActionButton(icon=Icons.CREATE, text="criar") #control principal
        )
        pass