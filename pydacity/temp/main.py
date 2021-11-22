import os
import sys
import time
import json
from pipe import *
from utilities import *

def parseCommand(rawInput):
	inList = rawInput.split(" ")
	input = inList[0]
	del(inList[0])
	arguments = inList
	arglen = len(arguments)
	
	if input == "Tone":
		if(arglen == 5):
			waveform = cleanString(arguments[0])
			pitch = cleanInt(arguments[1])
			start = cleanTime(arguments[2])
			end = cleanTime(arguments[3])
			track = cleanTrack(arguments[4])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + str(track))
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("tone:Frequency=" + str(pitch) + " waveform=" + str(waveform))

	elif input == "Chirp":
		if(arglen == 5):
			startfreq = cleanInt(arguments[0])
			endfreq = cleanInt(arguments[1])
			start = cleanTime(arguments[2])
			end = cleanTime(arguments[3])
			track = cleanTrack(arguments[4])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("Chirp:StartFreq=" + startfreq + " EndFreq=" + endfreq)

	elif input == "LowFilter":
		if(arglen == 4):	
			frequency = cleanInt(arguments[0])
			start = cleanTime(arguments[1])
			end = cleanTime(arguments[2])
			track = cleanTrack(arguments[3])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("Low-passFilter:frequency=" + frequency)

	elif input == "Compressor":
		if(arglen == 3):
			start = cleanTime(arguments[0])
			end = cleanTime(arguments[1])
			track = cleanTrack(arguments[2])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("Compressor:")

	elif input == "Echo":
		if(arglen == 3):
			start = cleanTime(arguments[0])
			end = cleanTime(arguments[1])
			track = cleanTrack(arguments[2])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("Echo:")
	
	elif input == "Phaser":
		if(arglen == 3):
			start = cleanTime(arguments[0])
			end = cleanTime(arguments[1])
			track = cleanTrack(arguments[2])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("Phaser:")
	
	elif input == "Reverb":
		if(arglen == 3):
			start = cleanTime(arguments[0])
			end = cleanTime(arguments[1])
			track = cleanTrack(arguments[2])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("Reverb:")
	
	elif input == "Wahwah":
		if(arglen == 3):
			start = cleanTime(arguments[0])
			end = cleanTime(arguments[1])
			track = cleanTrack(arguments[2])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("Wahwah:")			

	elif input == "Fadein":
		if(arglen == 3):
			start = cleanTime(arguments[0])
			end = cleanTime(arguments[1])
			track = cleanTrack(arguments[2])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("fadein:")		
	
	elif input == "Fadeout":
		if(arglen == 3):
			start = cleanTime(arguments[0])
			end = cleanTime(arguments[1])
			track = cleanTrack(arguments[2])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("fadeout:")	

	elif input == "Reverse":
		if(arglen == 3):
			start = cleanTime(arguments[0])
			end = cleanTime(arguments[1])
			track = cleanTrack(arguments[2])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("Reverse:")			

	elif input == "Delete":
		if((arglen==3) and False):
			start = cleanTime(arguments[0])
			end = cleanTime(arguments[1])
			track = cleanTrack(arguments[2])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("DeleteKey2")

	elif input == "Fart":
		if((arglen==2) and False):
			start = cleanTime(arguments[0])
			end = str(float(start) + 0.01)
			track = cleanTrack(arguments[1])
			if(validateTime(start, end)):
				do_command("SelectTracks:Track=0")
				do_command("SelectTime:Start=17.5 end=17.9")
				do_command("Copy")
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start=" + start + " End=" + end)
				do_command("Paste")

	

