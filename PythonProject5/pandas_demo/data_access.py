import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv(r"C:\Users\ebinb\PycharmProjects\PythonProject5\mydata.csv")  # Using raw string
print(df.to_string())
df.plot(kind='bar')
plt.show()