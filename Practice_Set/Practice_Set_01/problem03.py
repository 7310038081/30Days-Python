#3.Install an external module and use it to perform an operation of your interest
#pip install pyttsx3(text to speech)
import pyttsx3
engine = pyttsx3.init()
engine.say("My Name is Vivek Singh.Nice to meet you !")
engine.runAndWait()
