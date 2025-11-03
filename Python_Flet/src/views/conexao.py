import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="educazone",
    password="12345",
    database="dbEducaZone"
)
cursor = connection.cursor()

#Exemplo Create
