#This file is used One time to Create the Database in the MySQL Server

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)

#Prepare Cursor Object
cursorObject = dataBase.cursor()

#Create a Database
cursorObject.execute("CREATE DATABASE crmdb")
print("DATABASE CREATED")


# To run this, In CMD, > python mydb.py