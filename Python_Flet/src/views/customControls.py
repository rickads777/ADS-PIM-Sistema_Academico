import flet as ft
from .funcoes import *
from config import cxCadastro_maxHeight

#Home Controls

#body
def homeCard(icone: ft.Icons, nome, page: ft.Page = None, rota = "", sidebar: ft.NavigationRail = None, index_side: int = None):
    #Função click
    def clique(e):
        sidebar.selected_index = index_side
        page.go(rota)
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
                on_click= clique
            )
    return card

class caixaCadastros():
    def __init__(self, page :ft.Page):    
        self.page = page
        # Maiores IDs de cada
        self.maior_idAluno = 0
        self.maior_idProfessor= 0
        self.maior_idAdmin = 0

        # TextFields
        self.fldNome = ft.TextField(label="Nome",)
        self.fldUsuario = ft.TextField(label="Usuário", disabled=True)
        self.fldSenha = ft.TextField(label="Senha",)
        self.fldEmail = ft.TextField(label="E-mail",)
        self.fields = [self.fldNome,self.fldUsuario, self.fldSenha, self.fldEmail]
        ## Estilização dos Fields
        for field in self.fields: 
            field.border_color = ft.Colors.WHITE
            field.bgcolor = ft.Colors.LIGHT_BLUE_800
            field.focused_bgcolor = ft.Colors.LIGHT_BLUE_700
            field.color = ft.Colors.WHITE
            field.label_style = ft.TextStyle(color=ft.Colors.WHITE)
        # Dropdown p/ selecionar usuarios
        ## Opções
        Usuarios = ["Admin","Aluno","Professor"]    
    
        ## Definir Seleções como lista de options q será adicionado
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
        self.drpUsuario = ft.Dropdown(
            editable=False,
            label="Tipo de Usuário",
            options=optUser,
            on_change= self.muda_Drop,
            border_color= ft.Colors.WHITE,
            color=ft.Colors.WHITE
        )
        #Dropdown para selecionar turmas
        self.drpTurmas: ft.Dropdown = ft.Dropdown(
            label="Turmas",
            enable_filter=True,
            visible=False,
            width=310,
            enable_search=True,
            border_color= ft.Colors.WHITE,
            color=ft.Colors.WHITE
        )
        #Botão de Selecionar matérias
        self.alertMaterias = popEsc_Materia(self.page) #Chama a Classe do PopUp
        self.btnSlct_Materia = ft.TextButton(
            text="Selecionar Materias",
            visible=False,
            width=310,
            on_click=self.alertMaterias.abrirPop_Escolher_Materias
        )
        #Caixa de Cadastro
        self.caixaCadastro = ft.Row([
                ft.Column([
                    self.fldNome,
                    self.fldUsuario,
                    self.fldSenha,
                    self.fldEmail,
                    self.drpTurmas, self.btnSlct_Materia,
                    ft.Row([
                        self.drpUsuario,
                        ft.Row([
                            ft.IconButton(icon=ft.Icons.CHECK_CIRCLE, icon_size=30, icon_color=ft.Colors.LIGHT_BLUE,
                                        on_click= self.Salvar
                                        ),
                            ft.IconButton(icon=ft.Icons.CANCEL,icon_size=30, icon_color=ft.Colors.LIGHT_BLUE,
                                        on_click= self.Limpar
                                        )
                        ], alignment=ft.MainAxisAlignment.CENTER, expand=True
                        )
                    ], expand=True
                    ),
                    
                ], expand=True
                ),
            ],expand=True
        )
        self.content :ft.Container = ft.Container(
            content=self.caixaCadastro,
            bgcolor=ft.Colors.LIGHT_BLUE_900,
            border_radius=5,
            padding=10,
            animate=ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT),
            width=320,
            height=0
        )

    # Funções para o Clique    
    ## Limpar os campos
    def Limpar(self, e):
        for field in self.fields:
            if field.label != "Usuário":
                field.value = ""
            field.border_color = ft.Colors.WHITE
        self.muda_Drop(e)
        self.drpUsuario.border_color = ft.Colors.WHITE
        self.drpTurmas.border_color = ft.Colors.WHITE
        check: ft.Checkbox
        for check in self.alertMaterias.alertBody.controls:
            check.value = False
        self.page.update()
    
    ## Salvar
    def Salvar(self,e):
        verficacao = False #Controle de se existe algo nulo, se existe é True
        if self.drpUsuario.value == "Aluno" and self.drpTurmas.value == None:
            verficacao = True
            self.drpTurmas.border_color = ft.Colors.RED
        elif self.drpUsuario.value == "Professor":
            check: ft.Checkbox
            for check in self.alertMaterias.alertBody.controls:
                if not check.value:
                    verficacao = True
                else:
                    verficacao = False
                    break
        for field in self.fields:
            if field.value == '':
                field.border_color = ft.Colors.RED
                verficacao = True 
        if self.drpUsuario.value == '' or None:
            verficacao = True
            self.drpUsuario.border_color = ft.Colors.RED
        if verficacao:
            self.page.update()
            return
        else:
            cadastrar_Usuario(self.drpUsuario.value, self.fldNome.value, self.fldUsuario.value, self.fldSenha.value, self.fldEmail.value, self.drpTurmas.value, self.alertMaterias.Materias_Escolhidas, self.maior_idProfessor)
            self.maior_idProfessor = select_Next_Increment("professor")
            self.maior_idAdmin = select_Next_Increment("admin")
            self.maior_idAluno = select_Next_Increment("aluno")
            self.Limpar(e)
    # Função on_change
    ## Mostrar Turmas
    def muda_Drop(self, e):
        if self.drpUsuario.value == "Aluno":
            self.content.height =355
            self.drpTurmas.visible = True
            self.btnSlct_Materia.visible = False
            self.fldUsuario.value = "A"+(str(self.maior_idAluno))
        elif self.drpUsuario.value == "Professor":
            self.content.height =345
            self.btnSlct_Materia.visible = True
            self.drpTurmas.visible = False
            self.fldUsuario.value = "P"+(str(self.maior_idProfessor))
        elif self.drpUsuario.value == "Admin":
            self.fldUsuario.value = "R"+(str(self.maior_idAdmin))
            self.content.height =300
            self.drpTurmas.visible = False
            self.btnSlct_Materia.visible = False
        else:
            self.content.height =300
            self.drpTurmas.visible = False
            self.btnSlct_Materia.visible = False
            self.fldUsuario.value = None
            
        self.page.update()

    def retornaCtnCadastro(self):
        return self.content

