# Pitch, Intensity, and Rate Manipulator
# Nichola Lubold 3/10/2015
 
# Description: Manipulates a sound file in a variety of ways depending on selected option. 
# Update: Reduced number of options; took out IPU options
#		Added in pitch_contour_raise 
#		Added in pitch_median
#		Modified copying_pitch_contour option to include sizing speaker's speech to duration of Quinn's speech 
# Utilizing praat plugin toolkit, http://www.praatvocaltoolkit.com/, Ramon Corretge, 2012 

# This part presents a form to the user
form Pitch Intensity Rate Manipulator
	comment type of analysis (rate is currently unavailable):
	optionmenu analysis_type: 1
	option intensity
	option pitch_flat
	option pitch_median
	option pitch_copycontour
	option pitch_copycontour_dur
	option pitch_contour_raise
	option rate
	comment gender:
	choice gender: 1
	button male
	button female
	comment feature file:
	text featurefile E:\Nikki\Research\Tag\PraatScripts\wavfiles\blob_3.wav
	comment transform file:
	text transfile E:\Nikki\Research\Tag\PraatScripts\wavfiles\response_2.wav
	comment output file:
	text output E:\Nikki\Research\Tag\PraatScripts\wavfiles\transformed.wav
endform

# If intensity...raises/lowers average intensity to that of the speaker
if analysis_type = 1

	#meanIntensity = Get mean... 0 duration energy
	#printline 'meanIntensity'

	# Read in feature file
	Read from file... 'featurefile$'
	s_feature$ = selected$ ("Sound")

	# Get mean intensity
	start = Get start time
	end = Get end time
	To Intensity... 100 0
	meanint = Get mean... start end dB

	# Read in trans file
	Read from file... 'transfile$'
	s_trans$ = selected$ ("Sound")

	# Transform intensity	
	To Intensity... 100 0
	Formula... self+(meanint-self)
	Down to IntensityTier
	select IntensityTier 's_trans$'
	plus Sound 's_trans$'
	Multiply

	select Sound 'sound_two$'
	Write to WAV file... 'output$'

	# Save to WAV file
	Save as WAV file... 'output$'

	# create a copy with date and time
	date$ = date$()
	date$ = replace$(date$, ":", "-",0)
	where = index(output$,".wav")
	where = where - 1
	head$ = left$(output$, where) + "_intensity_" + date$ + ".wav"
	Write to WAV file... 'head$'
	
	# Remove extraneous intensity sounds
	select Sound 's_feature$'
	plus Sound 'sound_two$'
	plus IntensityTier 's_trans$'
	plus Intensity 's_trans$'
	Remove

# else if pitch_flat - maps Quinn to a flat pitch based on the mean pitch of the speaker
elsif analysis_type = 2
	if gender = 1
		floor = 75
		ceiling = 300
	else
		floor = 100
		ceiling = 500
	endif

	printline "Flat pitch"

	# Read in feature file & get mean pitch
	Read from file... 'featurefile$'

	printline "here?"
	s_feature$ = selected$ ("Sound")
	To Pitch... 0 floor ceiling
	mean = Get mean... 0 0 Hertz

	printline "Got mean of feature file"
	
	# Read in transform file
	Read from file... 'transfile$'
	s_trans$ = selected$ ("Sound")
	select Sound 's_trans$'
	start = Get start time
	end = Get end time
	
	To Manipulation... 0.01 floor ceiling
	Create PitchTier... 's_trans$' start end
	Add point... start mean
	Add point... end mean

	printline "Manipulation of transformed file"

	# Combine and save the changed file
	select Manipulation 's_trans$'
	plus PitchTier 's_trans$'
	Replace pitch tier
	select Manipulation 's_trans$'
	# Get resynthesis (PSOLA)
	Get resynthesis (overlap-add)
	Write to WAV file... 'output$'
	
	printline "Writing output of transformed file"

	# create a copy with date and time
	date$ = date$()
	date$ = replace$(date$, ":", "-",0)
	where = index(output$,".wav")
	where = where - 1
	head$ = left$(output$, where) + "_flat_" + date$ + ".wav"
	Write to WAV file... 'head$'

	printline "Writing output of copy transformed file"

	select Sound 's_trans$'
	plus Manipulation 's_trans$'
	plus Sound 's_feature$'
	plus Pitch 's_feature$'
	plus PitchTier 's_trans$'
	Remove

# else if pitch_median - puts the median of Quinn's speech at the median of the speaker's
elsif analysis_type = 3

	Read from file... 'featurefile$'
	s_featuretmp = selected("Sound")
	s_feature$ = selected$("Sound")

	Read from file... 'transfile$'
	s_transtmp = selected("Sound")
	s_trans$ = selected$("Sound")

	select s_featuretmp
	execute workpre.praat
	s_feature = selected("Sound")

	select s_transtmp
	execute workpre.praat
	s_trans = selected("Sound")

	select s_feature
