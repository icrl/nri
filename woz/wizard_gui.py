# wizard GUI
import nicoController as control
import time

from Tkinter import *

#create the window
root = Tk()

#modify root window
root.title("Wizard GUI")
#sets the width/height of window
root.geometry("500x580")

def main():
	#-------------Logging Setup-------------

	# Set up the current time to be able to create the file
	currtime = time.asctime( time.localtime(time.time()) )[4:16]
	currtime = currtime.replace(" ", "-")
	currtime = currtime.replace(":", "")
	
	# Create the filename using the date and time
	filename = "log{}.txt".format(currtime)

	# If the key has dialog associated with it, log it to the file
	def writeFile(key):
		if key not in {'0', '33', '34', '35'}:
			currtime = time.asctime( time.localtime(time.time()) )
			f = open(filename, "a")
			f.write(currtime + " ")
			if key.isdigit():
				f.write(control.dialog[key] + "\n")
			else:
				f.write(key + "\n")
			f.close()
	

	#-------------GUI Controls-------------

	# Call the movement/dialog option and then write any dialog to the file
	def call(code):
		cmd = str(code)
		control.sendCmd(cmd)
		writeFile(cmd)
	
	menubar = Menu(root)

	#-------------Menu Bar Controls-------------

	# Introduction
	intromenu = Menu(menubar, tearoff = 0)
	intromenu.add_command(label = 'Hello!', command = lambda: call(1))
	intromenu.add_command(label = 'I\'m ready to learn!', command = lambda: call(2))
	intromenu.add_command(label = 'What are we solving?', command = lambda: call(3))
	intromenu.add_command(label = 'I want to solve this.', command = lambda: call(4))
	menubar.add_cascade(label = "Introduction", menu = intromenu)

	# Confirmation
	confmenu = Menu(menubar)
	confmenu.add_command(label = 'Okay!', command = lambda: call(5))
	confmenu.add_command(label = 'Yes.', command = lambda: call(6))
	confmenu.add_command(label = 'Yes, I agree.', command = lambda: call(7))
	menubar.add_cascade(label = "Confirmation", menu = confmenu)

	# Asking Questions
	qmenu = Menu(menubar)
	qmenu.add_command(label = 'How do we solve this?', command = lambda: call(8))
	qmenu.add_command(label = 'What\'s next?', command = lambda: call(9))
	qmenu.add_command(label = 'How do we do that?', command = lambda: call(10))
	qmenu.add_command(label = 'More information?', command = lambda: call(11))
	qmenu.add_command(label = 'Is this correct?', command = lambda: call(15))
	qmenu.add_command(label = 'How do we start?', command = lambda: call(28))
	qmenu.add_separator()
	qmenu.add_command(label ='Now we add?', command = lambda: call(13))
	qmenu.add_command(label = 'Now we multiply?', command = lambda: call(12))
	qmenu.add_command(label = 'Now we divide?', command = lambda: call(14))
	menubar.add_cascade(label = "Questions", menu = qmenu)

	# Confusion
	confusemenu = Menu(menubar, tearoff = 0)
	confusemenu.add_command(label = 'How\'d we get that?', command = lambda: call(16))
	confusemenu.add_command(label = 'Break that down?', command = lambda: call(17))
	confusemenu.add_command(label = 'Seems complicated.', command = lambda: call(18))
	confusemenu.add_command(label = 'Don\'t know. Hints?', command = lambda: call(19))
	menubar.add_cascade(label = 'Confusion', menu = confusemenu)

	# Ending/Understanding
	endmenu = Menu(menubar, tearoff = 0)
	endmenu.add_command(label = 'I understand now.', command = lambda: call(20))
	endmenu.add_command(label = 'Think it\'s correct.', command = lambda: call(21))
	qmenu.add_separator()
	endmenu.add_command(label = 'Solved the problem!', command = lambda: call(22))
	endmenu.add_command(label = 'Thank you!', command = lambda: call(23))
	endmenu.add_command(label = 'Getting tired. Later?', command = lambda: call(24))
	menubar.add_cascade(label = "Ending", menu = endmenu)

	# What We Know
	knowmenu = Menu(menubar, tearoff = 0)
	knowmenu.add_command(label = 'I know painting.', command = lambda: call(25))
	knowmenu.add_command(label = 'I know driving.', command = lambda: call(26))
	knowmenu.add_command(label = 'I know swimming.', command = lambda: call(27))

	menubar.add_cascade(label = "I know...", menu = knowmenu)

	# Survey Questions
	surveymenu = Menu(menubar)
	surveymenu.add_command(label = 'Do you like math?', command = lambda: call(30))
	surveymenu.add_command(label = 'Done problems like these before?', command = lambda: call(31))
	surveymenu.add_command(label = 'Hard when you started?', command = lambda: call(32))

	menubar.add_cascade(label = 'Survey', menu = surveymenu)

	root.config(menu=menubar)

	#------------- Button Control Options-------------

	buttons = Frame(root, width = 655, height = 365, pady = 3)
	buttons.grid(row =0, sticky = "nsew")

	# Make Nico turn his head 
	turns = Label(buttons, text = "Move Head")
	forward = Button(buttons, text = "Face forward", command = lambda: call(0), width = 17)
	left = Button(buttons, text = "Turn Head Left", command = lambda: call(33), width = 17)
	right = Button(buttons, text = "Turn Head Right", command = lambda: call(34), width = 17)
	nod = Button(buttons, text = "Nod Head Yes", command = lambda: call(35), width = 17)
	next = Button(buttons, text = "Click Next", command = lambda: call(29), width = 17, bg = "lavender")

	turns.grid(row = 0, columnspan = 2)
	forward.grid(row = 1)
	left.grid(row = 1, column = 1)
	next.grid(row = 1, column = 2)
	right.grid(row = 2)
	nod.grid(row = 2, column = 1)

	#------------- Text entry options -------------
	textop = Frame(root, width = 655, height = 100, pady = 3)
	textop.grid(row = 2, sticky = "nsew")

	textLabel = Label(textop, text = "Text entry options")
	textLabel.grid(row = 0, columnspan = 4)

	# Enter anything for Nico to say
	eLabel =  Label(textop,text = "Enter text:")
	entry = Entry(textop)

	def onclick(event = None):
		eText = entry.get()
		call(eText)
		entry.delete(0,END)

	root.bind('<Return>', onclick)
	enter = Button(textop, text = "Enter", command = onclick)
	eLabel.grid(row = 1)
	entry.grid(row = 1, column = 1, columnspan = 2)
	enter.grid(row = 1, column = 3)

	# Provide an answer
	answerL = Label(textop, text= "The answer is __")
	answerE = Entry(textop, width = 4)

	def getAns():
		ans = answerE.get()
		call("The answer is %s."%ans)
		answerE.delete(0,END)

	answerSay = Button(textop, text = "Say", command = getAns)
	answerL.grid(row = 2)
	answerE.grid(row = 2, column = 1, columnspan = 2)
	answerSay.grid(row = 2, column = 3)
	

	multL = Label(textop, text = "We multiply __ and __")
	multE1 = Entry(textop, width = 4)
	multE2 = Entry(textop, width = 4)
	def getMult():
		m1 = multE1.get()
		m2 = multE2.get()
		call("We multiply %s and %s?"%(m1, m2))
		multE1.delete(0,END)
		multE2.delete(0,END)
	multSay = Button(textop, text = "Say", command = getMult)

	multL.grid(row = 3)
	multE1.grid(row = 3, column = 1)
	multE2.grid(row = 3, column = 2)
	multSay.grid(row = 3, column = 3)

	addL = Label(textop, text = "We add __ and __")
	addE1 = Entry(textop, width = 4)
	addE2 = Entry(textop, width = 4)
	def getAdd():
		a1 = addE1.get()
		a2 = addE2.get()
		call("We add %s and %s?"%(a1, a2))
		addE1.delete(0,END)
		addE2.delete(0,END)
	addSay = Button(textop, text = "Say", command = getAdd)

	addL.grid(row = 4)
	addE1.grid(row = 4, column = 1)
	addE2.grid(row = 4, column = 2)
	addSay.grid(row = 4, column = 3)

	divL = Label(textop, text = "We divide __ by __ ")
	divE1 = Entry(textop, width = 4)
	divE2 = Entry(textop, width = 4)
	def getDiv():
		d1 = divE1.get()
		d2 = divE2.get()
		call("We divide %s by %s?"%(d1, d2))
		divE1.delete(0,END)
		divE2.delete(0,END)
	divSay = Button(textop, text = "Say", command = getDiv)

	divL.grid(row = 5)
	divE1.grid(row = 5, column = 1)
	divE2.grid(row = 5, column = 2)
	divSay.grid(row = 5, column = 3)

	meanL = Label(textop, text = "Do you mean __?")
	meanE = Entry(textop, width = 4)
	def getMean():
		m = meanE.get()
		call("Do you mean %s"%m)
		meanE.delete(0,END)
	meanSay = Button(textop, text = "Say", command = getMean)

	meanL.grid(row = 6)
	meanE.grid(row = 6, column = 1, columnspan = 2)
	meanSay.grid(row = 6, column = 3)

	# separator
	sep1 = Frame(textop, height=2, bd=1, relief=SUNKEN, width = 450)
	sep1.grid(row = 7, columnspan = 4)

	# Paint Problem

	paintL = Label(textop, text = "I need __ fl oz")
	paintE = Entry(textop, width = 4)
	def getPaint():
		p = paintE.get()
		call("I need %s fluid ounces of paint."%p)
		paintE.delete(0,END)
	paintSay =  Button(textop, text = "Say", command = getPaint)

	paintL.grid(row = 8)
	paintE.grid(row = 8, column = 1, columnspan = 2)
	paintSay.grid(row = 8, column = 3)

	inchL = Label(textop, text = "It'll cover __ sq in")
	inchE = Entry(textop, width = 4)
	def getInch():
		i = inchE.get()
		call("It will cover %s square inches."%i)
		inchE.delete(0,END)
	inchSay =  Button(textop, text = "Say", command = getInch)

	inchL.grid(row = 9)
	inchE.grid(row = 9, column = 1, columnspan = 2)
	inchSay.grid(row = 9, column = 3)

	coverL = Label(textop, text = "Need __ ounces to cover __ in")
	coverE1 = Entry(textop, width = 4)
	coverE2 = Entry(textop, width = 4)
	def getCover():
		c1 = coverE1.get()
		c2 = coverE2.get()
		call("I need %s fluid ounces of paint to  cover %s square inches."%(c1, c2))
		coverE1.delete(0,END)
		coverE2.delete(0,END)
	coverSay = Button(textop, text = "Say", command = getCover)

	coverL.grid(row = 10)
	coverE1.grid(row = 10, column = 1)
	coverE2.grid(row = 10, column = 2)
	coverSay.grid(row = 10, column = 3)

	# separator
	sep2 = Frame(textop, height=2, bd=1, relief=SUNKEN, width = 450)
	sep2.grid(row = 11, columnspan = 4)

	# Driving problem
	timeL = Label(textop, text = "Traveling for __ hrs")
	timeE = Entry(textop, width = 4)
	def getTime():
		t = timeE.get()
		call("I will be traveling for %s hours."%t)
		timeE.delete(0,END)
	timeSay =  Button(textop, text = "Say", command = getTime)

	timeL.grid(row = 12)
	timeE.grid(row = 12, column = 1, columnspan = 2)
	timeSay.grid(row = 12, column = 3)

	mileL = Label(textop, text = "Traveled __ mi")
	mileE = Entry(textop, width = 4)
	def getMile():
		p = mileE.get()
		call("I will travel %s miles."%p)
		mileE.delete(0,END)
	mileSay =  Button(textop, text = "Say", command = getMile)

	mileL.grid(row = 13)
	mileE.grid(row = 13, column = 1, columnspan = 2)
	mileSay.grid(row = 13, column = 3)

	travL = Label(textop, text = "Travel __ mi in __ hrs")
	travE1 = Entry(textop, width = 4)
	travE2 = Entry(textop, width = 4)
	def getTrav():
		c1 = travE1.get()
		c2 = travE2.get()
		call("I will travel %s miles in %s hours."%(c1, c2))
		travE1.delete(0,END)
		travE2.delete(0,END)
	travSay = Button(textop, text = "Say", command = getTrav)

	travL.grid(row = 14)
	travE1.grid(row = 14, column = 1)
	travE2.grid(row = 14, column = 2)
	travSay.grid(row = 14, column = 3)

	# separator
	sep3 = Frame(textop, height=2, bd=1, relief=SUNKEN, width = 450)
	sep3.grid(row = 15, columnspan = 4)

	# Swimming problem
	shoreL = Label(textop, text = "Be __ ft from shore")
	shoreE = Entry(textop, width = 4)
	def getShore():
		p = shoreE.get()
		call("I will be %s feet from the shore."%p)
		shoreE.delete(0,END)
	shoreSay =  Button(textop, text = "Say", command = getShore)

	shoreL.grid(row = 16)
	shoreE.grid(row = 16, column = 1, columnspan = 2)
	shoreSay.grid(row = 16, column = 3)

	swimL = Label(textop, text = "Swim __ ft")
	swimE = Entry(textop, width = 4)
	def getSwim():
		p = swimE.get()
		call("I will have swam %s feet."%p)
		swimE.delete(0,END)
	swimSay =  Button(textop, text = "Say", command = getSwim)

	swimL.grid(row = 17)
	swimE.grid(row = 17, column = 1, columnspan = 2)
	swimSay.grid(row = 17, column = 3)

	secL = Label(textop, text = "Swam __ secs")
	secE = Entry(textop, width = 4)
	def getSec():
		p = secE.get()
		call("I will have swam for %s seconds."%p)
		secE.delete(0,END)
	secSay =  Button(textop, text = "Say", command = getSec)

	secL.grid(row = 18)
	secE.grid(row = 18, column = 1, columnspan = 2)
	secSay.grid(row = 18, column = 3)

	#------------- End the program immediately. -------------
	bEnd = Button(root, text = "End program", command = exit, width = 17, bg = 'red')
	bEnd.grid(row = 3)



#------------- MAIN -------------
if __name__ ==  "__main__":
	main()
	#kick off the event loop
	root.mainloop()
