#!/usr/bin/python
from tkinter import *
from gtts import gTTS
import os

root = Tk()

def close(root):
    root.destroy()

def save():
    text = entry.get() + ". \n"
    with open("info.txt", "a") as f:
        f.write(text)

def show():
    file = open("info.txt")
    data = file.read()
    Results = Label(root, bg="white", fg="blue", width="60",  text=data)
    Results.grid(row = 5, columnspan=7)

def speak():
    file1 = "asd.mp3"
    lang = "el"
    fileop = open("info.txt")
    name = fileop.read()
    tts = gTTS(name, lang)
    tts.save(file1)
    os.system("mpv " + file1)




exit = Button(root, text="Exit", bg="white", fg="purple", command=root.destroy)


slist = Label(root, text="Shopping list", bg="blue", width="60", fg="white")
slist.grid(row=0, column=0, columnspan=7, sticky=W)

seist = Label(root, text="item list", bg="blue", width="60", fg="white")
seist.grid(row=3, column=0, columnspan=7, sticky=W)

label = Label(root, text=" item ", fg="red")
entry = Entry(root)

exit.grid(row=1, column=6)
entry.grid(row=1, column=0, columnspan=2)
label.grid(row=1, column=2, columnspan=1, sticky=W)


save = Button(root, text="Save", bg="white", fg="black", command=save)
save.grid(row=1, column=3)

speak = Button(root, text="Speak", bg="white", fg="black", command=speak)
speak.grid(row=1, column=4)


showbutton = Button(root, text="Show", bg="white", fg="black", command=show)
showbutton.grid(row=1, column=5)

slist = Label(root, text="end of Shopping list", bg="blue", width="60", fg="white")
slist.grid(row=6, column=0, columnspan=7, sticky=W)



root.mainloop()

