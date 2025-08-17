from tkinter import*
import random
root=Tk()#screen
root.geometry("800x500")
root.title("Rock,Paper,scissor")
root.config(background="maroon")
cs=0
ps=0
options=("Rock","Paper","Scissors")
def gameplay(player):
    global cs,ps,options
    computer=random.choice(options)
    if player==computer:
        Cal1.config(text="tie")
    elif player=="Rock"and computer=="Paper":
        Cal1.config(text="computer wins")
    elif player=="Rock"and computer=="Scissors":
        Cal1.config(text="player wins")
    elif player=="Paper"and computer=="Scissors":
        Cal1.config(text="computer wins")
    elif computer=="Rock"and player=="Paper":
        Cal1.config(text="player wins")
    elif computer=="Rock"and player=="Scissors":
        Cal1.config(text="computer wins")
    elif computer=="Paper"and player=="Scissors":
        Cal1.config(text="player wins")


Cal=Label(root,text="Rock,Paper,Scissor",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal.grid(row=1,column=2)
Cal1=Label(root,text="player",fg="green")
Cal1.grid(row=1,column=1)
Cal2=Label(root,text="Your options",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal2.grid(row=2,column=1,pady=50)
submit=Button(root,text="Paper",fg="RoyalBlue1",bg="maroon",command=lambda:gameplay("Paper"))
submit.grid(row=3,column=2,pady=10)
Rock=Button(root,text="Rock",fg="RoyalBlue1",bg="maroon",command=lambda:gameplay("Rock"))
Rock.grid(row=3,column=1,pady=10)
scissors=Button(root,text="Scissors",fg="RoyalBlue1",bg="maroon",command=lambda:gameplay("Scissors"))
scissors.grid(row=3,column=3,pady=10)
Cal3=Label(root,text="score",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal3.grid(row=4,column=1)
Cal4=Label(root,text="Your selected:",fg="royal blue",bg="maroon",font=("times",15,"bold"))
Cal4.grid(row=5,column=2)
Cal5=Label(root,text="Computer selected:",fg="royal blue",bg="maroon",font=("times",15,"bold"))
Cal5.grid(row=6,column=2,pady=25)
Cal6=Label(root,text="Computer score:",fg="royal blue",bg="maroon",font=("times",15,"bold"))
Cal6.grid(row=6,column=3)
Cal7=Label(root,text="Player score: ",fg="royal blue",bg="maroon",font=("times",15,"bold"))
Cal7.grid(row=5,column=3,pady=25)

root.mainloop()