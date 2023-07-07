import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
)

cursorObj = dataBase.cursor()

cursorObj.execute('create database django_website')