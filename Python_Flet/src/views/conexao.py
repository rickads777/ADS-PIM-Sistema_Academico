import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="educazone",
    password="12345",
    database="dbEducaZone"
)
cursor = connection.cursor()

#Exemplo Create
#Select

def select_DB (table, colunas):
    cursor.execute(f'SELECT {colunas} FROM {table}')
    return cursor.fetchall()

def select_Unicos_DB (table, colunas):
    cursor.execute(f'SELECT DISTINCT {colunas} FROM {table}')
    return cursor.fetchall()

def generic_Select_DB(comando):
    cursor.execute(comando)
    return cursor.fetchall()

def select_Maior(table, coluna):
    cursor.execute(f'SELECT MAX({coluna}) FROM {table}')
    num = str(cursor.fetchall()[0])
    num = num.strip("(\'),")
    try:
        return int(num)
    except:
        return 0

def select_Senha(table, senha):
    cursor.execute(f'SELECT senha FROM {table} where senha = "{senha}"')
    return str(cursor.fetchall()).strip("[](\'),")

def select_Senha_User(table, senha):
    cursor.execute(f'SELECT senha FROM {table} where usuario = "{senha}"')
    return str(cursor.fetchall()).strip("[](\'),")