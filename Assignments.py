
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