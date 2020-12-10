#!/usr/bin/python
# v01.01.0000


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# import globally
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

from datetime import datetime as DT
from os import path as PATH
import pickle as PD
import PySimpleGUI as SG


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# setting constants
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

MAINDOWNCOLOR = "#880000"
MAINDOWNTEXTCOLOR = "#FF0000"
MAINUPCOLOR = "#008800"
MAINUPTEXTCOLOR = "#00FF00"


ADJBTNDOWNCOLOR = MAINDOWNCOLOR
ADJBTNDOWNTEXTCOLOR = MAINDOWNTEXTCOLOR
ADJBTNUPCOLOR = MAINUPCOLOR
ADJBTNUPTEXTCOLOR = MAINUPTEXTCOLOR
ADJTIMEDOWNBKGNDCOLOR = MAINDOWNCOLOR
ADJTIMEFONTSZ = 9
ADJTIMETXTCOLOR = "#CCCCCC"
ADJTIMEUPBKGNDCOLOR = MAINUPCOLOR

BTNUPCOLOR = MAINUPCOLOR
BTNUPTEXTCOLOR = MAINUPTEXTCOLOR
BTNDOWNCOLOR = MAINDOWNCOLOR
BTNDOWNTEXTCOLOR = MAINDOWNTEXTCOLOR

BTNQUITCOLOR = "#440022"
BTNQUITTEXTCOLOR = "#660044"

BTNFONTSZ = 12

BTNTASKDOWNCOLOR = MAINDOWNCOLOR
BTNTASKDOWNTEXTCOLOR = MAINDOWNTEXTCOLOR
BTNTASKUPCOLOR = MAINUPCOLOR
BTNTASKUPTEXTCOLOR = MAINUPTEXTCOLOR

BTNZEROCOLOR = "#440022"
BTNZEROTEXTCOLOR = "#666600"

COUNTERCOLOR = "#009999"
COUNTERFONTSZ = 20

FONT = "Source Code Pro"
LABELFONTSZ = 12
LASTFILENAME = "biditi.last"

MODE_NORMAL = "MODE_NORMAL"
MODE_RESTART = "MODE_RESTART"
MODE_START = "MODE_START"

MYFACTOR = 10
MYSCALE = 100
SETTIMERFONTSZ = 20
SPACECOLOR = "#888888"
SPACEFONTSZ = 10

STOPMODE_BUTTON = "STOPMODE_BUTTON"
STOPMODE_CYCLE = "STOPMODE_CYCLE"
TASKCOUNTERCOLOR = "#448811"
TIMERTEXTCOLOR = "#2F0004"
TIMERDOWNBKGNDCOLOR = "#880000"
TIMERFONTSZ = 60
TIMEROFFBKGNDCOLOR = "#000000"
TIMERUPBKGNDCOLOR = "#008800"
TIMERUPTEXTCOLOR = MAINUPTEXTCOLOR
TIMERDOWNTEXTCOLOR = MAINDOWNTEXTCOLOR


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# up and down buttons in various sizes, and base 64 encoded for ease of use
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

