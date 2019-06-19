import mysql.connector
class DBhandler:
    def SaveDetailsinDB(self,customer):
        sql = "insert into Users values(null,'{}','{}','{}')".format(customer.name,customer.phone,customer.email)
        con = mysql.connector.connect(user="root", password="", host="localhost",database = "NewDB")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Details of ",customer.name,"saved into database")

    def UpdateDetailsinDB(self,customer):
        sql = "Update Users set name = '{}',phone = '{}',email = '{}' where cid = {}" .format(customer.name,customer.phone,customer.email,customer.cid)
        con = mysql.connector.connect(user="root", password="", host="localhost",database = "NewDB")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        customer.ShowDetails()
        print("Entry Updated!!")

    def DeleteDetailsinDB(self,cid):
        sql = "delete from Users where cid = {}".format(cid)
        con = mysql.connector.connect(user="root", password="", host="localhost",database = "NewDB")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Entry Deleted!!")
class Users :
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    def ShowDetails(self):
        print("Name is : ",self.name)
        print("phone is : ",self.phone)
        print("email is : ",self.email)
print("1. Add New Customer ")
print("2. Update Existing Customer ")
print("3. Delete Customer ")

Choice = input(" Select from above : ")
if Choice == "1":

    user = Users(None,None,None)
    user.name = input("Enter Name : ")
    user.phone = input("Enter phone number  : ")
    user.email = input("Enter email  : ")
    user.ShowDetails()
    save = input("Do you want to save this Data (y/n) :  ")
    if save == "y":
        db = DBhandler()
        db.SaveDetailsinDB(user)
elif Choice == "2":
    user = Users(None, None, None)
    user.cid = input("Enter Customer ID : ")
    user.name = input("Enter New Name : ")
    user.phone = input("Enter New phone number  : ")
    user.email = input("Enter New email  : ")
    user.ShowDetails()
    save = input("Do you want to Update this Data (y/n) :  ")
    if save == "y":
        db = DBhandler()
        db.UpdateDetailsinDB(user)
elif Choice == "3":
    user = Users(None, None, None)
    user.cid = input("Enter Customer ID To Delete : ")
    save = input("Do you want to Delete this Id (y/n) :  ")
    if save == "y":
        db = DBhandler()
        db.DeleteDetailsinDB(user.cid)
