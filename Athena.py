from tkinter.constants import ANCHOR, CENTER, HIDDEN
from typing import Text
import wolframalpha
import tkinter as tk
import pyttsx3


#Imported package shit
client = wolframalpha.Client('RXVYYY-PEGUVQT4KK')
engine = pyttsx3.init()

#Window Initialization big time
window = tk.Tk()
window.title("Athena")
window.configure(background="white")
window.geometry("1920x1080")

background_label = tk.Label(window)
background_label.place(x=0,y=0,relwidth=1,relheight=1)


#Athena Label
Label_assist = tk.Label(window, text="Athena", bg="white",fg="black",font="Arial 32 bold")
Label_assist.place(relx = 0.5,rely = 0.4, anchor = CENTER)


#Text entry box
textentry = tk.Entry(window, width=20, bg ="white")
textentry.place(relx=0.5,rely=0.5,anchor = CENTER)  

#Answer Label
LabelResult = tk.Label(window, text = "lol",bg="white",fg="black",font="Arial 20 bold")

#Function for searching shit up foo
def click():
    entered_text=textentry.get()
    res = client.query(entered_text)
    Wolfram_result = next(res.results).text
    LabelResult.place(relx=0.5,rely=0.7,anchor = CENTER)
    LabelResult.config(text=Wolfram_result)
    engine.say(Wolfram_result)
    engine.runAndWait()

#The button
tk.Button(window,text="Enter",width=5, command=click).place(relx = 0.5,rely = 0.55, anchor = CENTER)

window.mainloop()


