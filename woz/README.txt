These are the files from Spring '17 for running the Wizard of Oz experiments.

1. Turn on Nico and wait for it to start.
2. Open terminal. Type: 
	cd ~Desktop/nico/PythonScriptSummer15
	python thread.py
3. This will open two terminal windows. One for recording the dialogue exchange and the other for controlling Nico’s responses.
4.You can type in numbers from 1-21 in the terminal window as your input choice.These numbers correspond to sentences in dialog dictionary (in thread.py).
5. We implemented interactions and gestures for 21 different nico dialogs.
6. You can also type in a phrase (which doesn't exist in dialog dictionary) in the terminal window and Nico will say it. Eg - ‘5 litres of green paint.’
7. The dialogue interaction should be saved in test1.csv in the same directory. This file will be overwritten every time the thread.py script is run.

---Notes---
Nico will sometimes say or do unexpected things(eg - Tai Chi) in the middle of an experiment. We weren’t able to turn off Nico’s automatic mode during the experiment because it would prevent Nico from recording the conversation. Turning off automatic mode would also mean Nico will not go back to its original pose after doing a gesture (eg- after waving hello Nico’s arm will remain up instead of coming back down). This could be a future improvement in the Wizard of Oz experiment.
