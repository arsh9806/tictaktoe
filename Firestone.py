from tkinter import *
from Mysql import *
from tkinter import messagebox

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('PrivateKey.json')
firebase_admin.initialize_app(cred)



def AddDetails():
    user = Users(None, None, None)
    user.name = entryname.get()
    user.phone = entryphone.get()
    user.email = entryemail.get()
    if user.name == "" or user.phone == "" or user.email == "":
        messagebox.showerror("Feild empty!", "Enter data!")
    else:
        user.ShowDetails()
        db = firestore.client()
        msg = messagebox.askquestion("Save Data", "Do you want to Save this Data?")
        if msg == "yes":
            data = user.__dict__
            db.collection("Users").document().set(data)

            messagebox.showinfo("DONE!", "Data Saved.")
window = Tk()
frame1 = Frame(window)
window.title("Database Management")
window.geometry("1250x1250")
#Adding new Customer
lableTitle = Label(frame1, text="Add Customer Details", font=("Arial Bold", 20), fg="white", bg="black")
lableTitle.grid(column=1, row=2)
rb = Radiobutton(text="Add New User",value = 1)
rb.grid(column=1, row=1)

lblname = Label(frame1, text="Enter user's name below : ",font=("Arial Bold",10))
lblname.grid(column=1, row=3)

entryname = Entry(frame1)
entryname.grid(column=1, row=4)
lblphone = Label(frame1, text="Enter user's Phone no. below : ",font=("Arial Bold",10))
lblphone.grid(column=1, row=5)
entryphone = Entry(frame1)
entryphone.grid(column=1, row=6)
lbemail = Label(frame1, text="Enter user's Email ID below : ",font=("Arial Bold",10))
lbemail.grid(column=1, row=7)
entryemail = Entry(frame1)
entryemail.grid(column=1, row=8)
but = Button(frame1,text="Add details", command=AddDetails, fg="red")
but.grid(column=1, row=9)
frame1.grid(row=0,column=0)
#Updating Exsiting Customer Details!

window.mainloop() #KEEP ON RUNNING THE PROGRAM