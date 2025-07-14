import pandas as pd
from sqlalchemy import create_engine

# Create SQLAlchemy engine
engine = create_engine("mysql+mysqlconnector://your_username:your_password@localhost/your_database")

# Read data using pandas
query = "SELECT * FROM your_table"
df = pd.read_sql(query, engine)

print(df)