UP16 = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABhGlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV8/pFIqHewg4pChOlkQFREnrUIRKoRaoVUHk0u/oElDkuLiKLgWHPxYrDq4OOvq4CoIgh8gTo5Oii5S4v+SQosYD4778e7e4+4d4G9WmWoGxwBVs4xMKink8qtC6BURhBFEFDMSM/U5UUzDc3zdw8fXuwTP8j735+hTCiYDfALxLNMNi3iDeGrT0jnvE8dYWVKIz4lHDbog8SPXZZffOJcc9vPMmJHNzBPHiIVSF8tdzMqGSjxJHFdUjfL9OZcVzluc1Wqdte/JXxgpaCvLXKc5hBQWsQQRAmTUUUEVFhK0aqSYyNB+0sM/6PhFcsnkqoCRYwE1qJAcP/gf/O7WLE6Mu0mRJNDzYtsfw0BoF2g1bPv72LZbJ0DgGbjSOv5aE5j+JL3R0eJHQHQbuLjuaPIecLkDDDzpkiE5UoCmv1gE3s/om/JA/y0QXnN7a+/j9AHIUlfpG+DgEBgpUfa6x7t7u3v790y7vx9hQHKgQe6DxQAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+QMCgQWChAICkQAAAAodEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVAgYnkgR2FlbGljR3JpbWV30quOAAAAUklEQVQ4y2NgwAN8Gxj++zYw/MenhomBQsCIz3Zk/uYG7Gpp4wJc/sbmCuq7gFCoo7uCui4gZDs2V1DPBcTaju4K6riAVNuRXUG5C8i1nWqxAAA1fxd8PnJqSQAAAABJRU5ErkJggg=='
DN16 = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABhGlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV8/pFIqHewg4pChOlkQFREnrUIRKoRaoVUHk0u/oElDkuLiKLgWHPxYrDq4OOvq4CoIgh8gTo5Oii5S4v+SQosYD4778e7e4+4d4G9WmWoGxwBVs4xMKink8qtC6BURhBFEFDMSM/U5UUzDc3zdw8fXuwTP8j735+hTCiYDfALxLNMNi3iDeGrT0jnvE8dYWVKIz4lHDbog8SPXZZffOJcc9vPMmJHNzBPHiIVSF8tdzMqGSjxJHFdUjfL9OZcVzluc1Wqdte/JXxgpaCvLXKc5hBQWsQQRAmTUUUEVFhK0aqSYyNB+0sM/6PhFcsnkqoCRYwE1qJAcP/gf/O7WLE6Mu0mRJNDzYtsfw0BoF2g1bPv72LZbJ0DgGbjSOv5aE5j+JL3R0eJHQHQbuLjuaPIecLkDDDzpkiE5UoCmv1gE3s/om/JA/y0QXnN7a+/j9AHIUlfpG+DgEBgpUfa6x7t7u3v790y7vx9hQHKgQe6DxQAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+QMCgQZDH7zs74AAAAodEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVAgYnkgR2FlbGljR3JpbWV30quOAAAAUklEQVQ4y7XRywkAIAwE0Yn92VN6skA9iCAi/hL3HuZBRCMZwwLGCcCrQhPiI3hRaKq3foIbRav7C04Uff2PYKUY6/8EM8Ws7iJY/zuSd18xCwrWFRd8Hac2awAAAABJRU5ErkJggg=='
UP32 = b'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'
DN32 = b'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'
UP96 = b'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'
DN96 = b'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'
DN64 = b'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'
UP64 = b'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'

CWD = PATH.abspath(".")
if CWD.find("_android") > -1:
	CONFIGDIRECTORY = ""
	UPIMAGE = UP64
	DOWNIMAGE = DN64
	SG.ChangeLookAndFeel("DarkPurple6")
elif CWD.find("_DEV") > -1:
	SG.ChangeLookAndFeel("DarkGreen5")
	CONFIGDIRECTORY = "/home/will/.config/biditi_DEV/"
	UPIMAGE = UP16
	DOWNIMAGE = DN16
else:
	CONFIGDIRECTORY = "/home/will/.config/biditi/"
	SG.ChangeLookAndFeel("DarkPurple6")
	UPIMAGE = UP16
	DOWNIMAGE = DN16


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# currentData dict keys and uses
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

BUTTON = "BUTTON"
DOWNSEC = "DOWNSEC"
EVENTS = "EVENTS"
FILENAME = "FILENAME"
TASK1COUNT = "TASK1COUNT"
TASK1DOWNTIMER = "TASK1DOWNTIMER"
TASK1UPTIMER = "TASK1UPTIMER"
TASK2COUNT = "TASK2COUNT"
TASK2DOWNTIMER = "TASK2DOWNTIMER"
TASK2UPTIMER = "TASK2UPTIMER"
TASK3COUNT = "TASK3COUNT"
TASK3DOWNTIMER = "TASK3DOWNTIMER"
TASK3UPTIMER = "TASK3UPTIMER"
TASK4COUNT = "TASK4COUNT"
TASK4DOWNTIMER = "TASK4DOWNTIMER"
TASK4UPTIMER = "TASK4UPTIMER"
TEXTNAME = "TEXTNAME"
UPSEC = "UPSEC"


