import mysql.connector

db = mysql.connector.connect(
    host="localhost",user="root",passwd="@Ebinbabu2209"
)
print("connected to database")