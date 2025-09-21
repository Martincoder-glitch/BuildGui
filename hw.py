from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()#screen
root.geometry("500x500")
root.title("MY HOMEWORK")
root.config(background="maroon")
def greet():
    name=fav.get()

    messagebox.showinfo("order success",f"{name}-,homework selected")
Cal=Label(root,text="Homework",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal.grid(row=1,column=2)
menu=["Maths","English","German","French","DT","ART","Music"]
fav=StringVar()
homework=ttk.Combobox(root,textvariable=fav,width=20,value=fav)
homework["values"]=menu
homework.grid(row=2,column=2,padx=50)
ORDER=Button(root,text="ORDER",fg="RoyalBlue1",bg="maroon",command=greet)
ORDER.grid(row=4,column=2,padx=15)
root.mainloop()