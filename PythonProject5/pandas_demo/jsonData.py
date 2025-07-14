import pandas as pd

obj = pd.read_json(r"C:\Users\ebinb\PycharmProjects\PythonProject5\mydata.json.json")
print(obj.to_string())
print(obj.info)
print(obj.head())
print(obj.tail())
import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())