DEFAULTS = [
	(DOWNSEC, 0,),
	(EVENTS, [],),
	(FILENAME, "biditi.pkl",),
	(TASK1COUNT, 0,),
	(TASK1DOWNTIMER, 7,),
	(TASK1UPTIMER, 14,),
	(TASK2COUNT, 0,),
	(TASK2DOWNTIMER, 7,),
	(TASK2UPTIMER, 14,),
	(TASK3COUNT, 0,),
	(TASK3DOWNTIMER, 7,),
	(TASK3UPTIMER, 14,),
	(TASK4COUNT, 0,),
	(TASK4DOWNTIMER, 7,),
	(TASK4UPTIMER, 14,),
	(TEXTNAME, "biditi.txt",),
	(UPSEC, 0,),
]

def defaults():
	defaultsRtn = {}
	for entry in DEFAULTS:
		defaultsRtn[entry[0]] = entry[1]
	return defaultsRtn


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# get a few things done that will be used by functions, but were unneeded by the init above
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

currentData = defaults()
directionUp = True
myFactor = MYFACTOR
myScale = MYSCALE
ticks = 0
timerRunning = False


def pickleIt(fileName, dataToPickle):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	with open(CONFIGDIRECTORY + fileName, 'wb') as FD_OUT_:
		PD.dump(dataToPickle, FD_OUT_)
		FD_OUT_.flush()
		FD_OUT_.close()
	with open(CONFIGDIRECTORY + LASTFILENAME, "tw") as FD_OUT_:
		FD_OUT_.writelines(fileName)
		FD_OUT_.flush()
		FD_OUT_.close()
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


def unPickleIt(fileName):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	with open(CONFIGDIRECTORY + fileName, "rb") as FD_IN_:
		dataToRTN_ = PD.load(FD_IN_)
	return dataToRTN_
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


def getData(fileName):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	global currentData
	if PATH.exists(CONFIGDIRECTORY + fileName):
		currentData = unPickleIt(fileName)
	else:
		currentData = defaults()
		pickleIt(fileName, currentData)
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


def makeTime(secondsIn):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	secondsIn = int(secondsIn)
	strRTN = f"{int(secondsIn // 60):02d}:{int(secondsIn % 60):02d}"
	return strRTN
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


def myInit():
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	if PATH.exists(CONFIGDIRECTORY + LASTFILENAME):
		# print(f"lastfilename {LASTFILENAME} being opened\n")
		with open(CONFIGDIRECTORY + LASTFILENAME, "tr") as FD_IN_:
			filename = FD_IN_.readline()
		getData(filename)
	else:
		pickleIt(LASTFILENAME, currentData)
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


myInit()


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# buttons defined here, don't forget to ** double unpack these when used
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

ADJBTNDOWN = {
	"image_data": DOWNIMAGE,
	"focus": True,
	"button_color": (ADJBTNDOWNTEXTCOLOR, ADJBTNDOWNCOLOR),
}

ADJBTNUP = {
	"image_data": UPIMAGE,
	"focus": True,
	"button_color": (ADJBTNUPTEXTCOLOR, ADJBTNUPCOLOR),
}

BTNDOWN = {
	"image_data": DN32,
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDOWNTEXTCOLOR, BTNDOWNCOLOR),
}

BTNUP = {
	"image_data": UP32,
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNUPTEXTCOLOR, BTNUPCOLOR),
}

BTNQUIT = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNQUITTEXTCOLOR, BTNQUITCOLOR),
}

BTNTASKUP = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNTASKUPTEXTCOLOR, BTNTASKUPCOLOR),
}