include minmaxf0.praat
	minF0_1 = minF0
	maxF0_1 = maxF0
	To Pitch... 0 minF0_1 maxF0_1
	f0_1 = Get quantile... 0 0 0.50 Hertz
	Remove

	select s_trans
include minmaxf0.praat
	minF0_2 = minF0
	maxF0_2 = maxF0
	To Pitch... 0 minF0_2 maxF0_2
	f0_2 = Get quantile... 0 0 0.50 Hertz
	Remove
	
	printline 'minF0_1'
	printline 'minF0_2'
	printline 'maxF0_1'
	printline 'maxF0_2'	
	printline 'f0_1'
	printline 'f0_2'

	f0_f = f0_1/f0_2
	
	select s_trans
	dur = Get total duration
	pitch = To Pitch... 0.01 minF0 maxF0
	plus s_trans
	manipulation = To Manipulation
	pitchtier = Extract pitch tier
	durationtier = Create DurationTier... 's_trans$' 0 dur
	Add point... 0 1
	plus manipulation
	Replace duration tier
	select pitchtier
	Formula... self*f0_f
	plus manipulation
	Replace pitch tier
	select manipulation
	resynthesis = Get resynthesis (overlap-add)
	execute workpost.praat
	
	result = Rename... 's_trans$'_copypitchmedian_'s_feature$'
	select result
	Write to WAV file... 'output$'

	# create a copy with date and time
	date$ = date$()
	date$ = replace$(date$, ":", "-",0)
	where = index(output$,".wav")
	where = where - 1
	head$ = left$(output$, where) + "_median_" + date$ + ".wav"
	Write to WAV file... 'head$'
	
	select s_feature
	plus s_trans
	plus Sound 's_feature$'
	plus Sound 's_trans$'
	plus pitch
	plus manipulation
	plus pitchtier
	plus durationtier
	plus resynthesis
	plus result
	Remove

	
# else if pitch_copycontour - maps the whole turn
elsif analysis_type = 4

	Read from file... 'featurefile$'
	s_featuretmp = selected("Sound")
	s_feature$ = selected$("Sound")

	Read from file... 'transfile$'
	s_transtmp = selected("Sound")
	s_trans$ = selected$("Sound")

	select s_featuretmp
	execute workpre.praat
	s_feature = selected("Sound")

	select s_transtmp
	execute workpre.praat
	s_trans = selected("Sound")

	select s_feature
include minmaxf0.praat
	minF0_1 = minF0
	maxF0_1 = maxF0
	pitch_1 = To Pitch... 0.01 minF0_1 maxF0_1
	pitchtier_1 = Down to PitchTier

	select s_trans
	dur = Get total duration
include minmaxf0.praat
	minF0_2 = minF0
	maxF0_2 = maxF0
	manipulation = To Manipulation... 0.01 minF0_2 maxF0_2
	plus pitchtier_1
	Replace pitch tier
	durationtier = Create DurationTier... 's_trans$' 0 dur
	Add point... 0 1
	plus manipulation
	Replace duration tier
	select manipulation
	resynthesis = Get resynthesis (overlap-add)
	execute workpost.praat
	result = Rename... 's_trans$'_copypitchcontour_'s_feature$'

	select result
	Write to WAV file... 'output$'
	
	# create a copy with date and time
	date$ = date$()
	date$ = replace$(date$, ":", "-",0)
	where = index(output$,".wav")
	where = where - 1
	head$ = left$(output$, where) + "_contour_" + date$ + ".wav"
	Write to WAV file... 'head$'

	select s_feature
	plus s_trans
	plus Sound 's_feature$'
	plus Sound 's_trans$'
	plus pitch_1
	plus pitchtier_1
	plus manipulation
	plus durationtier
	plus resynthesis
	plus result
	Remove
	

# else if pitch_copycontour_dur - resizes speaker's speech first
elsif analysis_type = 5
	if gender = 1
		floor = 75
		ceiling = 300
	else
		floor = 75
		ceiling = 500
	endif

	Read from file... 'transfile$'
	s_transtmp = selected("Sound")
	s_trans$ = selected$("Sound")

	select s_transtmp
	execute workpre.praat
	s_trans = selected("Sound")

	select s_trans
	new_duration = Get total duration
	#printline 'new_duration'

	Read from file... 'featurefile$'
	s_featuretmp = selected("Sound")
	s_feature$ = selected$("Sound")

	s_feature$ = selected$("Sound")
	wrk = Copy... wrk
	execute fixdc.praat
	dur = Get total duration
	#printline 'dur'	
