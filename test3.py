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
'''
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup
import requests
url = "https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")
# print(soup.title.text)
# print(soup.prettify())
# print(list(soup.children))
# print(list(soup.find_all("title")))
tags = soup.find_all("h3", attrs={'class':'lister-item-header'})
inmovies = []
for i,tag in enumerate(tags):
    inmovies.append(tag.find('a').contents[0])
    if i == 10:
        break
inratings = []
rating_records = soup.find_all("div",class_="inline-block ratings-imdb-rating")
for i, tag in enumerate(rating_records):
    inratings.append(float(tag.text.strip()))
    if i == 10:
        break


# data =  [10,25,100,40]


register = [0,1,2,3,4,5,6,7,8,9,10]
# pets = ["cats","dog","hed","bunny"] ,movies
plt.style.use('dark_background')
plt.figure(figsize=(5, 5))
international = plt.bar(inmovies,inratings,width = .3,color="0.8",edgecolor="r",linewidth=2, )
plt.xticks(inmovies,rotation="vertical",fontweight="bold")
plt.title("Movies rating chart")
plt.ylabel("Ratings",fontsize=15,fontweight="bold",color="0.7")
plt.title("Top 10 Highest Rated International Movies", fontweight="bold")
for a,b in zip(inmovies,inratings):
    plt.text(a, b, str(b), horizontalalignment='center')
plt.ylim((8,10))'''
# plt.legend()
# plt.show()
# data =  [10,25,100,40]
# register = 0,1,2,3
# pets = "cats","dog","hed","bunny"
# plt.figure(figsize=(8,4))
# b = plt.bar(register,data,width = .2 )
# plt.title("pets")
# plt.xticks(register,pets)
# plt.legend()
# plt.show()
'''string = "123456"
import random as rd
lis = rd.sample(string,6)

print(" ".join(lis))
print(lis)
'''

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
'''

url = "http://www.howstat.com/cricket/Statistics/Players/PlayerYears_ODI.asp?PlayerID=3243"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# Names = soup.find_all("td",class_="TableHeadingRight")
# columns = ["Year"]
# for tag in Names:
#     columns.append(tag.text.strip())
#
columns = soup.find_all("td",attrs={"class":"TableHeadingRight"})
lis = []

i = 0
for new in columns:
    i+=1
    if i==13:
        break
    lis.append(new.text.strip())
lis = np.array(lis)
# print(lis)
rows = soup.find("div", {"id": "bat"})
Year = rows.find_all("a",class_="LinkNormal")
years = []
for i in Year:
    years.append(int(i.text))
years.append("Overall(16)")
years = pd.Series(years)
# years = years.reshape()
# print(years.shape)

data = rows.find_all("td",{"align" : "right"})
scores = []
for i in data:
    scores.append(i.text.strip())

scores = np.array(scores)
scores = scores.reshape(17,12)

# print(scores)

news = pd.DataFrame(scores,columns=lis,index=(years))
# print(news)

X = np.array([int(i) for i in years[:-2]])
Y = np.array([float(i) for i in news["Avg"][:-2]])
X = X.reshape(len(X),1)
Y = Y.reshape(len(Y),1)
model = LinearRegression()
model.fit(X,Y)
print(model.intercept_)
print(model.coef_)
y1 = model.predict(X)
print(r2_score(Y,y1))
a = model.intercept_ + model.coef_ * 2019
print(a)
plt.plot(X,y1,label="Regreesion line")
plt.scatter(X,Y,label="Data points")
plt.show()'''


'''file = pd.read_csv("Advertising.csv")
X = np.array(file["TV"])
Y = np.array(file["Sales"])
model = LinearRegression()
X= X.reshape(len(X), 1)
Y= Y.reshape(len(Y), 1)
model.fit(X, Y)
Y1 = model.predict(X)
print("Slope is : ", model.coef_)
print("Intercept  is : ", model.intercept_)
print("R2 score is : ", r2_score(Y, Y1))
plt.plot(X,Y1,label="Regression",color="r")
plt.scatter(X,Y,label="Original")
plt.show()'''
import cv2 as cv
img = cv.imread("quote1.jpg")
(row, col) = img.shape[:2]
print(row, col)
center = (row/2,col/2)
newimg = cv.getRotationMatrix2D(center,90,1.0)
rotated = cv.warpAffine(img,newimg,(row,col))
cv.imshow("title",rotated)
cv.waitKey(0)



