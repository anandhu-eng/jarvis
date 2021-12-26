import pyttsx3
from speech_commands import *
from mic_commands import *
import wikipedia
import webbrowser
from todo import *
#if you are using linux, install espeak also---> sudo apt-get update && sudo apt-get install espeak

engine=pyttsx3.init()
voice=engine.getProperty("voices")
engine.setProperty('rate', 100)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)   #volume 0-1
engine.setProperty('voice', voice[11].id)		#english voice
#print(voice[10].id)----> to print the language of the voice

#engine.say("Hello, how are you")
#engine.runAndWait()
if __name__=="__main__":
	wish()
	while True:
		query=takeCommand().lower()
		if query=="None":
			say("Say that again please...")
		elif 'wikipedia' in query:
			say("Searching wikipedia...")
			query=query.replace("wikipedia","")
			results=wikipedia.summary(query, sentences=2)
			print(results)
			say("According to wikipedia,"+results)

		elif 'search' in query:
			if "youtube" in query:
				say("Opening youtube....")
				query=query.replace("search youtube","")
				webbrowser.open("https://www.youtube.com/results?search_query={query}".format(query=query))
			elif 'google' in query:
				say('Opening Google....')
				query=query.replace("search google","")
				webbrowser.open("https://www.google.com/search?q={query}".format(query=query))
		
		elif 'add task' in query:
			say("The feature will be comming soon!")
			query=query.replace("add task","")
			add_task(query)

		elif 'view pending tasks' in query:
			#say("The feature will be comming soon!")
			pending_task()
			
		elif 'shutdown jarvis' in query:
			say("Shutting down sir, do call me for assisting you!")
			break


