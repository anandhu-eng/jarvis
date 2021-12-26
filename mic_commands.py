import speech_recognition as sr

def takeCommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening....")
		r.pause_threshold=1 #pauses for 1 second before executing a command so that nothing gets missed.
		audio=r.listen(source)

	try:
		print("Recognising...")
		query = r.recognize_google(audio, language='en-in')
		print("User said:",query)
	except Exception as e:
		print(e)
		print("Say that again please....")
		return "None"
	return query
