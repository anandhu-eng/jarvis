## IMPORTING SECTION	 ##
import pyttsx3
import datetime
###########################

## ENGINE INITIALISATION ##
engine=pyttsx3.init()
voice=engine.getProperty("voices")
engine.setProperty('rate', 100)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)   #volume 0-1
engine.setProperty('voice', voice[11].id)		#english voice
############################

## FUNCTION SECTION 	  ##
def say(information):
	engine.say(information)
	engine.runAndWait()
def wish():
	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		engine.say("Good morning sir, how may i help you!")
	elif hour>=12 and hour<18:
		engine.say("Good afternoon sir, how may i help you!")
	else:
		engine.say("Good evening sir, how may i help you!")
	engine.runAndWait()
############################