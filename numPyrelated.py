# import numpy as np
# arr = np.arange(10,20,2)
# print(arr)
# arr1  = np.linspace(0,22,11 , dtype=int)
# print(arr1)
# arr2 = np.genfromtxt("Data.csv",delimiter=",",dtype=int)
# print(arr2[0:,:-1])
'''import time
stamp = time.time()
import pandas as pd
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
list1 = pd.DataFrame(data)
print(list1[['Name']])
stamp1 = time.time()
print(stamp1-stamp)'''
import pandas as pd
data = pd.read_csv("Data.csv", index_col ="Month")
# first = data.loc[1]  #retrieve
data.head(24)
new_data =pd.DataFrame({}, index=[2])

data = pd.concat([new_data]).reset_index(drop=True)
data.head(24)
print(data)