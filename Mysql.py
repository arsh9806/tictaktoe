import mysql.connector
class DBhandler:
    def SaveDetailsinDB(self,customer):
        sql = "insert into Users values(null,'{}','{}','{}')".format(customer.name,customer.phone,customer.email)
        con = mysql.connector.connect(user="root", password="", host="localhost",database = "NewDB")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Details of ",customer.name,"saved into database")
class Users :
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    def ShowDetails(self):
        print("Name is : ",self.name)
        print("phone is : ",self.phone)
        print("email is : ",self.email)


user = Users(None,None,None)
user.name = input("Enter Name : ")
user.phone = input("Enter phone number  : ")
user.email = input("Enter email  : ")
user.ShowDetails()
save = input("Do you want to save this Data (y/n) :  ")
if save == "y":
    db = DBhandler()
    db.SaveDetailsinDB(user)