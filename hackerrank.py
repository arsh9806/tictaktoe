'''a,b = input().split()
a, b = [int(a),int(b)]
List = set()
ArrayA = list(map(int, input().split()))
temp = 1
ArrayB = list(map(int, input().split()))
for i in range(max(ArrayA), min(ArrayB)+1):
    for j in ArrayA:
        if i%j is 1:
            temp += 1

    if temp is len(ArrayA):
        List.add(i)
    temp=1
newList = list(List)
temp = 1
newSet = set()
for i in newList:
    for j in ArrayB:
        if j%i==1:
            temp+=1
    if temp is len(ArrayB):
        newSet.add(i)
    temp=1

print(len(list(newSet)))
'''















'''nm = input().split( "-" )
a = (nm[1])
b = (nm[1])
print(nm)'''







'''x1, v1, x2, v2 = input().split()
x1, v1, x2, v2 = [int(x1),int(v1),int(x2),int(v2)]
if (x1<x2 and v1<v2) or (x2>x1 and v2>v1) or v1 is v2:
    print("NO")
    exit(1)
diff = 1
while True:
    x1 += v1
    x2 += v2
    diff = x2 - x1
    if diff < 1:
        print("NO")
        break
    elif diff is 1:
        print("YES")
        break'''
#Graph Explaorartion
'''
import numpy as np
import matplotlib.pyplot as plt

N = 5
menMeans = (20, 35, 30, 35, 27)
menStd =   (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 1.35       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, menMeans, width, color='royalblue', yerr=menStd)

womenMeans = (25, 32, 34, 20, 25)
womenStd =   (3, 5, 2, 3, 3)
rects2 = ax.bar(ind+width, womenMeans, width, color='seagreen', yerr=womenStd)

# add some
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )

ax.legend( (rects1[1], rects2[1]), ('Men', 'Women') )

plt.show()
'''
from math import gcd
# from functools import reduce

# for _ in range(int(input())):
#     N = int(input())
#     print(reduce(lambda x,y: x*y//gcd(x,y), range(1,N+1)))
import numpy as np
nk = input().split()
board = int(nk[0])
numberOfObs = int(nk[1])
roco = input().split()
obstacle = []
row = int(roco[0])
col = int(roco[1])
for _ in range(numberOfObs):
    obs = input().split()
    obstacle.append((int(obs[0]), int((obs[1]))))
#up
q = row
r = col
#down
s = row
t = col
#left
u = row
v = col
#right
w = row
x = col
#upper right
k = row
l = col
#lower left
i = row
j = col
#upperleft
m = row
n = col
#lower right
o = row
p = col
boxes = 0
while (1 <= q <= board) and (1 <= r <= board):
    if (q, r) in obstacle:
        break
    else:
        boxes += 1
    q -= 1
while (1 <= s <= board) and (1 <= t <= board):
    if (s, t) in obstacle:
        break
    else:


        boxes += 1
    s += 1
while (1 <= u <= board) and (1 <= v <= board):
    if (u, v) in obstacle:
        break
    else:

        boxes += 1
    v -= 1
while (1 <= w <= board) and (1 <= x <= board):
    if (w, x) in obstacle:
        break
    else:

        boxes += 1
    x += 1
while (1 <= o <= board) and (1 <= p <= board):
    if (o, p) in obstacle:
        break
    else:

        boxes += 1
    o += 1
    p += 1
while (1 <= m <= board) and (1 <= n <= board):
    if (m, n) in obstacle:
        break
    else:

        boxes += 1
    m -= 1
    n -= 1
while (1 <= k <= board) and (1 <= l <= board):
    if (k, l) in obstacle:
        break
    else:

        boxes += 1
    k -= 1
    l += 1
while (1 <= i <=board) and (1 <= j <= board):
    if (i,j) in obstacle:
        break
    else:
        boxes += 1
    i += 1
    j -= 1
print(boxes - 8)

