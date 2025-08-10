from tkinter import *
root=Tk()#screen
root.geometry("500x500")
root.title("temperature_converter")
root.config(background="snow")
def converter():
    celsius=int(yr.get())
    f=celsius*9/5+32
    Cal.config(text=f"Temperature in farenheit-{f}")
Temp=Label(root,text="Celsius-->farenheit",fg="royal blue",bg="CadetBlue1",font=("times",28,"bold"))
Temp.grid(row=1,column=1)
Cal1=Label(root,text="Enter temperature",fg="royal blue",bg="CadetBlue1",font=("times",28,"bold"))
Cal1.grid(row=2,column=1)
yr=Entry()
yr.grid(row=2,column=2)
Cal=Label(root,text="Temperature in farenheit",fg="royal blue",bg="CadetBlue1",font=("times",28,"bold"))
Cal.grid(row=3,column=1)
submit=Button(root,text="convert temp",fg="RoyalBlue1",bg="maroon",command=converter)
submit.grid(row=4,column=1,pady=10)
root.mainloop()