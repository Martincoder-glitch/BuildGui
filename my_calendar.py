from tkinter import *
root=Tk()#screen
root.geometry("500x500")
root.title("MY APP")
root.config(background="MediumOrchid4")
#title
Cal=Label(root,text="Calendar app",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal.grid(row=1,column=1)
Cal1=Label(root,text="Enter your year",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal1.grid(row=2,column=1)
yr=Entry()
yr.grid(row=3,column=2)
submit=Button(root,text="Show Calender",fg="RoyalBlue1",bg="maroon")
submit.grid(row=4,column=2)
root.mainloop()