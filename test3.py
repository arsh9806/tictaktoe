'''TotalSquares = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
                ]
GivenSquare = []
List = []
for i in range(3):
     List = list(map(int, input().split()))
     GivenSquare.append(List)
List = []
for i in TotalSquares:
    total = 0
    for j in range(3):

        for k in range(3):
            if i[j][k] != GivenSquare[j][k]:
                total += abs(i[j][k] - GivenSquare[j][k])
    List.append(total)
print(min(List))

Array = [1, 2, 2, 3, 1, 2]
temp = []
NewList = []
for i in range(len(Array)):
    NewList.append(Array.count(Array[i])+Array.count(Array[i]+1))
print(max(NewList))'''
'''NumberOfElemts = int(input())
NewList = list(set(map(int,input().split())))
NewList.sort()
NumberOfElements = int(input())
elements = list(map(int,input().split()))

rank = []
index = 0
n = len(NewList)
for i in elements:
    while n > index and i >= NewList[index]:
        index += 1
    rank.append(n+1-index)
for i in rank:
    print(i)'''



'''NumberOfElemts = int(input())
NewList = list(set(map(int,input().split())))
NumberOfElements = int(input())
elements = list(map(int,input().split()))
temp = NewList
rank = []
for i in elements:
    NewList.append(i)
    NewList.sort(reverse=1)
    rank.append(NewList.index(i) + 1)
    NewList = temp
for i in rank:
    print(i)
'''
'''element = [5, 25, 50, 120]
rank = 1
i = 0
ranks = []
for j in range(len(element)):
    NewList.append(element[j])
    NewList.sort()
    ele = element[j]
    while NewList[i] != ele:
        i += 1
        if NewList[i] != NewList[i-1]:
            rank += 1
        print(i)
    print("*")

    ranks.append(rank)
    NewList.remove(ele)

for i in reversed(ranks):
    print(i)'''
'''import random as rd
import os
files = []
# print(files)
for _, _, c in os.walk("C:/Users/Arsh/Downloads"):
    for i in c:
        if i.endswith("mp3"):
            files.append(i)
print(files)

otp = rd.randint(1000, 9000)
print("OTP Lastly is:", otp)'''
'''
import requests as rq
import json as js
ref = rq.get("https://newsapi.org/v2/everything?q=bitcoin&from=2019-05-25&sortBy=publishedAt&apiKey=02d2944f372c48d0bf0d53fb8647a6c1")
response = js.loads(ref.text)
print(response)
print(response['articles'][0])
print(response['articles'][0]['title'])
print(response['articles'][0]['description'])'''
'''import numpy as np
chessBoard = np.zeros((8, 8), dtype=int)
chessBoard[1::2, ::2] = 1
chessBoard[::2, 1::2] = 1
case = int(input())
lis = []
for _ in range(case):
    n = int(input())
    sum1 = 0
    div = (n-1)//3
    sum1 = (3*div*(div+1))//2
    div = (n-1)//5
    sum1 += (5*div*(div+1))//2
    div = (n-1)//15
    sum1 -= (15*div*(div+1))//2
    lis.append(sum1)
for i in lis:
    print(i)'''
import math
# import numpy as np
# arr3D = np.array([[1,2,3],
#                  [4,5,6],
#                  [7,8,9]])
#
# arr3D1 = np.array([[11,12,13],
#                  [14,15,16],
#                  [17,18,19]])
#
#
# print(np.vstack((arr3D, arr3D1)))
'''
import timeit
stamp = timeit.default_timer()
arr = [1,2,3,4,3,3,2,1]
lis = []
while arr:
    lis.append(len(arr))
    arr[:] = [i - min(arr) for i in arr]
    arr = list(filter(lambda a:a != 0,arr))
    print(arr)
print(lis)
stamp1 = timeit.default_timer()
print(stamp1-stamp)
'''

'''
import numpy as np
#for checking 1
arr = np.genfromtxt("numbers.txt", dtype=int)
if (len(arr[:, len(arr[1]) - 1])) == list(arr[:, len(arr[1]) - 1]).count(1):
    print("one")
#for checking 2
'''
lis = [1,2,3,4,5,8,7]
lis = [x for x in lis if x%2 != 0]
print(lis)
