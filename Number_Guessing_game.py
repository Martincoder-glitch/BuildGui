from tkinter import *
import random
root=Tk()#screen
root.geometry("850x850")
root.title("MY APP")
root.config(background="maroon")
computer=None
def game():
    computer=random.randint(1,10)
    user=int(yr1.get())
Cal=Label(root,text="Welcome to our game",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal.grid(row=1,column=2)
Cal1=Label(root,text="Whats your name",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal1.grid(row=2,column=1,pady=20)
yr=Entry(root,width=75)
yr.grid(row=3,column=1,padx=50)
submit=Button(root,text="ok",fg="RoyalBlue1",bg="maroon",font=("times",28,"bold"))
submit.grid(row=3,column=2)
Cal2=Label(root,text="Take a guess",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal2.grid(row=4,column=1,pady=20)
yr1=Entry(root,width=75)
yr1.grid(row=4,column=2,padx=50)
submit1=Button(root,text="guess",fg="RoyalBlue1",bg="maroon",font=("times",28,"bold"))
submit1.grid(row=4,column=3)
root.mainloop()