BTNTASKDOWN = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNTASKDOWNTEXTCOLOR, BTNTASKDOWNCOLOR),
}

BTNZEROALL = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNZEROTEXTCOLOR, BTNZEROCOLOR),
}


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# text parameters
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
TEXTADJTIMEDOWN = {
	"size": (5, 1),
	"text_color": ADJBTNDOWNTEXTCOLOR,
	"font": (FONT, ADJTIMEFONTSZ),
	"justification": "center",
	"background_color": ADJTIMEDOWNBKGNDCOLOR,
}

TEXTADJTIMEUP = {
	"size": (5, 1),
	"text_color": ADJBTNUPTEXTCOLOR,
	"font": (FONT, ADJTIMEFONTSZ),
	"justification": "center",
	"background_color": ADJTIMEUPBKGNDCOLOR,
}

TEXTTIMERDOWN = {
	"size": (5, 1),
	"text_color": TIMERDOWNTEXTCOLOR,
	"font": (FONT, SETTIMERFONTSZ),
	"justification": "center",
	"background_color": TIMERDOWNBKGNDCOLOR,
}

TEXTTIMERUP = {
	"size": (5, 1),
	"text_color": TIMERUPTEXTCOLOR,
	"font": (FONT, SETTIMERFONTSZ),
	"justification": "center",
	"background_color": TIMERUPBKGNDCOLOR,
}

TEXTSPACE1 = {
	"size": (3, 1),
	"text_color": SPACECOLOR,
	"font": (FONT, SPACEFONTSZ),
	"justification": "center",
}
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# columns, remember to ** unpack as appropriate
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

CLMADJTIMES = [
	[SG.Text(
		"",
		key="_upTime_",
		**TEXTTIMERUP,
	),],
	[SG.Text(
		"",
		key="_downTime_",
		**TEXTTIMERDOWN,
	),],
	[SG.Btn(
		"Quit",
		**BTNQUIT,
	)],
	[SG.Btn(
		"zeroAll",
		**BTNZEROALL,
	)]
]

CLMTASK1 = [
	[SG.Button(
		"task1+",
		**BTNTASKUP,
	),],
	[SG.Text(
		"",
		size=(3, 1),
		text_color=TASKCOUNTERCOLOR,
		font=(FONT, COUNTERFONTSZ),
		justification="center",
		key="_task1count_",
	),],
	[SG.Button(
		"task1-",
		**BTNTASKDOWN,
	),],
	[SG.Btn(
		"",
		key="U1M+",
		**ADJBTNUP,
	),
	SG.Btn(
		"",
		key="U1S+",
		**ADJBTNUP,
	),
	SG.Btn(
		"",
		key="D1M+",
		**ADJBTNUP,
	),
	SG.Btn(
		"",
		key="D1S+",
		**ADJBTNUP,
	),],
	[SG.Text(
		"00:00",
		key="_task1UpTimer_",
		**TEXTADJTIMEUP,
	),
	SG.Text(
		"00:00",
		key="_task1DownTimer_",
		**TEXTADJTIMEDOWN,
	),],
	[SG.Btn(
		"",
		key="U1M-",
		**ADJBTNDOWN,
	),
	SG.Btn(
		"",
		key="U1S-",
		**ADJBTNDOWN,
	),
	SG.Btn(
		"",
		key="D1M-",
		**ADJBTNDOWN,
	),
	SG.Btn(
		"",
		key="D1S-",
		**ADJBTNDOWN,
	),],
]

