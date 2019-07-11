# import numpy as np
# arr = np.arange(10,20,2)
# print(arr)
# arr1  = np.linspace(0,22,11 , dtype=int)
# print(arr1)
# arr2 = np.genfromtxt("Data.csv",delimiter=",",dtype=int)
# print(arr2[0:,:-1])
import tkinter as tk
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
'''

import pandas as pd
data = pd.read_csv("Data.csv", index_col ="Month")
# first = data.loc[1]  #retrieve
data.head(24)
new_data =pd.DataFrame({}, index=[2])

data = pd.concat([new_data]).reset_index(drop=True)
data.head(24)
print(data)
'''
'''

import pandas as pd
# arr1 = {"john": 20, "jennie": 30, "jim": 40, "jack": 50, "joe": 60}
# arr = {"john": 50, "jennie": 130, "jim": 240, "jack": 530, "joe": 760}
# arr = [1,32,3,4,56,6]
# arr1 = [12 ,332,333,43,563,63]
# print(pd.DataFrame([arr, arr1]))
# 
# data = pd.read_csv("Data.csv")
# print(data)
# print()
# print(data.loc[3])
'''


import matplotlib.pyplot as plt
# X = [1,2,3,4,5,6]
# Y1 = [n for n in X]
# Y2 = [n*n for n in X]
# Y3 = [n*n*n for n in X]
#
# print(X)
# print(Y1)
# print(Y2)
# print(Y3)
#
# plt.plot(X, Y1, label="Y1")
# plt.plot(X, Y2, label="Y2")
# plt.plot(X, Y3, label="Y3")
# plt.show()
'''arr = [1,32,3,4,56,6]
arr1 = [12 ,332,333,43,563,63]
arr2 = [1,2,3,4,5,6]
plt.plot(arr, arr1, label="1")
plt.plot(arr, arr2, label="32")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Polynomial Graphs")
plt.grid(True)
plt.legend()
plt.show()'''
import numpy as np
# x = [1,22,5,54,7.5,8,8,9]
# y = [11,2,5,4,7.5,8,8,9]
# plt.hist([y,x], 20)
#
# plt.show()
'''
scores = {"virat":82, "rohit":140, "rahul":102, "dhawan":118, "dhoni":56}
for i in scores:
    plt.bar(i,scores[i])
plt.show()
'''
'''
player = ["arsh","raman","sandeep"]
kills = [19,15,16]

plt.pie(kills,labels=player)
plt.show()
'''

'''
import math

lst = [1 ,2 ,3 ,1 ,2 ,3 ,3 ,3]
def most_common(lst):
    return max(set(lst), key=lst.count)
print(most_common(lst))'''
import math
import matplotlib.pyplot as plt
import numpy as np

lis = np.arange(-2,5,0.01)
linear = [i for i in lis]
lam = lambda x : 1 if x>0 else 0
bin = list(map(lam, lis))
sigmoid = [(1/(1+math.exp(-i))) for i in lis]
hyper = [math.tanh(i) for i in lis]
lam1 = lambda x : x if x>=0 else 0
rlu = list(map(lam1,lis))
softmax = (np.exp(lis))/sum(np.exp(lis))
plt.plot(lis,linear,label="linear")
plt.plot(lis,bin,label="binary")
plt.plot(lis,sigmoid,label="sigmoid")
plt.plot(lis,rlu,label="recified linear")
plt.plot(lis,hyper,label="hyper")
plt.plot(lis,softmax,label="softmax")
plt.legend()
plt.grid()
plt.show()