include minmaxf0.praat
	result = Lengthen (overlap-add)... 'minF0' 'maxF0' 'new_duration'/'dur'
	Rename... 's_feature$'_changeduration_'method$'_'new_duration:2'
	execute fixdc.praat
	select wrk
	Remove
	select result
	Write to WAV file... 'output$'

	Read from file... 'output$'
	newsoundtmp = selected("Sound")
	newsound$ = selected$("Sound")
	
	select newsoundtmp
	execute workpre.praat
	newsound = selected("Sound")
	
	select newsound
include minmaxf0.praat
	minF0_1 = minF0
	maxF0_1 = maxF0
	pitch_1 = To Pitch... 0.01 minF0_1 maxF0_1
	pitchtier_1 = Down to PitchTier
	
	#printline 'minF0_1'
	#printline 'maxF0_1'

	select s_trans
	dur = Get total duration
	#printline 'dur'
include minmaxf0.praat
	minF0_2 = minF0
	maxF0_2 = maxF0
	manipulation = To Manipulation... 0.01 minF0_2 maxF0_2
	plus pitchtier_1
	Replace pitch tier
	durationtier = Create DurationTier... 's_trans$' 0 dur
	Add point... 0 1
	plus manipulation
	Replace duration tier
	select manipulation
	resynthesis = Get resynthesis (overlap-add)
	execute workpost.praat
	result2 = Rename... 's_trans$'_copypitchcontour_'s_feature$'

	select result2
	Write to WAV file... 'output$'

	# create a copy with date and time
	date$ = date$()
	date$ = replace$(date$, ":", "-",0)
	where = index(output$,".wav")
	where = where - 1
	head$ = left$(output$, where) + "_contourDur_" + date$ + ".wav"
	Write to WAV file... 'head$'
	
	select s_trans
	plus s_featuretmp
	plus s_transtmp
	plus newsoundtmp
	plus pitch_1
	plus pitchtier_1
	plus manipulation
	plus resynthesis
	plus result
	plus result2
	plus newsound
	plus durationtier
	Remove


# else if pitch_contour_raise
elsif analysis_type = 6

	# Set floor and ceiling
	if gender = 1
		floor = 75
		ceiling = 300
	else
		floor = 100
		ceiling = 500	
	endif

	Read from file... 'featurefile$'
	s_trans$ = selected$("Sound")
	To Pitch... 0 floor ceiling
	avg1 = Get mean... 0 0 Hertz
	
	printline 'avg1'
	
	Read from file... 'transfile$'
	s_feature$ = selected$("Sound",1)
	select Sound 's_feature$'
	To Pitch... 0 floor ceiling
	avg2 = Get mean... 0 0 Hertz
	max2 = Get maximum... 0 0 Hertz Parabolic
	min2 = Get minimum... 0 0 Hertz	Parabolic

	printline 'avg2'
	printline 'max2'
	printline 'min2'

	diff = avg1 - avg2
	printline 'diff'

	if gender = 1
		if diff < 0
			mindiff = min2 + diff
			if mindiff < 50
				diff = min2 - 50
			endif
			printline 'mindiff'
		else
			maxdiff = max2 + diff
			if maxdiff > 350
				diff = 350 - max2
			endif
			printline 'maxdiff'
		endif
	else
		if diff < 0
			mindiff = min2 + diff
			if mindiff < 75
				diff = min2 - 75
			endif
			printline 'mindiff'
		else
			maxdiff = max2 + diff
			if maxdiff > 525
				diff = 525 - max2
			endif
			printline 'maxdiff'
		endif
	endif

	select Sound 's_feature$'
	manipulation = To Manipulation... 0.01 floor ceiling
	pitch = Extract pitch tier
	Shift frequencies... 0 1000 diff Hertz
	plus manipulation
	Replace pitch tier
	select manipulation
	resynthesis = Get resynthesis (overlap-add)
	result = Rename... 'transfile$'_shiftedFrequencies
	select result
	Write to WAV file... 'output$'

	# create a copy with date and time
	date$ = date$()
	date$ = replace$(date$, ":", "-",0)
	where = index(output$,".wav")
	where = where - 1
	head$ = left$(output$, where) + "_mean_" + date$ + ".wav"
	Write to WAV file... 'head$'

	select Sound 's_feature$'
	plus Sound 's_trans$'
	plus manipulation
	plus pitch
	plus result
	plus Pitch 's_feature$'
	plus Pitch 's_trans$'
	Remove

# else rate - NOT COMPLETE
else
	Read from file... 'featurefile$'
	soundname$ = selected$ ("Sound")
	filedur = Get total duration
	printline 'filedur'
endif



printline "Script Finished"