CLMTASK2 = [
	[SG.Button(
		"task2+",
		**BTNTASKUP,
	),],
	[SG.Text(
		"",
		size=(3, 1),
		text_color=TASKCOUNTERCOLOR,
		font=(FONT, COUNTERFONTSZ),
		justification="center",
		key="_task2count_",
	),],
	[SG.Button(
		"task2-",
		**BTNTASKDOWN,
	),],
	[SG.Btn(
		"",
		key="U2M+",
		**ADJBTNUP,
	),
	SG.Btn(
		"",
		key="U2S+",
		**ADJBTNUP,
	),
	SG.Btn(
		"",
		key="D2M+",
		**ADJBTNUP,
	),
	SG.Btn(
		"",
		key="D2S+",
		**ADJBTNUP,
	),],
	[SG.Text(
		"00:00",
		key="_task2UpTimer_",
		**TEXTADJTIMEUP,
	),
	SG.Text(
		"00:00",
		key="_task2DownTimer_",
		**TEXTADJTIMEDOWN,
	),],
	[SG.Btn(
		"",
		key="U2M-",
		**ADJBTNDOWN,
	),
	SG.Btn(
		"",
		key="U2S-",
		**ADJBTNDOWN,
	),
	SG.Btn(
		"",
		key="D2M-",
		**ADJBTNDOWN,
	),
	SG.Btn(
		"",
		key="D2S-",
		**ADJBTNDOWN,
	),],
]

CLMTASK3 = [
	[SG.Button(
		"task3+",
		**BTNTASKUP,
	),],
	[SG.Text(
		"",
		size=(3, 1),
		text_color=TASKCOUNTERCOLOR,
		font=(FONT, COUNTERFONTSZ),
		justification="center",
		key="_task3count_",
	),],
	[SG.Button(
		"task3-",
		**BTNTASKDOWN,
	),],
	[SG.Btn(
		"",
		key="U3M+",
		**ADJBTNUP,
	),
	SG.Btn(
		"",
		key="U3S+",
		**ADJBTNUP,
	),
	SG.Btn(
		"",
		key="D3M+",
		**ADJBTNUP,
	),
	SG.Btn(
		"",
		key="D3S+",
		**ADJBTNUP,
	),],
	[SG.Text(
		"00:00",
		key="_task3UpTimer_",
		**TEXTADJTIMEUP,
	),
	SG.Text(
		"00:00",
		key="_task3DownTimer_",
		**TEXTADJTIMEDOWN,
	),],
	[SG.Btn(
		"",
		key="U3M-",
		**ADJBTNDOWN,
	),
	SG.Btn(
		"",
		key="U3S-",
		**ADJBTNDOWN,
	),
	SG.Btn(
		"",
		key="D3M-",
		**ADJBTNDOWN,
	),
	SG.Btn(
		"",
		key="D3S-",
		**ADJBTNDOWN,
	),],
]

CLMTASK4 = [
	[SG.Button(
		"task4+",
		**BTNTASKUP,
	),],
	[SG.Text(
		"",
		size=(3, 1),
		text_color=TASKCOUNTERCOLOR,
		font=(FONT, COUNTERFONTSZ),
		justification="center",
		key="_task4count_",
	),],
	[SG.Button(
		"task4-",
		**BTNTASKDOWN,
	),],
	[SG.Btn(
		"",
		key="U4M+",
		**ADJBTNUP,
	),
	SG.Btn(
		"",
		key="U4S+",
		**ADJBTNUP,
	),
	SG.Btn(
		"",
		key="D4M+",
		**ADJBTNUP,
	),
	SG.Btn(
		"",
		key="D4S+",
		**ADJBTNUP,
	),],
	[SG.Text(
		"00:00",
		key="_task4UpTimer_",
		**TEXTADJTIMEUP,
	),
	SG.Text(
		"00:00",
		key="_task4DownTimer_",
		**TEXTADJTIMEDOWN,
	),],
	[SG.Btn(
		"",
		key="U4M-",
		**ADJBTNDOWN,
	),
	SG.Btn(
		"",
		key="U4S-",
		**ADJBTNDOWN,
	),
	SG.Btn(
		"",
		key="D4M-",
		**ADJBTNDOWN,
	),
	SG.Btn(
		"",
		key="D4S-",
		**ADJBTNDOWN
	),],
]


