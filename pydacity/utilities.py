import requests
import string

from random import randrange
from pipe import *


class Note:
    name = ''
    frequency = 1.00

    def __init__(self, Freq, Name):
        self.name = Name
        self.frequency = Freq

f = open("Frequencies.txt", "r")
NoteList = []
for x in f:
    res = x.split("=")
    newNote = Note(res[1].strip("\n"), res[0].strip("\n"))
    NoteList.append(newNote)

for el in NoteList:
    print(el.name + ", " + el.frequency)

print("Loaded note frequencies successfully")

def cleanEncoding(input):
	
	result = input.encode("ascii",errors='ignore').decode()
	return result


def validateList(list):
	result = True
	for e in list:
		if e == False:
			result = False
	return result

def getUsername(input):
	result = ""
	displayname = "display-name"
	for e in input:
		if(displayname in e.get("key")):
			result = e.get("value")
			return result

	return("null")

def validateUsername(username):
	return True
	file = open("whitelist.txt")
	output = file.read()
	if(" " + username + ", " in output):
		return True
	else:
		return False

def validateTime(start, end):
	start = cleanDouble(start)
	end = cleanDouble(end)
	if(start > end):
		return False
	if((end - start) > 1):
		return False

	else:
		return True
	
def cleanString(input):
	res = ''.join(e for e in input if(e.isalpha()))
	res = res[0:12]
	res = res.capitalize()
	return res

def cleanFrequency(input):
	for e in NoteList:
		if(input == e.name):
			return str(e.frequency)
	return cleanInt(input)

def cleanInt(input):
	res = ''.join(e for e in input if(e.isnumeric()))
	res = res[0:6]
	if not(str(res)):
		res = res + "1"
	if(int(res) == 0):
		res = "1"
	return res

def cleanDouble(input):
	if(input == False):
		return False
	res = ''.join(e for e in input if(e.isnumeric() or (e == ".")))
	res = res[0:6]

	if not res:
		return False

	if(res[0] == "."):
		return False

	if(checkPeriods(input)):
		res = float(res)
		return res
	else:
		return False

def cleanTime(input):
	input = cleanDouble(input)

	if(input > 16):
		return False
	else:
		return str(input)

def cleanTrack(input):
	res = ''.join(e for e in input if(e.isnumeric()))
	if(res.isnumeric() == False):
		return str(randrange(5))

	res = res[0:6]

	input = int(input)
	if((input > 4) or (input < 0)):
		return str(randrange(5))

	return str(input)

def checkPeriods(input):
	counter = 0;
	for e in input:
		if(e == "."):
			counter = counter + 1

	if(counter > 1):
		return False
	else:
		return True

def DTMF(input):
	resultArray = []
	for e in input:
		e = e.strip()

	for e in input:
		t = ''.join(f for f in e if(f.isalnum()))
		resultArray.append(t[0:25])
	result = ''
	for e in resultArray:
		result = result + e
	do_command("SelectTracks:Track=5")
	do_command("SelectTime:Start=0 end=16")
	
	if not result:
		return

	if(len(result) == 0):
		return

	else:
		print(result[0:500])
		do_command("DtmfTones:Sequence=" + result[0:500] + " 55 0.8")

def autoplay():
    do_command("Play")

def autoloop():
    do_command("PlayLooped")

def newTrack():
    do_command("NewStereoTrack")

def fitInWindow():
    do_command("FitInWindow")
    do_command("FitV")










