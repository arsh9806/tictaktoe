'''NumberOfElements , k = input().split()
NumberOfElements , k = [int(NumberOfElements),int(k)]
Array = list(map(int, input().split()))
temp = 0
for i in range(0,len(Array)):
    for j in range(i+1,len(Array)):
        if (Array[i]+Array[j])%k is 0:
            temp += 1

print(temp)'''


'''bnm = input().split()

budget = int(bnm[0])

NumberOfKeyboards = int(bnm[1])

NumberOfUsb = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))

drives = list(map(int, input().rstrip().split()))
keyboards.sort(reverse=1)
drives.sort(reverse=1)
amount = 0
print(keyboards)
print(drives)
temp = 0
boole = False
for i in range(0,NumberOfKeyboards):
    for j in range(0,NumberOfUsb):
        if keyboards[i]+drives[j] <= budget and keyboards[i]+drives[j] > temp :
            print(keyboards[i],drives[j])
            temp = keyboards[i]+drives[j]
            boole = True


if boole:
    print(temp)
else :
    print("-1")'''
'''NumberOfQueries = int(input())
l=[]
for i in range(0,NumberOfQueries):
    xyz = list(map(int,input().split()))
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])


    if abs(z-x) > abs(z-y):
        l.append("Cat B")
    elif abs(z-x) < abs(z-y):
        l.append("Cat A")
    elif abs(z-x) == abs(z-y):
        l.append("Mouse C")
print(l)'''

