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

case = int(input())
lis = []
for _ in range(case):
    n = int(input())
    a = 1
    b = 2
    c = a + b
    sum1 = 2
    while True:

        if c < n and c % 2 == 0:
            sum1 += c

        a = b
        b = c
        c = a + b
        if c < n:
            continue
        else:
            break
    lis.append(sum1)
for i in lis:
    print(i)