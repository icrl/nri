# wizard GUI
import nicoController as control
import time

from Tkinter import *

#create the window
root = Tk()

#modify root window
root.title("Wizard GUI")
#sets the width/height of window
root.geometry("655x600")

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
		if key != "22" and key != "23" and key != "0":
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
	
	#------------- Button Entry Options-------------

	buttons = Frame(root, width = 655, height = 365, pady = 3)
	buttons.grid(row =0, sticky = "nsew")

	# Introduction
	intro = Label(buttons, text = "Introduction")
	b1 = Button(buttons, text = 'Hello!', command = lambda: call(1), width = 17, bg = "lavender")
	b2 = Button(buttons, text = 'I\'m ready to learn!', command = lambda: call(2), width = 17, bg = "lavender")
	b3 = Button(buttons, text = 'What are we solving?', command = lambda: call(3), width = 17, bg = "lavender")
	b4 = Button(buttons, text = 'I want to solve this.', command = lambda: call(4), width = 17, bg = "lavender")
	
	intro.grid(row = 0, columnspan = 4)
	b1.grid(row = 1)
	b2.grid(row = 1, column = 1)
	b3.grid(row = 1, column = 2)
	b4.grid(row = 1, column = 3)

	# Confirmation
	confirm = Label(buttons, text = "Confirmation")
	b5 = Button(buttons, text = 'Okay!', command = lambda: call(5), width = 17, bg = "misty rose")
	b6 = Button(buttons, text = 'Yes.', command = lambda: call(6), width = 17, bg = "misty rose")
	b7 = Button(buttons, text = 'Yes, I agree.', command = lambda: call(7), width = 17, bg = "misty rose")

	confirm.grid(row = 2, columnspan = 4)
	b5.grid(row = 3)
	b6.grid(row = 3, column = 1)
	b7.grid(row = 3, column = 2)

	# Asking Questions
	question = Label(buttons, text = "Asking Questions")
	b8 = Button(buttons, text = 'How do we solve this?', command = lambda: call(8), width = 17, bg = "mint cream")
	b9 = Button(buttons, text = 'What\'s next?', command = lambda: call(9), width = 17, bg = "mint cream")
	b10 = Button(buttons, text = 'How do we do that?', command = lambda: call(10), width = 17, bg = "mint cream")
	b11 = Button(buttons, text = 'More information?', command = lambda: call(11), width = 17, bg = "mint cream")
	b12 = Button(buttons, text = 'Now we multiply?', command = lambda: call(12), width = 17, bg = "mint cream")
	b13 = Button(buttons, text = 'Now we add?', command = lambda: call(13), width = 17, bg = "mint cream")
	b14 = Button(buttons, text = 'Now we divide?', command = lambda: call(14), width = 17, bg = "mint cream")
	b15 = Button(buttons, text = 'Is this correct?', command = lambda: call(15), width = 17, bg = "mint cream")

	question.grid(row = 4, columnspan = 4)
	b8.grid(row = 5)
	b9.grid(row = 5, column = 1)
	b10.grid(row = 5, column = 2)
	b11.grid(row = 5, column = 3)
	b12.grid(row = 6)
	b13.grid(row = 6, column = 1)
	b14.grid(row = 6, column = 2)
	b15.grid(row = 6, column = 3)

	# Confusion
	confuse = Label(buttons, text = "Confusion")
	b16 = Button(buttons, text = 'How\'d we get that?', command = lambda: call(16), width = 17, bg = "light yellow")
	b17 = Button(buttons, text = 'Break that down?', command = lambda: call(17), width = 17, bg = "light yellow")
	b18 = Button(buttons, text = 'Seems complicated.', command = lambda: call(18), width = 17, bg = "light yellow")
	b19 = Button(buttons, text = 'Don\'t know. Hints?', command = lambda: call(19), width = 17, bg = "light yellow")

	confuse.grid(row = 7, columnspan = 4)
	b16.grid(row = 8)
	b17.grid(row = 8, column = 1)
	b18.grid(row = 8, column = 2)
	b19.grid(row = 8, column = 3)

	# Ending/Understanding
	ending = Label(buttons, text = "End/Understand")
	b20 = Button(buttons, text = 'I understand now.', command = lambda: call(20), width = 17, bg = "light cyan")
	b21 = Button(buttons, text = 'Think it\'s correct.', command = lambda: call(21), width = 17, bg = "light cyan")
	b22 = Button(buttons, text = 'Solved the problem!', command = lambda: call(22), width = 17, bg = "light cyan")
	b23 = Button(buttons, text = 'Thank you!', command = lambda: call(23), width = 17, bg = "light cyan")
	b24 = Button(buttons, text = 'Getting tired. Later?', command = lambda: call(24), width = 17, bg = "light cyan")

	ending.grid(row = 9, columnspan = 4)
	b20.grid(row = 10)
	b21.grid(row = 10, column = 1)
	b22.grid(row = 10, column = 2)
	b23.grid(row = 10, column = 3)
	b24.grid(row = 11)

	# What We Know
	know = Label(buttons, text = "What We Know")
	b25 = Button(buttons, text = 'I know running.', command = lambda: call(25), width = 17, bg = "wheat")
	b26 = Button(buttons, text = 'I know painting.', command = lambda: call(26), width = 17, bg = "wheat")

	know.grid(row = 11, column = 1)
	b25.grid(row = 11, column = 2)
	b26.grid(row = 11, column = 3)

	# Make Nico turn his head 
	turns = Label(buttons, text = "Turn Head")
	forward = Button(buttons, text = "Face forward", command = lambda: call(0), width = 17, bg = "peach puff")
	left = Button(buttons, text = "Turn Head Left", command = lambda: call(27), width = 17, bg = "peach puff")
	right = Button(buttons, text = "Turn Head Right", command = lambda: call(28), width = 17, bg = "peach puff")

	turns.grid(row = 12)
	forward.grid(row = 12, column = 1)
	left.grid(row = 12, column = 2)
	right.grid(row = 12, column = 3)

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
	enter = Button(textop, text = "Enter", command = onclick, width = 17)
	eLabel.grid(row = 1)
	entry.grid(row = 1, column = 1, columnspan = 2)
	enter.grid(row = 1, column = 3)


	#She ran x km
	ranKmL = Label(textop, text= "She ran __ km")
	ranKmE = Entry(textop, width = 4)

	def ranKm():
		kms = ranKmE.get()
		call("She ran %s kilometers."%kms)
		ranKmE.delete(0,END)

	ranKmSay = Button(textop, text = "Say", command = ranKm)
	ranKmL.grid(row = 2)
	ranKmE.grid(row = 2, column = 1, columnspan = 2)
	ranKmSay.grid(row = 2, column = 3)

	#She ran x min
	ranMinL = Label(textop, text = "She ran __ min")
	ranMinE = Entry(textop, width = 4)

	def ranMin():
		mins = ranMinE.get()
		call("She ran for %s minutes."%mins)
		ranMinE.delete(0, END)

	ranMinSay = Button(textop, text = "Say", command = ranMin)
	ranMinL.grid(row = 3)
	ranMinE.grid(row = 3, column = 1, columnspan = 2)
	ranMinSay.grid(row = 3, column = 3)

	# Provide an answer
	answerL = Label(textop, text= "The answer is __")
	answerE = Entry(textop, width = 4)

	def getAns():
		ans = answerE.get()
		call("The answer is %s."%ans)
		answerE.delete(0,END)

	answerSay = Button(textop, text = "Say", command = getAns)
	answerL.grid(row = 4)
	answerE.grid(row = 4, column = 1, columnspan = 2)
	answerSay.grid(row = 4, column = 3)

	# Need to do next
	# Need to find time to run x km
	findKmL = Label(textop, text = "Find time to run __ km")
	findKmE = Entry(textop, width = 4)

	def findKm():
		kms = findKmE.get()
		call("We need to find out how long it takes for Luna to run %s kilometers."%kms)
		findKmE.delete(0,END)

	findKmSay = Button(textop, text = "Say", command = findKm)
	findKmL.grid(row = 5)
	findKmE.grid(row = 5, column = 1, columnspan = 2)
	findKmSay.grid(row = 5, column = 3)

	# Need to find km ran in x min
	findMinL = Label(textop, text = "Find km run in __ min")
	findMinE = Entry(textop, width = 4)

	def findMin():
		mins = findMinE.get()
		call("We need to find out how many kilometers she ran in %s minutes!"%mins)
		findMinE.delete(0,END)

	findMinSay = Button(textop, text = "Say", command = findMin)
	findMinL.grid(row = 6)
	findMinE.grid(row = 6, column = 1, columnspan = 2)
	findMinSay.grid(row = 6, column = 3)

	# In x mins be y km away
	runAnsL = Label(textop, text = "In __ mins be __ km away")
	runAnsE1 = Entry(textop, width = 4)
	runAnsE2 = Entry(textop, width = 4)

	def runAns():
		mins = runAnsE1.get()
		kms = runAnsE2.get()
		call("So in %s minutes she would be %s kilometers away"%(mins, kms))
		runAnsE1.delete(0,END)
		runAnsE2.delete(0,END)

	runAnsSay = Button(textop, text = "Say", command = runAns)
	runAnsL.grid(row = 7)
	runAnsE1.grid(row = 7, column = 1)
	runAnsE2.grid(row = 7, column = 2)
	runAnsSay.grid(row = 7, column = 3)

	#------------- End the program immediately. -------------
	bEnd = Button(root, text = "End program", command = exit, width = 17, bg = 'red')
	bEnd.grid(row = 3)


#------------- MAIN -------------
if __name__ ==  "__main__":
	main()
	#kick off the event loop
	root.mainloop()
	"""
	filepath = "/home/nao/programs/move.top"
	#ad.main()
	args = shlex.split('python adialog_new.py')
	#subprocess.Popen(["python", "adialog_new.py"])
	p = subprocess.call(['gnome-terminal', '-x', 'bash', '-c','python adialog.py'])
	#Thread(target = func2).start()
	subprocess.kill()
	"""
