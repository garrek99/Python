# pip install pyttsx3
import pyttsx3

engine = pyttsx3.init()
this = "This has been a lovely course in Python. I have learned the fundamentals of Python thanks to this course!"
engine.say(this)
engine.runAndWait()