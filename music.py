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
    file=filedialog.askopenfilenames(filetypes=[("Audio Files","*.mp3 *.wav *.ogg")])
    if file:
        playlist=list(file)
        current_index=0
        Cal1.config(text=os.path.basename(playlist[current_index]))
def play_music():        
    global paused
    global current_song
    global current_index
    global playlist
    if paused==False:
        current_song=playlist[current_index]
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
    elif paused==True:
        pygame.mixer.music.unpause()
        paused=False
def stop_music():
    pygame.mixer.music.stop()
def pause_music():
    global paused
    paused=True
    pygame.mixer.music.pause()
def next_music():
    global playlist
    global current_index
    if current_index<len(playlist):
        current_index+=1
        play_music()
        Cal1.config(text=os.path.basename(playlist[current_index]))
def prev_music():
    global playlist
    global current_index
    if current_index>0:
        current_index-=1
        play_music()
        Cal1.config(text=os.path.basename(playlist[current_index]))
def set_volume(value):
    volume=int(value)/100
    pygame.mixer.music.set_volume(volume)
Cal=Label(root,text="Music Player",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal.grid(row=1,column=1,padx=45)
Cal1=Label(root,text="No Song Loaded",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal1.grid(row=2,column=1,pady=20)
submit=Button(root,text="Load",fg="RoyalBlue1",bg="maroon",command=load_music)
submit.grid(row=3,column=1,pady=20)
submit1=Button(root,text="Play",fg="RoyalBlue1",bg="maroon",command=play_music)
submit1.grid(row=3,column=2,pady=20)
submit2=Button(root,text="Pause",fg="RoyalBlue1",bg="maroon",command=pause_music)
submit2.grid(row=4,column=1,pady=20)
submit3=Button(root,text="Stop",fg="RoyalBlue1",bg="maroon",command=stop_music)
submit3.grid(row=4,column=2,pady=20)
submit4=Button(root,text="Prev",fg="RoyalBlue1",bg="maroon",command=prev_music)
submit4.grid(row=5,column=1,pady=20)
submit5=Button(root,text="Next",fg="RoyalBlue1",bg="maroon",command=next_music)
submit5.grid(row=5,column=2,pady=20)
Cal2=Label(root,text="Volume",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
Cal2.grid(row=6,column=1)
bar=Scale(root,from_=0,to=100,orient=HORIZONTAL,command=set_volume)
bar.grid(row=7,column=1,padx=10)

root.mainloop()