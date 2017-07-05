#import adialog_new as ad
from naoqi import ALProxy
import nicoGestures as gesture
import sys

try:
	tts = ALProxy("ALTextToSpeech", "nico.d.mtholyoke.edu", 9559)
except Exception,e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ",e
	sys.exit(1)

dialog = {
	######## Introduction ########
	'1': "Hello! My name is Neeco. How are you doing today?" ,
	'2': "I'm ready to learn mahth! Do you have any problems for me to solve?",
	'3': "What problems are we solving today?",
	'4': "I want to learn how to solve this problem!",
	######## Confirmation ########
	'5': "Okay!",
	'6': "Yes!",
	'7': "Yes, I agree.",
	######## Asking Questions #######
	'8': "How do you solve this problem?",
	'9': "What do we do next?",
	'10': "How do we do that?",
	'11': "Could you give me more information?",
	'12': "Okay now we mul tip ly?",
	'13': "Okay now we add?",
	'14': "Okay so we divide?",
	'15': "Is this correct?",
	######## Confusion ########
	'16': "How did we get that number?",
	'17': "Could you break that down into parts?",
	'18': "Hmmm. That part seems complicated to me. Can you explain that again?",
	'19': "I don't know. Could you give me some hints?",
	######## Ending/Understanding ########
	'20': "I think I understand now.",
	'21': "I think this is correct.",
	'22': "Yay, we solved the problem!",
	'23': "Thank you! You're awesome. You made me feel smarter.",
	'24': "I'm getting tired now, but I think I understand the problem better. Maybe we can continue this another time.",
	######## What We Know #######
	'25': "I know that Luna runs one kilometer in 6 minutes and she runs at a constant speed.",
	'26': "I know that you need 2 liters of blue paint, and 3 liters of yellow paint, to make 5 liters of green paint."
}

# If the 
def speak(command_dialog):
	if command_dialog.isdigit() and (int(command_dialog) <= 26):
		tts.post.say(dialog[command_dialog])
	else:
		tts.say(command_dialog)
	
#Hello
def hello(command_dialog):
	gesture.waveRight2()
	tts.say(dialog[command_dialog])

def shrugAndShakeHead(command_dialog):
	gesture.shrug_and_shakehead()
	speak(command_dialog)

#nodding yes
def nod(command_dialog):
    gesture.nodYes()
    speak(command_dialog)

def fistYay(command_dialog):
	gesture.fistYay()
	speak(command_dialog)

#shaking no
def shakeHead(command_dialog):
	gesture.shakeNo()
	speak(command_dialog)

def handsHips(command_dialog):
	gesture.handsOnHips()
	speak(command_dialog)

def handOutLeft(command_dialog):
	gesture.handOutLeft()
	speak(command_dialog)

def handOutRight(command_dialog):
	gesture.handOutRight()
	speak(command_dialog)

def handChestLeft(command_dialog):
	gesture.handOnChestLeft()
	speak(command_dialog)

def bigShrug(command_dialog):
	gesture.largeShrug()
	speak(command_dialog)

def handLookAndOut(command_dialog):
	gesture.lookAtNailsRight()
	speak(command_dialog)
	gesture.handOutRight2()

def cheer(command_dialog):
	gesture.cheering()
	speak(command_dialog)

# Control what to do for built in commands or entered speech
def sendCmd(inp):
	if inp == '0':
		gesture.faceForward()
	elif inp == '1':
		hello(inp)
	elif inp in {'2', '3'} or inp[0:15].lower() == "we need to find":
		handsHips(inp)
	elif inp == '4':
		handChestLeft(inp)
	elif inp in {'5', '6', '7', '12', '13', '14', '20'}:
		nod(inp)
	elif inp in {'8', '9'}:
		bigShrug(inp)
	elif inp in {'10', '16', '20', '21'} or inp[0:9].lower() == "she ran for" or inp[0:5].lower() == "so do":
		handOutLeft(inp)
	elif inp in {'11', '15', '17', '25', '26'} or inp[0:7].lower() == "she ran" or inp[0:10].lower() == "the answer":
		handOutRight(inp)
	elif inp == '18':
		handLookAndOut(inp)
	elif inp == '19':
		shrugAndShakeHead(inp)
	elif inp == '23':
		fistYay(inp)
	elif inp == '22':
		cheer(inp)
	elif inp == '24':
		shakeHead(inp)
	elif inp == '27':
		gesture.turnHeadLeft()
	elif inp == '28':
		gesture.turnHeadRight()
	elif inp[0:7].lower() == "she ran":
		handOutLeft(inp)
	else:
		speak(inp)

'''TODO:
	incorporate adialog_new.py
'''
