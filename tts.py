#!/usr/bin/python
import sys
from gtts import gTTS
import os

# defilos irthes stne variables
#s = "παρακαλω δωσε το κειμενο  " 
#file = "file.mp3"
file1 = "asd.mp3"

# initialize tts, create mp3 and play
#tts = gTTS(s, 'el')
#tts.save(file)
#os.system("mpv " + file)
#name = input("right your text : ")
name = sys.argv[1]
#a = "Your text " + name 
tts = gTTS(name, 'el')
tts.save(file1)
os.system("mpv " + file1)