CLMTIMER = [
	[SG.Text(
		"timer", size=(5, 1),
		text_color=TIMERTEXTCOLOR,
		font=(FONT, TIMERFONTSZ),
		justification="center",
		key="_timer_",
	),],
]

layout = [
	[
		SG.Col(CLMTIMER),
		SG.Col(CLMADJTIMES),
	],
	[
		SG.Col(CLMTASK1),
		SG.Col(CLMTASK2),
		SG.Col(CLMTASK3),
		SG.Col(CLMTASK4),
	],
]


window = SG.Window("biditi", layout, location=(0, 0), element_padding=(0, 0)).finalize()


def nowStr(dtObj=DT.now()):
	return dtObj.strftime("%Y%m%d.%H%M%S")


def updateTime():
	# update timer and cycleCount
	tempTimerVAL = ticks // myFactor
	timerSTR = makeTime(tempTimerVAL)
	window.Element("_timer_").Update(value=timerSTR)
	window.Element("_task1count_").Update(value=(f"{currentData[TASK1COUNT]:03d}"))
	window.Element("_task2count_").Update(value=(f"{currentData[TASK2COUNT]:03d}"))
	window.Element("_task3count_").Update(value=(f"{currentData[TASK3COUNT]:03d}"))
	window.Element("_task4count_").Update(value=(f"{currentData[TASK4COUNT]:03d}"))

	window.Element("_upTime_").Update(value=(makeTime(currentData[UPSEC])))
	window.Element("_downTime_").Update(value=(makeTime(currentData[DOWNSEC])))

	TUpTimer = makeTime(currentData[TASK1UPTIMER])
	TDownTimer = makeTime(currentData[TASK1DOWNTIMER])
	window.Element("_task1UpTimer_").Update(value=f"{TUpTimer}")
	window.Element("_task1DownTimer_").Update(value=f"{TDownTimer}")

	TUpTimer = makeTime(currentData[TASK2UPTIMER])
	TDownTimer = makeTime(currentData[TASK2DOWNTIMER])
	window.Element("_task2UpTimer_").Update(value=f"{TUpTimer}")
	window.Element("_task2DownTimer_").Update(value=f"{TDownTimer}")

	TUpTimer = makeTime(currentData[TASK3UPTIMER])
	TDownTimer = makeTime(currentData[TASK3DOWNTIMER])
	window.Element("_task3UpTimer_").Update(value=f"{TUpTimer}")
	window.Element("_task3DownTimer_").Update(value=f"{TDownTimer}")

	TUpTimer = makeTime(currentData[TASK4UPTIMER])
	TDownTimer = makeTime(currentData[TASK4DOWNTIMER])
	window.Element("_task4UpTimer_").Update(value=f"{TUpTimer}")
	window.Element("_task4DownTimer_").Update(value=f"{TDownTimer}")


def incCount(inCount):
	TI = inCount + 1
	if TI > 999:
		TI = 999
	return TI


def decCount(inCount):
	TI = inCount - 1
	if TI < 0:
		TI = 0
	return TI


def incTime(inSeconds, increment):
	TInSeconds = inSeconds + increment
	TMin = TInSeconds // 60
	# TSec = TInSeconds % 60
	if TMin > 99:
		TInSeconds = (99 * 60) + 59
	return TInSeconds


def decTime(inSeconds, increment):
	TInSeconds = inSeconds - increment
	if TInSeconds < 0:
		TInSeconds = 0
	return TInSeconds


def updateTimerBackground(COLOR):
	# put change background code
	window.Element("_timer_").Update(background_color=COLOR)


def doStartButton():
	window.find_element("Go/Stop").Update(**BTNSTART)


def doStopButton():
	window.find_element("Go/Stop").Update(**BTNSTOP)


def zeroStuff(modeIn):
	global ticks, directionUp, currentData
	ticks = 0
	directionUp = True
	updateTime()
	updateTimerBackground(TIMEROFFBKGNDCOLOR)
	if modeIn == MODE_NORMAL:
		currentData = defaults()
		pickleIt(currentData[FILENAME], currentData)
	updateTime()


