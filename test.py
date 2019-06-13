'''Array = ["C", "C++", "Java", "Python", "Dart"]
temp = 0
#Array = list(map(int,input("enter array : ").split()))
Shift = int(input(" Enter shift value"))
for i in range(0,Shift):
    temp = Array[0]
    Array.remove(Array[0])
    Array.append(temp)

print(Array)'''



'''
NumberOfCandies = int(input("Enter number of candies"))
M = int(input("Enter value of M "))
CandiesAte = []
X = 0
CandiesAte.append(0)
for i in range(0, NumberOfCandies):
    X = (X+M) % NumberOfCandies

    if X in CandiesAte:
        break
    else:
        CandiesAte.append(X)
print(len(CandiesAte))'''

'''NumberOfBirds = int(input())
Occurence = list(map(int, input().split()))
Type = []
for i in range(0, max(Occurence)):
    Type.append(Occurence.count(i+1))

print((Type.index(max(Type))) + 1)'''




'''year = int(input())
if 1700 <= year <= 2700:
    if 1700 <= year < 1918:
        if year%4 == 0:
            print(f"12.09.{year}")
        else:
            print(f"13.09.{year}")
    elif 1918 < year <=2700:
        if (year%400==0) or (year%4==0 and year%100 is not 0):
            print(f"12.09.{year}")
        else:
            print(f"13.09.{year}")
    else:
        print(f"26.09.{year}")
'''


'''num = int(input())
for i in range(1,num+1):

    print("{0:d}     {0:o}     {0:X}     {0:b}".format(i))'''

'''Sum = 0
NumberOfItems, i = input().split()
NumberOfItems, i = [int(NumberOfItems), int(i)]
Items = list(map(int, input().split()))
AnnaCharged = int(input())
for j in range(0, NumberOfItems):
    Sum += Items[j]
Sum = Sum - Items[i]
Actual = Sum//2
if AnnaCharged is Actual:
    print("Bon Appetit")
else:
    print(AnnaCharged - Actual)'''

'''NumberOfSocks = int(input())
Items = list(map(int, input().split()))'''


'''Array = list(map(int,input().split()))
pairs = 0
s = 0
Array.sort()
#Array = [10, 10, 10, 10, 20, 20, 20, 30, 50]
Newset = set()
for i in Array:
    Newset.add(i)
Newset = list(Newset)
for i in Newset:
    a= Array.count(i)
    if a%2 is 0:
        pairs += (a//2)
    else:
        a -= 1
        pairs += (a//2)

print(pairs)'''



'''NumberOfPages = int(input())
PageNumber = int(input())
TurnsFront = 0
TurnsBack = 0
#from the front
if NumberOfPages % 2 is 0 and (NumberOfPages is (PageNumber+1)):
    print("1")
    exit(0)
TurnsFront = PageNumber//2
#from back
Diff = NumberOfPages - PageNumber
TurnsBack = Diff//2
if TurnsBack < TurnsFront:
    print(TurnsBack)
elif TurnsFront < TurnsBack:
    print(TurnsFront)
else:
    print(TurnsBack)'''


'''Total = int(input("Enter total amount to test Promocode : "))
print("------------------------------------------------")
print()
AmountToPay = 0
Discout = 0
Promo = ""
if Total < 500:
    AmountToPay = Total
    print("No Promocode Available")
    print("Final Amount To Pay : ", AmountToPay)
    exit(0)
def PromoCode(total):
    if total >=500 and total <= 1000:
        print("Apply ' FLAT30 ' promocode to get 30% discount ")
        print("------------------------------------------------")

    elif total >1000:
        print("Apply ' FLAT50 ' promocode to get 50% discount ")
        print("------------------------------------------------")

PromoCode(Total)
while True:
    Promo = input("Enter Promocode : ")
    if Total >= 500 and Total <= 1000 and Promo == "FLAT30":
        print("Promocode Applied Successfully")
        print("------------------------------------------------")
        AmountToPay = Total - (.3*Total)
        print("Actual Amount : " ,Total)
        print("Discount : ",.3*Total)

        print("Final Amount To Pay : ",AmountToPay)
        exit(0)
    elif Total > 1000 and Promo == "FLAT50":
        print("Promocode Applied Successfully")
        print("------------------------------------------------")
        AmountToPay = Total - (.5 * Total)
        print("Actual Amount : ", Total)
        print("Discount : ", .5 * Total)
        print("Final Amount To Pay : ", AmountToPay)
        exit(0)
    elif Promo == "" and Total:
            print("You haven't entered any promo code ")
            print("------------------------------------------------")

            AmountToPay = Total
            print("Final Amount To Pay : ", AmountToPay)
            exit(0)
    else:
        print("Enter a valid Promocode ")
        print("------------------------------------------------")
        print()'''


'''arr = [57,57,-57,57]
arr.sort()
run = 0
print(arr)
for i in range(len(arr)-1, -1, -1):
    if arr[i] is not max(arr):
        print("hi")
        run = arr[i]
        break

print(run)

NumberOfSteps = int(input())
Steps = input()
SeaLevel = 0
for i in range(NumberOfSteps):
    if Steps[i] is "D":
        SeaLevel -= 1
    elif Steps[i] is "U":
        SeaLevel += 1
'''


d = { 1 : "ABC",2 : "CDE"}
print(d)











