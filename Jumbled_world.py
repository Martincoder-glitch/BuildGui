from tkinter import *
from tkinter import messagebox
root=Tk()#screen
root.geometry("500x500")
root.title("JUMBLED WORD GAME")
root.config(background="maroon")
List=["ghoul","ghost","halloween","pumpkin","costumes","scary","monsters"]
Jumble=["loguh","tohsg","wolenelha","iunpkmp","sstocmeu","rsyca","strnseom"]
index=0
score=0
cal=Label(root,text="JUMBLED WORD GAME",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
cal.grid(row=1,column=1)
ans=StringVar()
cal1=Label(root,text=Jumble[index],fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
cal1.grid(row=2,column=1,pady=50)
yr=Entry(root,width=30,textvariable=ans)
yr.grid(row=3,column=1,pady=75)
cal2=Label(root,text=f"score:{score}",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
cal2.grid(row=2,column=2,pady=70)
def game():
    global Jumble
    global index
    global ans
    global List
    global score
    if index<len(List):
        user=ans.get()
        if user==List[index]:
            messagebox.showinfo("succes"," you got it")   
            score+=1
        else:
            messagebox.showinfo("wrong","unluck try again")   
        index+=1 
        yr.delete(0,END)
        cal1.configure(text=Jumble[index])
        cal2.configure(text=f"score:{score}")
    else:
       messagebox.showinfo("yay","your at the end pls reset") 
def reset():
    global score
    index=0
    score=0
    yr.delete(0,END)
    cal1.configure(text=Jumble[index])
    cal2.configure(text=f"score:{score}")
    messagebox.showinfo("succes","Game reseted")
submit=Button(root,text="Check",fg="RoyalBlue1",bg="maroon",command=game)
submit.grid(row=4,column=1,pady=20)
submit1=Button(root,text="Reset",fg="RoyalBlue1",bg="maroon",command=reset)
submit1.grid(row=5,column=1,pady=20)
root.mainloop()