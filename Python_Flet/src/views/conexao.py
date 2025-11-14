import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="educazone",
    password="12345",
    database="dbEducaZone"
)
cursor = connection.cursor()

connection.close()

#Exemplo Create
#Select

def select_DB (table, colunas):
    connection.connect()
    cursor.execute(f'SELECT {colunas} FROM {table}')
    ret = cursor.fetchall()
    connection.close()
    return ret 

def select_Unicos_DB (table, colunas):
    connection.connect()
    cursor.execute(f'SELECT DISTINCT {colunas} FROM {table}')
    ret = cursor.fetchall()
    connection.close()
    return ret

def generic_Select_DB(comando):
    connection.connect()
    cursor.execute(comando)
    ret = cursor.fetchall()
    connection.close()
    return ret

def select_Maior(table, coluna):
    connection.connect()
    cursor.execute(f'SELECT MAX({coluna}) FROM {table}')
    num = str(cursor.fetchall()[0])
    num = num.strip("(\'),")
    try:
        connection.close()
        return int(num)
    except:
        connection.close()
        return 0

def select_Next_Increment(table):
    connection.connect()
    cursor.execute(f'SELECT `auto_increment` FROM INFORMATION_SCHEMA.TABLES WHERE table_name = "{table}"; ')
    num = str(cursor.fetchall()[0])
    num = num.strip("(\'),")
    try:
        connection.close()
        return int(num)
    except:
        connection.close()
        return 0

def select_Senha(table, senha):
    connection.connect()
    cursor.execute(f'SELECT senha FROM {table} where senha = "{senha}"')
    ret = str(cursor.fetchall()).strip("[](\'),")
    connection.close()
    return ret

def select_Senha_User(table, senha):
    connection.connect()
    cursor.execute(f'SELECT senha FROM {table} where usuario = "{senha}"')
    ret = str(cursor.fetchall()).strip("[](\'),")
    connection.close()
    return ret

#Deletar
def delete_Registo(table, id, identificador):
    connection.connect()
    cursor.execute(f'Delete FROM {table} where {identificador} = "{id}"')
    connection.commit()
    connection.close()


#Comando Genérico que Precise dar Comit (Insert, Delete, Update)
def generic_Comitable(comando):
    connection.connect()
    cursor.execute(comando)
    connection.commit()
    connection.close()