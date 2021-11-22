import requests
import string
from pipe import *

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
	file = open("whitelist.txt")
	return True
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
	res = ''.join(e for e in input if(e in string.printable))
	res = ''.join(e for e in input if(e.isalpha()))
	res = res[0:12]
	return res

def cleanInt(input):
	res = ''.join(e for e in input if(e in string.printable))
	res = ''.join(e for e in input if(e.isnumeric()))
	res = res[0:6]
	res = (res)
	return res

def cleanDouble(input):
	res = ''.join(e for e in input if(e in string.printable))
	if(input == False):
		return False
	res = ''.join(e for e in input if(e.isnumeric() or (e == ".")))
	res = res[0:6]

	if(res[0] == "."):
		return False

	if(checkPeriods(input)):
		res = float(res)
		return res
	else:
		return False

def cleanTime(input):
	res = ''.join(e for e in input if(e in string.printable))
	input = cleanDouble(input)

	if(input > 16):
		return False
	else:
		return str(input)

def cleanTrack(input):
	input = cleanInt(input)
	input = int(input)
	if((input > 4) or (input < 0)):
		return False

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
		t = ''.join(f for f in e if(f.isalnum()))
		resultArray.append(t[0:25])
	result = ''
	for e in resultArray:
		result = result + e
	do_command("SelectTracks:Track=5")
	do_command("SelectTime:Start=0 end=16")
	
	if(len(result) == 0):
		return

	else:
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










