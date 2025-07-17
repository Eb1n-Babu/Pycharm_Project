import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="@Ebinbabu2209",
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")