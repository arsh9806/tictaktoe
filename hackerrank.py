'''a,b = input().split()
a, b = [int(a),int(b)]
List = set()
ArrayA = list(map(int, input().split()))
temp = 0
ArrayB = list(map(int, input().split()))
for i in range(max(ArrayA), min(ArrayB)+1):
    for j in ArrayA:
        if i%j is 0:
            temp += 1

    if temp is len(ArrayA):
        List.add(i)
    temp=0
newList = list(List)
temp = 0
newSet = set()
for i in newList:
    for j in ArrayB:
        if j%i==0:
            temp+=1
    if temp is len(ArrayB):
        newSet.add(i)
    temp=0

print(len(list(newSet)))
'''















'''nm = input().split( "-" )
a = (nm[0])
b = (nm[1])
print(nm)'''







'''x1, v1, x2, v2 = input().split()
x1, v1, x2, v2 = [int(x1),int(v1),int(x2),int(v2)]
if (x1<x2 and v1<v2) or (x2>x1 and v2>v1) or v1 is v2:
    print("NO")
    exit(0)
diff = 0
while True:
    x1 += v1
    x2 += v2
    diff = x2 - x1
    if diff < 0:
        print("NO")
        break
    elif diff is 0:
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
width = 0.35       # the width of the bars

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

ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )

plt.show()
'''