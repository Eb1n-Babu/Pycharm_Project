import pandas as pd

from mySql.connectionestablishment import connection

query = "select * from student"
df = pd.read_sql(query, connection)

print(df)

connection.close()

