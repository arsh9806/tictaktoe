from tkinter import *
from Mysql import *
from tkinter import messagebox


window = Tk()
window.title("Database Manager")
window.geometry("800x500")
frame = LabelFrame(window, text="Adding a User!",width=400, height=400, background="pink")
labelname = Label(frame,text="Enter name :").grid(column=1,row=1)
labelprice = Label(frame,text="Enter price :").grid(column=1,row=3)
b1 = Button(frame,text="Add Record",fg="brown").grid(column=2,row=4)
entryname = Entry(frame).grid(column=2,row=1)
entryprice = Entry(frame).grid(column=2,row=3)
frame.pack(expand=False)
window.mainloop()