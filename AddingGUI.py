from tkinter import *
from Mysql import *
from tkinter import messagebox

def AddDetails():
    user = Users(None, None, None)
    user.name = f1entryname.get()
    user.phone = f1entryphone.get()
    user.email = f1entryemail.get()
    if user.name == "" or user.phone == "" or user.email == "":
        messagebox.showerror("Feild empty!", "Enter data!")
    else:
        user.ShowDetails()
        db = DBhandler()
        msg = messagebox.askquestion("Save Data", "Do you want to Save this Data?")
        if msg == "yes":
            db.SaveDetailsinDB(user)
            messagebox.showinfo("DONE!", "Data Saved.")
            f1entryname.delete(0, END)
            f1entryphone.delete(0, END)
            f1entryemail.delete(0, END)





window = Tk()
frame1 = LabelFrame(window,text="Adding A Record")

window.title("Database Management")
window.geometry("1250x1250")
#Adding new Customer
f1lableTitle = Label(frame1, text="Add Customer Details", font=("Arial Bold", 10), fg="white", bg="black")

#f1rb = Radiobutton(text="Add New User",value = 1)

f1lblname = Label(frame1, text="Enter user's name below : ",font=("Arial Bold",10))

f1entryname = Entry(frame1)

f1lblphone = Label(frame1, text="Enter user's Phone no. below : ",font=("Arial Bold",10))

f1entryphone = Entry(frame1)

f1lbemail = Label(frame1, text="Enter user's Email ID below : ",font=("Arial Bold",10))

f1entryemail = Entry(frame1)

f1but = Button(frame1,text="Add details", command=AddDetails, fg="red")
f1lableTitle.grid(column=1, row=0)
#f1rb.grid(column=1, row=1)
f1lblname.grid(column=1, row=3)
f1entryname.grid(column=1, row=4)
f1lblphone.grid(column=1, row=5)
f1entryphone.grid(column=1, row=6)
f1lbemail.grid(column=1, row=7)
f1entryemail.grid(column=1, row=8)
f1but.grid(column=1, row=9)
frame1.grid(row=0)



#Updating Exsiting Customer Details!

def UpdateDetails():
    user = Users(None, None, None)
    user.cid = f2Entrycid.get()
    user.name = f2entryname.get()
    user.phone = f2entryphone.get()
    user.email = f2entryemail.get()
    if user.name == "" or user.phone == "" or user.email == "" or user.cid == "":
        messagebox.showerror("Feild empty!", "Enter data!")
    else:
        user.ShowDetails()
        db = DBhandler()
        msg = messagebox.askquestion("Update Data", "Do you want to Update this Data?")
        if msg == "yes":
            db.UpdateDetailsinDB(user)
            messagebox.showinfo("DONE!", "Data Updated.")


frame2 = LabelFrame(window,text="Updating a Record")
f2lblTitle = Label(frame2, text="Updating Details", font=("Arial Bold", 10),fg="white", bg="black")
f2lblcid = Label(frame2,text="Enter CID below ",font=("Arial Bold",10))
f2Entrycid = Entry(frame2)
f2lblname = Label(frame2, text="Enter user's name below : ",font=("Arial Bold",10))
f2entryname = Entry(frame2)
f2lblphone = Label(frame2, text="Enter user's Phone no. below : ",font=("Arial Bold",10))
f2entryphone = Entry(frame2)
f2lbemail = Label(frame2, text="Enter user's Email ID below : ",font=("Arial Bold",10))
f2entryemail = Entry(frame2)
f2but = Button(frame2,text="Update details", command=UpdateDetails, fg="red")
frame2.grid(column=1,row=0)

f2lblTitle.grid(column=2, row=1)
f2lblcid.grid(column=2, row =4)
f2Entrycid.grid(column=2,row=5)
f2lblname.grid(column=2,row=6)
f2entryname.grid(column=2, row=7)
f2lblphone.grid(column=2, row=8)
f2entryphone.grid(column=2, row=9)
f2lbemail.grid(column=2, row=10)
f2entryemail.grid(column=2, row=11)
f2but.grid(column=2, row=12)

#fetching all

window.mainloop() #KEEP ON RUNNING THE PROGRAM