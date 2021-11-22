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
	
	if input == "Sine":
		if(arglen == 4):
			pitch = cleanFrequency(arguments[0])
			start = cleanTime(arguments[1])
			end = cleanTime(arguments[2])
			track = cleanTrack(arguments[3])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + str(track))
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("Tone:Frequency=" + str(pitch) + " Waveform=Sine")

	if input == "Sawtooth":
		if(arglen == 4):
			pitch = cleanFrequency(arguments[0])
			start = cleanTime(arguments[1])
			end = cleanTime(arguments[2])
			track = cleanTrack(arguments[3])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + str(track))
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("Tone:Frequency=" + str(pitch) + " Waveform=Sawtooth")
					
	if input == "Square":
		if(arglen == 4):
			pitch = cleanFrequency(arguments[0])
			start = cleanTime(arguments[1])
			end = cleanTime(arguments[2])
			track = cleanTrack(arguments[3])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + str(track))
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("Tone:Frequency=" + str(pitch) + " Waveform=Square")		

	elif input == "Chirp":
		if(arglen == 5):
			startfreq = cleanFrequency(arguments[0])
			endfreq = cleanFrequency(arguments[1])
			start = cleanTime(arguments[2])
			end = cleanTime(arguments[3])
			track = cleanTrack(arguments[4])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("Chirp:StartFreq=" + startfreq + " EndFreq=" + endfreq)

	elif input == "LowFilter":
		if(arglen == 4):	
			frequency = cleanFrequency(arguments[0])
			start = cleanTime(arguments[1])
			end = cleanTime(arguments[2])
			track = cleanTrack(arguments[3])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("Low-passFilter:Frequency=" + frequency)

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
				do_command("Fadein:")		
	
	elif input == "Fadeout":
		if(arglen == 3):
			start = cleanTime(arguments[0])
			end = cleanTime(arguments[1])
			track = cleanTrack(arguments[2])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("Fadeout:")	

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
		if((arglen==3)):
			start = cleanTime(arguments[0])
			end = cleanTime(arguments[1])
			track = cleanTrack(arguments[2])
			if(validateTime(start,end)):
				do_command("SelectTracks:Track=" + track)
				do_command("SelectTime:Start="+ start + " End=" + end)
				do_command("Silence")