#Pop Ups

##Pop Up para Prof Escolher materias
class popEsc_Materia:
    def __init__(self, page: ft.Page):
        self.page = page
        self.alertBody= ft.Column(wrap=True, scroll= ft.ScrollMode.AUTO)
        self.popEsc_Mat = ft.AlertDialog(
            title=ft.Text("Selecione as Matérias"),
            actions=[
                ft.TextButton("Confirmar", on_click=self.salvarEscolha_Materias),
                ft.TextButton("Cancelar", on_click=lambda e: self.page.close(self.popEsc_Mat))
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            content= self.alertBody,
            modal=True
        )
        self.Materias_Escolhidas = []
        #Materias puxadas do banco
        self.dbMaterias = {}
        self.select_Materia()

    def select_Materia(self):
        self.dbMaterias.clear()
        Materias = select_Unicos_DB("Materia","nome, idmateria") 
        for materia, id in Materias:
            self.alertBody.controls.append(
                ft.Checkbox(label=materia, value=False)
            )
            self.dbMaterias.update({materia:id})
    
    def abrirPop_Escolher_Materias(self, e):
        self.page.open(self.popEsc_Mat)

    def salvarEscolha_Materias(self, e):
        check:ft.Checkbox
        self.Materias_Escolhidas.clear()
        for check in self.alertBody.controls:
            if check.value:
                self.Materias_Escolhidas.append(self.dbMaterias.get(check.label))
        self.page.close(self.popEsc_Mat)

##Pop Up Exlcuir
class popExcluir_Cadastro:
    def __init__(self, usuario):
        self.usuario = usuario
        self.btnConfirma = ft.TextButton("Confirmar")
        self.btnCancela = ft.TextButton("Cancelar")
        self.popExcluir = ft.AlertDialog(
        title=ft.Text(f"Excluindo - {self.usuario}"),
        actions=[
            self.btnConfirma,
            self.btnCancela
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        content= ft.Text("Você realmente deseja realizar a exclusão? Essa alteração é final"),
        modal=True
    )

#Sidebar Controls
##navRailDestination
class sideDestination:
    def __init__(self, icone: ft.Icons, rota, texto):    
        
        self.rota = rota
        self.texto =texto
        self.icone = icone
        cor = ft.Colors.WHITE

        self.nav = ft.NavigationRailDestination(
                    icon=ft.Icon(name=self.icone),
                    label=self.rota,
                    label_content=ft.Text(value=self.texto, color=cor),
                    selected_icon=ft.Icon(name=self.icone, color=cor),

                )

#Tabela Genérica, padrão para as subclasses
class Tabela():
    def __init__(self, page: ft.Page, nomeTabela: str, colunas: list, linhas: str ):
        self.page = page
        self.nomeTabela = nomeTabela
        self.colunas = colunas
        self.colunas.append("") #Adiciona coluna sem nada, pra ficar os botões
        self.linhas = linhas
        self.Tab: ft.DataTable = ft.DataTable (columns=[])
        for coluna in self.colunas:
            self.Tab.columns.append(
                ft.DataColumn(
                    ft.Text(coluna),
                    heading_row_alignment=ft.MainAxisAlignment.CENTER
                )
            )
    def editarLinha(self):
        pass
    def excluirLinha(self):
        pass

    

class Tab_profs(Tabela):
    def __init__(self, page, nomeTabela, colunas, linhas):
        super().__init__(page,nomeTabela, colunas, linhas)
        self.btnExcluir = ft.IconButton(icon=ft.Icons.DELETE)
        self.criarLinhas()

    def criarLinhas(self):
        #Seleciona as linhas da tabela
        linhas_dtTble = select_DB(self.nomeTabela,self.linhas)

        for id, usuario, nome, senha, email in linhas_dtTble:
            materias = generic_Select_DB(f"select m.nome from Materia as m inner join professor_materia as mp on m.idmateria = mp.idmateria inner join professor as p on p.idprofessor = mp.idprofessor where p.idprofessor = {id}")
            #mat_prof = ", ".join(f'{materia}'.strip("()\',") for materia in materias)
            mat_prof = []
            for materia in materias:
                mat_prof.append(f'{materia}'.strip("()\',") )
            
            self.Tab.rows.append(
                dtLinha_Prof(self.page, nome, usuario, senha, email, mat_prof).linha
            )

class dtLinha:
    def __init__(self, page: ft.Page, nome, usuario: str, senha, email):
        #Paramêtros com valores recebidos
        self.page = page
        self.nome = nome
        self.usuario = usuario
        self._senha = senha
        self.email = email
        self.id = int(usuario.strip("APR"))
        self.identificador = usuario[0]
        self.linha: ft.DataRow
        
        #Textos fixos
        self.txtNome = ft.Text(self.nome)
        self.txtUsuario = ft.Text(self.usuario)
        self.txtSenha = ft.Text(value="*****")
        self.txtEmail = ft.Text(self.email)

        self.texts = [self.txtNome, self.txtUsuario, self.txtSenha, self.txtEmail]

        #Text fields
        self.fldNome = ft.TextField(value=self.nome)
        self.fldSenha = ft.TextField(value=self._senha)
        self.fldEmail = ft.TextField(value=self.email)

        #alerta de exclusão
        self.alert_Excluir = popExcluir_Cadastro(self.usuario)
        self.alert_Excluir.btnConfirma.on_click = self.click_Excluir

        self.fields = [self.fldNome, self.fldSenha, self.fldEmail]
        for field in self.fields:
            field.visible = False
            field.expand = True
            field.text_size = 15
        
        #Botões
        self.btnEditar = ft.IconButton(
            icon=ft.Icons.EDIT,
        )
        self.btnExcluir = ft.IconButton(
            icon=ft.Icons.DELETE,
            on_click=lambda e: self.page.open(self.alert_Excluir.popExcluir)
            
        )
        self.btnConfirmar = ft.IconButton(
            icon=ft.Icons.CHECK_CIRCLE, 
            icon_color=ft.Colors.LIGHT_BLUE,
            visible= False,
            #on_click= self.Salvar
        )
        self.btnCancelar = ft.IconButton(
            icon=ft.Icons.CANCEL,
            icon_color=ft.Colors.LIGHT_BLUE,
            visible= False,
            
        )

        #Senha Row
        self.btnMostra_Senha = ft.IconButton(
                                    icon=ft.Icons.VISIBILITY_OFF,
                                    selected_icon= ft.Icons.VISIBILITY,
                                    selected=False,
                                    on_click=self.mostra_Senha
                                )
        self.rowSenha = ft.Row(
                            [
                                self.btnMostra_Senha,
                                self.txtSenha,
                                self.fldSenha
                            ]
                        )
    def troca_Visible(self):
        self.btnEditar.visible = not self.btnEditar.visible
        self.btnExcluir.visible = not self.btnExcluir.visible
        self.btnConfirmar.visible = not self.btnConfirmar.visible 
        self.btnCancelar.visible = not self.btnCancelar.visible
        self.btnMostra_Senha.visible = not self.btnMostra_Senha.visible
        for field in self.fields:
            field.visible = not field.visible
        for text in self.texts:
            if text == self.txtUsuario:
                continue
            text.visible = not text.visible

    def mostra_Senha(self, e):
        self.btnMostra_Senha.selected = not self.btnMostra_Senha.selected 
        self.txtSenha.value = "*****" if self.txtSenha.value == self._senha else self._senha
        self.page.update()
    
    def click_Excluir(self,e):
        match self.identificador:
            case "R":
                delete_Registo("admin",self.id, "idadmin")
            case "A":
                delete_Registo("aluno", self.id, "idaluno")
            case "P":
                delete_Registo("professor_materia", self.id, "idprofessor")
                delete_Registo("professor", self.id, "idprofessor")
                self.page.close(self.alert_Excluir.popExcluir)
                self.page.update()
                self.page.go("/admin/home")
                self.page.go("/admin/professores")
                self.page.open(ft.SnackBar(ft.Text(f"{self.usuario} excluído com sucesso")))

            

    

class dtLinha_Prof(dtLinha):
    def __init__(self, page, nome, usuario:str, senha, email, materias: list[str]):
        super().__init__(page, nome, usuario, senha, email)
        self.materias = ", ".join(f'{materia}' for materia in materias) #Materias como Str
        self.listMaterias = materias #Lista das mastérias
        
        
        #Field
        self.txtMaterias = ft.Text(value=self.materias, width=180)
        self.texts.append(self.txtMaterias)

        self.btnCancelar.on_click= self.click_Cancelar
        self.btnEditar.on_click= self.click_Editar
        self.btnConfirmar.on_click = self.click_confirmar
        
        #Chama a Classe do PopUp Escolher Materias 
        self.alertMaterias = popEsc_Materia(self.page) 
        self.marca_Materias()

        self.btnSlct_Materia = ft.TextButton(
            text="Selecionar Materias",
            visible=False,
            width=180,
            on_click=self.alertMaterias.abrirPop_Escolher_Materias
        )

        self.linha= ft.DataRow(
            cells=[
                        ft.DataCell(
                            content=ft.Row(
                                [
                                    self.txtUsuario,
                                ],
                            )
                        ),
                        ft.DataCell(
                            content=ft.Row(
                                [
                                    self.txtNome,
                                    self.fldNome
                                ]
                            )
                        ),
                        ft.DataCell(
                            content=ft.Row(
                                [
                                    self.txtEmail,
                                    self.fldEmail
                                ]
                            )
                        ),
                        ft.DataCell(
                            content= self.rowSenha

                        ),
                        ft.DataCell(
                            content=ft.Column(
                                [
                                    self.txtMaterias,
                                    self.btnSlct_Materia
                                ], scroll= ft.ScrollMode.AUTO
                            )
                        ),
                        
                        ft.DataCell(ft.Row([
                            self.btnEditar, 
                            self.btnExcluir,
                            self.btnConfirmar,
                            self.btnCancelar
                            ]))
                    ]
        )
    def troca_Visible(self):
        self.btnSlct_Materia.visible = not self.btnSlct_Materia.visible
        return super().troca_Visible()
        
    def click_Editar(self, e):
        self.troca_Visible()
        self.page.update()

    def click_Cancelar(self, e):
        self.troca_Visible()
        self.fldNome.value = self.txtNome.value
        self.fldEmail.value = self.txtEmail.value
        self.fldSenha.value = self.txtSenha.value
        self.marca_Materias()
        self.page.update()

    def click_confirmar(self, e):
        try:
            
            connection.connect()
            cursor.execute(f'update professor set nome ="{self.fldNome.value}", email ="{self.fldEmail.value}", senha = "{self.fldSenha.value}" where idprofessor = {self.id}')
            if self.alertMaterias.Materias_Escolhidas != []:
                cursor.execute(f'delete from professor_materia where idprofessor = {self.id}')
                for materia in self.alertMaterias.Materias_Escolhidas:
                    cursor.execute(f'INSERT INTO Professor_Materia (idprofessor, idmateria) VALUES ({self.id}, {materia})')
            connection.commit()
            connection.close()

        except: 
            self.page.open(ft.SnackBar(ft.Text(f"Um Erro inesperado Ocorreu")))
            self.click_Cancelar(e)
        else:
            self.txtNome.value = self.fldNome.value 
            self.txtEmail.value = self.fldEmail.value
            self._senha = self.fldSenha.value
            self.listMaterias.clear()
            check: ft.Checkbox
            for check in self.alertMaterias.alertBody.controls:
                if check.value:
                    self.listMaterias.append(check.label)
            materia = ", ".join(f'{materia}' for materia in self.listMaterias)
            self.txtMaterias.value = materia
            self.page.open(ft.SnackBar(ft.Text(f"{self.usuario} editado com sucesso")))
            self.click_Editar(e) 

    def marca_Materias(self):
        #Selecionar as matérias que já estão cadastradas
        check: ft.Checkbox
        for check in self.alertMaterias.alertBody.controls:
            if check.label in self.listMaterias:
                check.value = True