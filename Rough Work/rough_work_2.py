name = "Muzamil"
a = name[2]
print(a)

import pyjokes
import os
import pyttsx3

jokes = pyjokes.get_joke()
print(jokes)

engine = pyttsx3.init()
engine.say("Hello Everyone, Today I am goig to write this program and you all will see how fast , I write and read ")
engine.runAndWait()