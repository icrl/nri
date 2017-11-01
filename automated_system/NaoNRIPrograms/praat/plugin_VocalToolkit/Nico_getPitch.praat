# Pitch Extractor
# Nichola Lubold 3/10/2015
 
# Description: Extracts Mean Pitch from given audio 

# This part presents a form to the user
form Pitch Extractor
	comment feature file:
	text featurefile C:\Nikki\ASU_Research\NRI_Project\System\NRI_Git_Hub\automated_system\NaoNRIPrograms\praat\plugin_VocalToolkit\userMean.txt
endform



# Set floor and ceiling
#if gender = 1
#	floor = 75
#	ceiling = 300
#else
#	floor = 100
#	ceiling = 500	
#endif

floor = 75
ceiling = 400

Read from file... 'featurefile$'
s2$ = selected$("Sound")
To Pitch... 0 floor ceiling
avg1 = Get mean... 0 0 Hertz

# appendFile: meanFile$, avg1, ", "
	
printline 'avg1'

select Sound 's2$'
plus Pitch 's2$'
Remove

# else rate
#else
#	Read from file... 'featurefile$'
#	soundname$ = selected$ ("Sound")
#	filedur = Get total duration
#	printline 'filedur'
#endif



printline "Script Finished"