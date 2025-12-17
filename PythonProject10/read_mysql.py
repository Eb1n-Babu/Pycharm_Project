import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="@Ebinbabu2209",
    database="userprofile",
    charset="utf8"
)

def get_data():
    cursor = my_db.cursor()
    cursor.execute("select * from userlist")
    data = cursor.fetchall()
    for row in data:
        print(row)


get_data()

def get_data2(user_id):
    cursor = my_db.cursor()
    cursor.execute("select * from userlist where id = %s", (user_id,))
    data = cursor.fetchone()
    print(data)

get_data2(10)
