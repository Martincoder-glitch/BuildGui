from tkinter import *
from time import strftime
import random
root=Tk()#screen
root.geometry("500x500")
root.title("Digital clock")
root.config(background="maroon")
colors=["cornflower blue","lemon chiffon","Violet Red4","gainsboro"]

    
def show_time():
    string=strftime("%A/%m/%y\n%H:%M:%S")
    root.config(background=colors[random.randint(0,3)])

    Cal.config(text=string)
    root.config(background=colors[random.randint(0,3)])
    Cal.after(1000,show_time)
Cal=Label(root,text="Clock",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal.grid(row=1,column=3)
show_time()
root.mainloop()