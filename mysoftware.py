import os
import pyttsx3

pyttsx3.speak("Hey , Welcome to my pc")
pyttsx3.speak("What's your name")
name = input("What's your name  : ")

pyttsx3.speak("Nice to meet you "+name)
pyttsx3.speak("Here is the menu ")

print("launch chrome")
print("launch Notepad")
print("launch Windows Media Player")
print("launch calculator")
print("Visit any website")


while(8):
	pyttsx3.speak("Can you please tell me your requirements")
	req = input("\nCan you please tell me your requirements  :  ")

	if (("run" in req) or ("execute" in req) or ("open" in req) or ("launch" in req)) and ("chrome" in req):
		pyttsx3.speak("Opening chrome")
		os.system("chrome")
	elif (("run" in req) or ("execute" in req) or ("open" in req) or ("launch" in req)) and ("notepad" in req):
		pyttsx3.speak("Opening notepad")
		os.system("notepad")
	elif (("run" in req) or ("execute" in req) or ("open" in req) or ("launch" in req)) and ("player" in req):
		pyttsx3.speak("Opening Windows Media Player")
		os.system("wmplayer")
	
	elif (("run" in req) or ("execute" in req) or ("open" in req) or ("launch" in req)) and ("calculator" in req):
		pyttsx3.speak("Opening Calculator")
		os.system("calc")
	
	elif "www" in req:
		pyttsx3.speak("Opening Website")
		os.system("chrome/req")
	elif "exit" in req:
		exit()
	else:	
		#pyttsx3("Please enter the right choice")
		print("Please enter the right choice ")
