from tkinter import *
from gtts import gTTS
from translate import Translator
import os
root=Tk()#screen
root.geometry("500x500")
root.title("Text to Speech Translator")
root.config(background="maroon")
cal=Label(root,text="Text to Speech Translator",fg="royal blue",bg="MediumOrchid4",font=("times",28,"bold"))
cal.grid(row=1,column=1)
yr=Entry(root,width=75)
yr.grid(row=2,column=1,pady=25)
selection=StringVar(value="ja")
r1=Radiobutton(root,text="Japanese",variable=selection,value="ja")
r1.grid(row=3,column=1)
r2=Radiobutton(root,text="French",variable=selection,value="fr")
r2.grid(row=4,column=1,pady=25)
r3=Radiobutton(root,text="German",variable=selection,value="de")
r3.grid(row=5,column=1,pady=25)
r4=Radiobutton(root,text="Spanish",variable=selection,value="es")
r4.grid(row=6,column=1,pady=25)
r5=Radiobutton(root,text="Russian",variable=selection,value="ru")
r5.grid(row=7,column=1,pady=25)
def start():
    translator=Translator(to_lang=selection.get())
    text_to_translate=yr.get()
    translated_text=translator.translate(text_to_translate)
    sound=gTTS(text=translated_text,lang=selection.get())
    sound.save("text.mp3")
sumbit=Button(root,text="Submit",fg="RoyalBlue1",bg="maroon",font=("times",28,"bold"),command=start)
sumbit.grid(row=6,column=2)
root.mainloop()