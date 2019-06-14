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
class Order :
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
c1.applyPromoCode()


'''class Address:

    # Constructor for Standardization
    def __init__(self, adrsLine, city, state):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state

    # Function : Update Operation
    def updateAddressDetails(self, adrsLine, city, state):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state

    # Function : Read Operation
    def showAddressDetails(self):
        print("=================")
        print("AdrsLine:\t",self.adrsLine)
        print("City:\t", self.city)
        print("State:\t", self.state)
        print("=================")


adrsList = []
choice = "yes"
while choice == "yes":
    adrs = Address(None, None, None)
    adrs.adrsLine = input("Enter Address Line: ")
    adrs.city = input("Enter City: ")
    adrs.state = input("Enter State: ")
    adrsList.append(adrs)

    choice = input("Would you like to add another Address(yes/no): ")
for i in adrsList:
    i.showAddressDetails()'''