from tkinter import *
from tkinter import filedialog
import pygame
pygame.mixer.init()
import os
current_song=""
paused=False
current_index=0
playlist=[]
root=Tk()#screen
root.geometry("500x500")
root.title("MY APP")
root.config(background="maroon")
def load_music():
    global current_song
    global current_index
    global playlist
    file=filedialog.askopenfilename(filetypes=[("Audio Files","*.mp3 *.wav *.ogg")])

Cal=Label(root,text="Music Player",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal.grid(row=1,column=1,padx=45)
Cal1=Label(root,text="No Song Loaded",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal1.grid(row=2,column=1,pady=20)
submit=Button(root,text="Load",fg="RoyalBlue1",bg="maroon")
submit.grid(row=3,column=1,pady=20)
submit1=Button(root,text="Play",fg="RoyalBlue1",bg="maroon")
submit1.grid(row=3,column=2,pady=20)
submit2=Button(root,text="Pause",fg="RoyalBlue1",bg="maroon")
submit2.grid(row=4,column=1,pady=20)
submit3=Button(root,text="Stop",fg="RoyalBlue1",bg="maroon")
submit3.grid(row=4,column=2,pady=20)
submit4=Button(root,text="Prev",fg="RoyalBlue1",bg="maroon")
submit4.grid(row=5,column=1,pady=20)
submit5=Button(root,text="Next",fg="RoyalBlue1",bg="maroon")
submit5.grid(row=5,column=2,pady=20)
Cal2=Label(root,text="Volume",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal2.grid(row=6,column=1)
bar=Scale(root,from_=0,to=100,orient=HORIZONTAL)
bar.grid(row=7,column=1,padx=10)

root.mainloop()