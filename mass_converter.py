from tkinter import *
root=Tk()#screen
root.geometry("500x500")
root.title("MY APP")
root.config(background="maroon")
def converter():
    Gram=int(yr.get())
    kg=Gram/1000  
    Cal.config(text=f"weight in kg-{kg}")
Mass=Label(root,text="Gram-->kilogram",fg="royal blue",bg="CadetBlue1",font=("times",28,"bold"))
Mass.grid(row=1,column=1)
Cal1=Label(root,text="Enter weight",fg="royal blue",bg="CadetBlue1",font=("times",28,"bold"))
Cal1.grid(row=2,column=1)
yr=Entry()
yr.grid(row=2,column=2)
Cal=Label(root,text="weight in kilograms",fg="royal blue",bg="CadetBlue1",font=("times",28,"bold"))
Cal.grid(row=3,column=1)
submit=Button(root,text="convert weight",fg="RoyalBlue1",bg="maroon",comman=converter)
submit.grid(row=4,column=1,pady=10)
root.mainloop()