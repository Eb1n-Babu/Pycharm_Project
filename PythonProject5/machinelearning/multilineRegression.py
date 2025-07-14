import pandas
from sklearn import linear_model

obj = pandas.read_csv(r"C:\Users\ebinb\PycharmProjects\PythonProject5\machinelearning\data.csv")
new_demo = pandas.DataFrame(obj)
X = obj[['Weight', 'Volume']]
y = obj['CO2']