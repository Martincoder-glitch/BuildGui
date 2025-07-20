from tkinter import*
import calendar
root=Tk()#screen
root.geometry("500x500")
root.title("MY APP")
root.config(background="MediumOrchid4")
def show():
    root1=Tk()#screen
    root1.geometry("500x500")
    root1.title("MY APP")
    root1.config(background="MediumOrchid4")
    user=int(yr.get())
    content=calendar.calendar(user)
    cal=Label(root1,text=content,justify="right",font=("times",20,"bold"))
    cal.grid(row=1,column=1)
    root1.mainloop()

#title
Cal=Label(root,text="Calendar app",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal.grid(row=1,column=1)
Cal1=Label(root,text="Enter your year",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal1.grid(row=2,column=1)
yr=Entry()
yr.grid(row=3,column=2)
submit=Button(root,text="Show Calender",fg="RoyalBlue1",bg="maroon",command=show)
submit.grid(row=4,column=2,pady=10)
Exit=Button(root,text="Exit",fg="RoyalBlue1",bg="maroon",command=exit)
Exit.grid(row=5,column=2,pady=10)
root.mainloop()
