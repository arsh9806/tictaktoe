from tkinter import *
from Mysql import *
from tkinter import messagebox

import tkinter.ttk as ttk
import tkinter.font as tkFont


window = Tk()
window.title("Database Manager")
window.geometry("1100x500")
#Labels and entries
labelName = Label(text="Enter name :").grid(column=0, row=1,columnspan=3)
name_text = StringVar()
entryName = Entry(window, textvariable=name_text).grid(column=1, row=1)
labelClass = Label(text="Enter class :").grid(column=0, row=2, columnspan=3)
class_text = StringVar()
entryClass = Entry(window, textvariable=class_text).grid(column=1, row=2)
labelRoll = Label(text="Enter Roll number: ").grid(column=2, row=1)
roll_text = StringVar()
entryRoll = Entry(window, textvariable=roll_text).grid(column=3, row=1)
labelSec = Label(text="Enter Section: ").grid(column=2, row=2)
sec_text = StringVar()
entrySec = Entry(window, textvariable=sec_text).grid(column=3, row=2)
#Listbox
tree1 = ttk.Treeview(window, height=10)
tree1['columns'] = ('name','roll','sec')
tree1.grid(row=3, column=0, rowspan=6, columnspan=2,sticky='nsew')
tree1.heading('#0', text="Name")
tree1.heading('#1', text="Class")
tree1.heading('#2', text="Roll NO.")
tree1.heading('#3', text="Section")
i=0
def Insert_value():
    if name_text.get() == "" or\
            class_text.get() == "" or\
            roll_text.get() == "" or \
            sec_text.get() == "":
        messagebox.showerror("Feilds Empty", "Enter Some values")
    else:
        tree1.insert('', 'end', text=name_text.get(), values=(class_text.get(), roll_text.get(), sec_text.get()))
def delete():
    selected_item = tree1.selection() ## get selected item
    if not selected_item:
        messagebox.showerror("Not Selected", "Select some item!")
    else:
        msg = messagebox.askokcancel("Delete Entry", "This Entry will be deleted!")
        print(msg)
        if msg == 1:
            for i in selected_item:
                tree1.delete(i)
def Close():
    msg = messagebox.askquestion("Exit?","Are you sure you want to exit?")
    if msg == "yes":
        exit(0)

def update():
    tree1.item(tree1.selection())['values'][0] = 1
    print(tree1.item(tree1.selection()))
    tree1.update_idletasks()
#     newwin = Tk()
#     newwin.title("Update Record")
#     newwin.geometry("300x300")
#
#     namelbl = Label(newwin,text = "Enter name : ", width=20).grid(column=1, row=1)
#     classlbl = Label(newwin,text = "Enter class : ", width=20).grid(column=1, row=2)
#     rolllbl = Label(newwin,text = "Enter roll Num : ", width=20).grid(column=1, row=3)
#     sectionlbl = Label(newwin,text = "Enter Section : ", width=20).grid(column=1, row=4)
#     UpButton = Button(text="Save changes!",command= lambda: edit_records(ntry.get(),ctry.get(),rtry.get(),stry.get()))
#     ntry = Entry(newwin).grid(row=1, column=2)
#     ctry = Entry(newwin).grid(row=2, column=2)
#     rtry = Entry(newwin).grid(row=3, column=2)
#     stry = Entry(newwin).grid(row=4, column=2)
#     newwin.mainloop()
# def edit_records(ntry,ctry,rtry,stry):








#ScrollBar Attached to listBox(list1)
sb1 = Scrollbar(window)
sb1.grid(row=3, column=2, rowspan=5)
tree1.configure(yscrollcommand=sb1.set)
sb1.configure(command=tree1.yview)

#Buttons
viewAll = Button(text="View All",width=12)
viewAll.grid(row=3, column=3)
SearchEntry = Button(text="Search Entry", width=12).grid(row=4, column=3)
AddEntry = Button(text="Add Entry",width=12,command = Insert_value).grid(row=5, column=3)
UpdateSelected = Button(text="Update Selected",width=12,command=update).grid(row=6, column=3)
DeleteSelected = Button(text="Delete Selected",width=12,command=delete).grid(row=7, column=3)
Close = Button(text="Close",width=12,command=Close).grid(row=8, column=3)
window.mainloop()