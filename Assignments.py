
#assignment 1 question 1
'''Array = ["C", "C++", "Java", "Python", "Dart"]
temp = 0
#Array = list(map(int,input("enter array : ").split()))
Shift = int(input(" Enter shift value"))
for i in range(0,Shift):
    temp = Array[0]
    Array.remove(Array[0])
    Array.append(temp)

print(Array)'''

#assignment 1 question 2
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

#assignment 2 question 1
'''matrix = [[[1,2,3], [4,5,6], [7,8,9]],
          [[10,11,12], [13, 14, 15], [16,17,180]],
          [[19,20,21], [22,23,24], [25,26,27]]]
NewList = []
for _ in range(2):
    NewList = []
    for j in range(2, -1,-1):
        temp = []
        for i in range(3):
            temp.append(matrix[i][j])
        NewList.append(temp)
    matrix = NewList
for i in NewList:
    print(i)
for i in range(3):
    for j in range(3):
        for k in range(3):
            NewList[i][j][k] = sum(NewList[i][j])//len(NewList[i][j])
print("^^^^^^^^^^^^")
for i in NewList:
    print(i)'''

#assignment 2 question 2
'''class Ticket :
   def __init__(self,name,phone,City,Source,Destination,Total):
       Customer.__init__(self,name,phone,City)
       self.Source = Source
       self.Destination = Destination
       self.Total = Total
   def ShowTicket(self,Plane):

       Customer.ShowCustomerDetails(self)
       print("Traveling From "
             "",self.Source,"To ",self.Destination)
       Plane.flight(self.Total)

class Customer(Ticket):
    def __init__(self, name, phone, City):
        self.name = name
        self.phone = phone
        self.City = City

    def ShowCustomerDetails(self):
        print("^^^^^^^^^^^^^^^^^^^^^^^")
        print(" Final details are : ")
        print("Name : ", self.name)
        print("Phone  : ", self.phone)
        print("Residence city : ", self.City)

class Flight:
    pass
class ClassA(Flight):
    def flight(self,price):
        print("A Class flight booked for ", price)
class ClassB(Flight):
    def flight(self,price):
        print("B Class flight booked for ", price)
class ClassC(Flight):
    def flight(self,price):
        print("C Class flight booked for ", price)

name  = input("Enter your name : ")
phnum  = input("Enter your Phone Number  : ")
residence  = input("Enter your residence city  : ")
Source  = input("Enter source city  : ")
desti  = input("Enter Destination city  : ")
abc = True
while abc:
    Class  = input("Enter Type of Flight you want (A,B,C)  : ")
    if Class == "A":
        Tot = 20000
        abc =False
    elif Class == "B":
        Tot = 15000
        abc = False
    elif Class == "C":
        Tot = 10000
        abc = False
    else:
        print("Wrong input ! Please Enter valid Letter ")

obj = ClassA()
ticket = Ticket(name,phnum,residence,Source,desti,Tot)
ticket.ShowTicket(obj)'''
#assingnment 3 question 1(a)
'''
def check(s):
    try:
        int(s)
        return True
    except:
        return False

string1 = "(3.1+6*2   ∧  2)  *  (    2.153   -   1))"
string = string1.replace(" ","")
lis = []
i = 0
while i < len(string):
    a = check(string[i])
    if a:
        index1 = i
        i += 1
        if string[i] == ".":

            i += 1
            while check(string[i]):
                i += 1
            index2 = i

            lis.append(float(string[index1:index2]))
        else:
            lis.append(float(string[i-1]))
    else:
        lis.append(string[i])
        i += 1



print(lis)'''

#assignment 3 question 1(b)
'''
def hasprecedence(op1,	op2):
    if (op1 == "*" or op1 == "/" or op1 == "^") and (op2 == "+" or op2 == "-"):
        return True
    else:
        return False
print(hasprecedence("/","+"))'''

#Floor and ciel of a value without inbuilt functions !
'''
a = 100.1
print("floor is : ", int(a))
print("ceil is : ", int(a)+1)
'''
#walking through a file and checking what type of file is it
'''import random as rd
import os
files = []
# print(files)
for _, _, c in os.walk("C:/Users/Arsh/Downloads"):
    for i in c:
        if i.endswith("mp3"):
            files.append(i)
print(files)'''