def startTimer():
	global timerRunning, currentData
	timerRunning = True
	updateTimerBackground(TIMERUPBKGNDCOLOR)
	updateTime()


def stopTimer(stopMode):
	global timerRunning
	timerRunning = False
	updateTimerBackground(TIMEROFFBKGNDCOLOR)
	updateTime()


def getValues(inValues):
	global currentData
	for key, item in DEFAULTSVALUESNDX.items():
		currentData[key] = inValues[item]


def addEvent(event2add):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	global currentData
	entryToAdd = [nowStr(DT.now()), event2add]
	# currentData[EVENTS].append(entryToAdd)
	pickleIt(currentData[FILENAME], currentData)
	with open(CONFIGDIRECTORY + currentData[TEXTNAME], "ta") as FDOut:
		outStr = ""
		outStr += f"""{entryToAdd}	{currentData[TASK1COUNT]}	{currentData[TASK2COUNT]}	{currentData[TASK3COUNT]}	{currentData[TASK4COUNT]}
"""
		# print(outStr)
		FDOut.writelines(outStr)
		FDOut.flush()
		FDOut.close()
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


getData(currentData[FILENAME])
updateTime()


while True:  # Event Loop
	event, values = window.Read(timeout=myScale)  # use as high of a timeout value as you can
	if event is None or event == "Quit":  # X or quit button clicked
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		addEvent(event)
		stopTimer(STOPMODE_BUTTON)
		pickleIt(currentData[FILENAME], currentData)
		break
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "zeroAll":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		zeroStuff(MODE_NORMAL)
		stopTimer(STOPMODE_BUTTON)
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣

	elif event == "task1+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK1COUNT] = incCount(currentData[TASK1COUNT])
		currentData[UPSEC] = currentData[TASK1UPTIMER]
		currentData[DOWNSEC] = currentData[TASK1DOWNTIMER]
		updateTime()
		if not timerRunning:
			zeroStuff(MODE_RESTART)
			startTimer()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "task2+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK2COUNT] = incCount(currentData[TASK2COUNT])
		currentData[UPSEC] = currentData[TASK2UPTIMER]
		currentData[DOWNSEC] = currentData[TASK2DOWNTIMER]
		updateTime()
		if not timerRunning:
			zeroStuff(MODE_RESTART)
			startTimer()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "task3+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK3COUNT] = incCount(currentData[TASK3COUNT])
		currentData[UPSEC] = currentData[TASK3UPTIMER]
		currentData[DOWNSEC] = currentData[TASK3DOWNTIMER]
		updateTime()
		if not timerRunning:
			zeroStuff(MODE_RESTART)
			startTimer()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "task4+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK4COUNT] = incCount(currentData[TASK4COUNT])
		currentData[UPSEC] = currentData[TASK4UPTIMER]
		currentData[DOWNSEC] = currentData[TASK4DOWNTIMER]
		updateTime()
		if not timerRunning:
			zeroStuff(MODE_RESTART)
			startTimer()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣

	elif event == "task1-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK1COUNT] = decCount(currentData[TASK1COUNT])
		updateTime()
		if timerRunning:
			stopTimer(STOPMODE_BUTTON)
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "task2-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK2COUNT] = decCount(currentData[TASK2COUNT])
		updateTime()
		if timerRunning:
			stopTimer(STOPMODE_BUTTON)
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "task3-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK3COUNT] = decCount(currentData[TASK3COUNT])
		updateTime()
		if timerRunning:
			stopTimer(STOPMODE_BUTTON)
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "task4-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK4COUNT] = decCount(currentData[TASK4COUNT])
		updateTime()
		if timerRunning:
			stopTimer(STOPMODE_BUTTON)
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣

	elif event == "U1M+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK1UPTIMER] = incTime(currentData[TASK1UPTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "U1S+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK1UPTIMER] = incTime(currentData[TASK1UPTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D1M+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK1DOWNTIMER] = incTime(currentData[TASK1DOWNTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D1S+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK1DOWNTIMER] = incTime(currentData[TASK1DOWNTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	# getValues(values)

	elif event == "U2M+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK2UPTIMER] = incTime(currentData[TASK2UPTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "U2S+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK2UPTIMER] = incTime(currentData[TASK2UPTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D2M+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK2DOWNTIMER] = incTime(currentData[TASK2DOWNTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D2S+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK2DOWNTIMER] = incTime(currentData[TASK2DOWNTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣

	elif event == "U3M+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK3UPTIMER] = incTime(currentData[TASK3UPTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "U3S+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK3UPTIMER] = incTime(currentData[TASK3UPTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D3M+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK3DOWNTIMER] = incTime(currentData[TASK3DOWNTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D3S+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK3DOWNTIMER] = incTime(currentData[TASK3DOWNTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣

	elif event == "U4M+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK4UPTIMER] = incTime(currentData[TASK4UPTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "U4S+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK4UPTIMER] = incTime(currentData[TASK4UPTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D4M+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK4DOWNTIMER] = incTime(currentData[TASK4DOWNTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D4S+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK4DOWNTIMER] = incTime(currentData[TASK4DOWNTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣

	elif event == "U1M-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK1UPTIMER] = decTime(currentData[TASK1UPTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "U1S-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK1UPTIMER] = decTime(currentData[TASK1UPTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D1M-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK1DOWNTIMER] = decTime(currentData[TASK1DOWNTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D1S-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK1DOWNTIMER] = decTime(currentData[TASK1DOWNTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	# getValues(values)

	elif event == "U2M-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK2UPTIMER] = decTime(currentData[TASK2UPTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "U2S-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK2UPTIMER] = decTime(currentData[TASK2UPTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D2M-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK2DOWNTIMER] = decTime(currentData[TASK2DOWNTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D2S-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK2DOWNTIMER] = decTime(currentData[TASK2DOWNTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣

	elif event == "U3M-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK3UPTIMER] = decTime(currentData[TASK3UPTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "U3S-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK3UPTIMER] = decTime(currentData[TASK3UPTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D3M-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK3DOWNTIMER] = decTime(currentData[TASK3DOWNTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D3S-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK3DOWNTIMER] = decTime(currentData[TASK3DOWNTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣

	elif event == "U4M-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK4UPTIMER] = decTime(currentData[TASK4UPTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "U4S-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK4UPTIMER] = decTime(currentData[TASK4UPTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D4M-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK4DOWNTIMER] = decTime(currentData[TASK4DOWNTIMER], 60)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "D4S-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK4DOWNTIMER] = decTime(currentData[TASK4DOWNTIMER], 1)
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣

	upTicks = int(currentData[UPSEC] * myFactor)
	downTicks = int(currentData[DOWNSEC] * myFactor)

	if event != "__TIMEOUT__":
		# currentData[AUTOGO1] = values[DEFAULTSVALUESNDX[AUTOGO1]]
		# currentData[AUTOGO2] = values[DEFAULTSVALUESNDX[AUTOGO2]]
		# currentData[AUTOGO3] = values[DEFAULTSVALUESNDX[AUTOGO3]]
		# currentData[AUTOGO4] = values[DEFAULTSVALUESNDX[AUTOGO4]]
		# currentData[CYCLE] = values[VALDXCYCLE]  # cycle up and down until stopped checkbox
		addEvent(event)
	if timerRunning:
		if directionUp is True:
			ticks += 1
		else:
			ticks -= 1
		# print(ticks)
		updateTime()
		if directionUp & (ticks >= upTicks):
			updateTimerBackground(TIMERDOWNBKGNDCOLOR)
			directionUp = False
			ticks = downTicks
		if directionUp is False and ticks <= myFactor:
			ticks = 0
			stopTimer(STOPMODE_CYCLE)
	else:
		updateTimerBackground(TIMEROFFBKGNDCOLOR)


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# end of biditi.property
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
