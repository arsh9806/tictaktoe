from tkinter import *
def onclick():
    print("Button pressed!")


window = Tk()
lableTitle = Label(window, text="Add Customer Details")
lableTitle.pack()


lblname = Label(window, text="Enter user's name below : ")
lblname.pack()
entryname = Entry(window)
entryname.pack()
lblphone = Label(window, text="Enter users name below : ")
lblphone.pack()
entryphone = Entry(window)
entryphone.pack()
lbemail = Label(window, text="Enter users name below : ")
lbemail.pack()
entryemail = Entry(window)
entryemail.pack()
but = Button(text = "Add details",command = onclick)
but.pack()

window.mainloop() #KEEP ON RUNNING THE PROGRAM