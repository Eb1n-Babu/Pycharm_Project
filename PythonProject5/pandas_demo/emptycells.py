import pandas as pd
import matplotlib.pyplot as plt

obj_2 = pd.read_csv(r"C:\Users\ebinb\PycharmProjects\PythonProject5\emptycellsdemo.csv")
print(obj_2.to_string())

obj_3 = obj_2.dropna()
print(obj_3.to_string())
obj_4 = obj_2["Age"].mean()
print(obj_4)
"""obj_2 = obj_2.fillna({"Age": "30"},inplace=True)
print(obj_2.to_string())"""
obj_2.plot()
plt.show()
