# INSTALL Mysql on your comp, instalar mysql no seu pc
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Leonard0'

	)

#prepare a cursor object, preparar objeto cursor
cursorObject = dataBase.cursor()

#create a database, criar o banco de dados
cursorObject.execute("CREATE DATABASE dcrm")
print("DATABASE CREATED")