#program to define has a relationaship
'''class Order :
    def __init__(self, items):
        self.items = items
    def ShowSortedItems(self):
        dictonary = {}
        for i in self.items:
            dictonary[i.price]= i.item
        print("<----Items when sorted ----->")
        for i in sorted(dictonary):
            print(" item - ",dictonary[i],"|||| price - ",i)
    def getTotalAmount(self):
        sum = 0
        for i in self.items:
            sum = sum + i.price
        return sum
    def ShowData(self):
        for j in self.items:
            j.showItemsAndPrice()
    def applyPromoCode(self):
        AmountToPay = 0
        Discout = 0
        Promo = ""
        if Total < 500:
            AmountToPay = Total
            print("No Promocode Available")
            print("Final Amount To Pay : ", AmountToPay)
            exit(0)

        def PromoCode(total):
            if total >= 500 and total <= 1000:
                print("Apply ' FLAT30 ' promocode to get 30% discount ")
                print("------------------------------------------------")

            elif total > 1000:
                print("Apply ' FLAT50 ' promocode to get 50% discount ")
                print("------------------------------------------------")

        PromoCode(Total)
        while True:
            Promo = input("Enter Promocode : ")
            if Total >= 500 and Total <= 1000 and Promo == "FLAT30":
                print("Promocode Applied Successfully")
                print("------------------------------------------------")
                AmountToPay = Total - (.3 * Total)
                print("Actual Amount : ", Total)
                print("Discount : ", .3 * Total)

                print("Final Amount To Pay : ", AmountToPay)
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
                print()

class FoodItems:
    def __init__(self,item,price):

        self.item = item
        self.price = price

    def showItemsAndPrice(self):
        print("item is : ", self.item," - ","price is : ", self.price)
        print()
Cart = []
Total = 0
AddMore = "yes"
while AddMore == "yes":
    f1 = FoodItems(None, None)
    f1.item = input("Enter name of food item : ")
    f1.price = int(input("Enter price of the item : "))
    Total += f1.price
    Cart.append(f1)
    AddMore = input("Would you like to add another Address(yes/no): ")

c1 = Order(Cart)
print("----------------")
c1.ShowData()
print("^^^^^^^^^^^^^^^")
c1.ShowSortedItems()
print("----------")
print("Total is : ", c1.getTotalAmount())
print("----------")
c1.applyPromoCode()'''



#is a relationship
'''class Laptop :
    def __init__(self,RAM,HardDrive):
        self.HardDrive = HardDrive
        self.RAM = RAM

    def ShowLaptopDetails(self):
        print("^^^^^^^^^^^^^^^^")
        print("HARDRIVE SIZE IS : " ,self.HardDrive)
        print("ram size is : " , self.RAM)


class Dell(Laptop):
    def __init__(self,RAM,HardDrive,Processor,Logo):
        Laptop.__init__(self, RAM, HardDrive)
        self.Processor = Processor
        self.Logo = Logo
    def ShowDellDetails(self):
        Laptop.ShowLaptopDetails(self)

        print("Processor  IS : ", self.Processor)
        print("Logo is : ", self.Logo)
        print("^^^^^^^^^^^^^^^^")

class Acer(Laptop):
    def __init__(self,RAM,HardDrive,Name,Speed):
        Laptop.__init__(self, RAM, HardDrive)
        self.Name = Name
        self.Speed = Speed
    def ShowAcerDetails(self):
        Laptop.ShowLaptopDetails(self)

        print("Name  IS : ", self.Name)
        print("Speed is : ", self.Speed)
        print("^^^^^^^^^^^^^^^^")
dell = Dell(4 , 128 , "i5 8th gen","DELL")
dell.ShowDellDetails()
acer = Acer(6,500,"ACER", " 1.67 GHz")
acer.ShowAcerDetails()'''

# import datetime as dt
#
# print(dt.datetime.today())
# tomo = dt.datetime(2019,6,17,2,56,45)
# print(tomo)
# print(dt.datetime.today() - tomo)
