import pandas as pd

list_1 = [0,1,2,3,4,5]
obj_3 = pd.DataFrame(list_1)
print(obj_3)
print(list_1[0])

dict_1 = {
    'student':["amal","akhil","anju","robin"],'marks':[100,30,50,50]}
obj_4 = pd.DataFrame(dict_1)
print(obj_4)
print(obj_4.loc[0])
print(obj_4.loc[1])
obj_4 = pd.DataFrame(dict_1,index=["day1","day2","day3","day4"])
print(obj_4)
