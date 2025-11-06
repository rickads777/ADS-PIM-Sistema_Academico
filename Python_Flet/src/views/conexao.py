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