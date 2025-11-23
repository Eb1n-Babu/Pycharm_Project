import mysql.connector

# Establish connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Ebinbabu2209",
    database="db"
)

# Check if connection is successful
if connection.is_connected():
    print("Connection Successful!")