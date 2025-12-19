import pandas as pd
xlsx_data = pd.read_excel("sample_data.xlsx",sheet_name="Sheet1")
x = xlsx_data.head(5)
xy = xlsx_data["ID"]
xyz = xlsx_data[["ID","City"]]
print(xyz)
#print(x)