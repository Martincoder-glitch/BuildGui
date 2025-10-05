from tkinter import *
root=Tk()#screen
from tkinter import messagebox
from tkinter.filedialog import *
root.geometry("500x500")
root.title("address book")
root.config(background="maroon")
myAddressBook={}
def clear_all():
    yr1.delete(0,END)
    yr2.delete(0,END)
    yr3.delete(0,END)
    yr4.delete(0,END)
    yr5.delete(0,END)
def add_items():
    Key=yr1.get()
    if Key=="":
        messagebox.showinfo("Error","Name cannot be empty")
    else :
        if Key not in myAddressBook.keys():
            listbox.insert(END,Key)
        myAddressBook[Key]=( yr1.get(),yr2.get(),yr3.get(),yr4.get(),yr5.get())
        clear_all()
def edit_items():
    clear_all()
    index=listbox.curselection()
    if index:
        yr1.insert(0,listbox.get(index))
        data=myAddressBook[yr1.get()]
        yr2.insert(0,data[1])
        yr3.insert(0,data[2])
        yr4.insert(0,data[3])
        yr5.insert(0,data[4])
    else:
        messagebox.showinfo("Error","the boxes cannot be empty")
def delete_items():
    index=listbox.curselection()
    if index:
        del myAddressBook[listbox.get(index)]
        listbox.delete(index)
def save():
    file=asksaveasfile(defaultextension=".txt")
    if file:
        print(myAddressBook,file=file)
        clear_all()
        listbox.delete(0,END)
        myAddressBook.clear()
def open():
    global myAddressBook
    clear_all()
    listbox.delete(0,END)
    myAddressBook.clear()
    file=askopenfile(title="Open File")
    if file:
        myAddressBook=eval(file.read())
        for key in myAddressBook.keys():
            listbox.insert(END,key)


Cal=Label(root,text="Addressbook ",fg="royal blue",bg="maroon",font=("times",15,"bold"))
Cal.grid(row=1,column=1,pady=25)
yr1=Entry(root,width=25)
yr1.place(x=700,y=150)
yr2=Entry(root,width=25)
yr2.place(x=700,y=200)
yr3=Entry(root,width=25)
yr3.place(x=700,y=250)
yr4=Entry(root,width=25)
yr4.place(x=700,y=300)
yr5=Entry(root,width=25)
yr5.place(x=700,y=350)
submit=Button(root,text="open",fg="RoyalBlue1",bg="maroon",command=open)
submit.grid(row=1,column=2,padx=50)
submit1=Button(root,text="add/update",fg="RoyalBlue1",bg="maroon",command=add_items)
submit1.place(x=500,y=300)
submit2=Button(root,text="save",fg="RoyalBlue1",bg="maroon",command=save)
submit2.place(x=400,y=450)
submit3=Button(root,text="delete",fg="RoyalBlue1",bg="maroon",command=delete_items)
submit3.place(x=400,y=350)
submit3=Button(root,text="Edit",fg="RoyalBlue1",bg="maroon",comman=edit_items)
submit3.place(x=350,y=350)
yr1=Entry(root,width=25)
yr1.place(x=700,y=150)
yr2=Entry(root,width=25)
yr2.place(x=700,y=200)
yr3=Entry(root,width=25)
yr3.place(x=700,y=250)
yr4=Entry(root,width=25)
yr4.place(x=700,y=300)
yr5=Entry(root,width=25)
yr5.place(x=700,y=350)
Cal5=Label(root,text="email:",fg="royal blue",bg="maroon",font=("times",15,"bold"))
Cal5.place(x=650,y=250)
Cal6=Label(root,text="adress:",fg="royal blue",bg="maroon",font=("times",15,"bold"))
Cal6.place(x=650,y=200)
Cal7=Label(root,text="name: ",fg="royal blue",bg="maroon",font=("times",15,"bold"))
Cal7.place(x=650,y=150)
Cal8=Label(root,text="mobile: ",fg="royal blue",bg="maroon",font=("times",15,"bold"))
Cal8.place(x=650,y=300)
Cal9=Label(root,text="birthday: ",fg="royal blue",bg="maroon",font=("times",15,"bold"))
Cal9.place(x=650,y=350)

frame=Frame(root)
scrollbar=Scrollbar(frame,orient="vertical")
scrollbar.pack(side=RIGHT,fill=Y)
listbox=Listbox(frame,width=70,yscrollcommand=scrollbar.set,bg="red")
listbox.pack(side=LEFT,padx=5)
scrollbar.config(command=listbox.yview)
frame.grid(row=2,column=1,padx=50,pady=50)
root.mainloop()