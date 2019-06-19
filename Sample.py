
class Ticket :
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
ticket.ShowTicket(obj)
