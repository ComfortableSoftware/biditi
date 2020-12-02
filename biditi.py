#!/usr/bin/python


from datetime import datetime as DT
from os import path as PATH
import pickle as PD
import PySimpleGUI as SG


CWD = PATH.abspath(".")
if CWD.find("_DEV") > -1:
	SG.ChangeLookAndFeel("DarkGreen1")
else:
	SG.ChangeLookAndFeel("DarkPurple6")


BTNDEFAULTTXTCOLOR = "#550044"
BTNFONTSZ = 9
BTNQUITCOLOR = "#992222"
BTNRESETCOLOR = "#992233"
BTNSTARTCOLOR = "#116611"
BTNSTOPCOLOR = "#662200"
BTNTASKCOLOR = "#33CC88"
BTNTASKDOWNCOLOR = "#CC3322"
BTNZEROCOLOR = "#AA2233"
COUNTERFONTSZ = 20
CYCLECOUNTERCOLOR = "#773322"
GRN = "#44CC33"
LABELFONTSZ = 8
LASTFILENAME = "biditi.last"
MODE_NORMAL = "MODE_NORMAL"
MODE_RESTART = "MODE_RESTART"
MODE_START = "MODE_START"
MYFACTOR = 10
MYSCALE = 100
PNK = "#FF2266"
SPACECOLOR = "#444444"
SPACEFONTSZ = 9
STARTCOLOR = "#44CC33"
STARTSTOPBTNTXTCOLOR = "#118822"
STOPMODE_BUTTON = "STOPMODE_BUTTON"
STOPMODE_CYCLE = "STOPMODE_CYCLE"
TASKCOUNTERCOLOR = "#448811"
TIMERCOLOR = "#2F0004"
TIMERFONTSZ = 70


AUTOGO1 = "AUTOGO1"
AUTOGO2 = "AUTOGO2"
AUTOGO3 = "AUTOGO3"
AUTOGO4 = "AUTOGO4"
BUTTON = "BUTTON"
CYCLE = "CYCLE"
DOWNMIN = "DOWNMIN"
DOWNSEC = "DOWNSEC"
EVENTS = "EVENTS"
FILENAME = "FILENAME"
STARTCOUNT = "STARTCOUNT"
TASK1COUNT = "TASK1COUNT"
TASK2COUNT = "TASK2COUNT"
TASK3COUNT = "TASK3COUNT"
TASK4COUNT = "TASK4COUNT"
TEXTNAME = "TEXTNAME"
TIME = "TIME"
UPMIN = "UPMIN"
UPSEC = "UPSEC"


VALNDXCYCLE = 0
VALNDXAUTOGO1 = 1
VALNDXAUTOGO2 = 2
VALNDXAUTOGO3 = 3
VALNDXAUTOGO4 = 4
VALNDXUPMIN = 5
VALNDXUPSEC = 6
VALNDXDOWNMIN = 7
VALNDXDOWNSEC = 8


DEFAULTS = [
	(AUTOGO1, True,),
	(AUTOGO2, False,),
	(AUTOGO3, False,),
	(AUTOGO4, False,),
	(CYCLE, False,),
	(DOWNMIN, 0,),
	(DOWNSEC, 7,),
	(EVENTS, [],),
	(FILENAME, "biditi.pkl",),
	(STARTCOUNT, 0,),
	(TASK1COUNT, 0,),
	(TASK2COUNT, 0,),
	(TASK3COUNT, 0,),
	(TASK4COUNT, 0,),
	(TEXTNAME, "biditi.txt",),
	(UPMIN, 0,),
	(UPSEC, 10,),
]

def defaults():
	defaultsRtn = {}
	for entry in DEFAULTS:
		defaultsRtn[entry[0]] = entry[1]
	return defaultsRtn


currentData = defaults()


cycleCount = 0  # counted at the end of the cycle
directionUp = True
myFactor = MYFACTOR
myScale = MYSCALE
ticks = 0
timerRunning = False


def pickleIt(fileName, dataToPickle):
	print(f"filename is {fileName}")
	with open(fileName, 'wb') as FD_OUT_:
		PD.dump(dataToPickle, FD_OUT_)
		FD_OUT_.flush()
		FD_OUT_.close()
	with open(LASTFILENAME, "tw") as FD_OUT_:
		FD_OUT_.writelines(fileName)
		FD_OUT_.flush()
		FD_OUT_.close()


def unPickleIt(fileName):
	with open(fileName, "rb") as FD_IN_:
		dataToRTN_ = PD.load(FD_IN_)
	return dataToRTN_


def getData(fileName):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	global currentData
	if PATH.exists(fileName):
		currentData = unPickleIt(fileName)
	else:
		currentData = defaults()
		pickleIt(fileName, currentData)
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


def myInit():
	if PATH.exists(LASTFILENAME):
		print(f"lastfilename {LASTFILENAME} being opened\n")
		with open(LASTFILENAME, "tr") as FD_IN_:
			filename = FD_IN_.readline()
		getData(filename)
	else:
		pickleIt(LASTFILENAME, currentData)


myInit()


BTNSTART = {
	"button_color": (BTNDEFAULTTXTCOLOR, BTNSTARTCOLOR),
}

BTNSTARTSTOP = {
	"focus": True,
	"font": ("Source Code Pro", BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, "Black"),
}

BTNSTOP = {
	"button_color": (BTNDEFAULTTXTCOLOR, BTNSTOPCOLOR),
}

BTNRESTART = {
	"focus": True,
	"font": ("Source Code Pro", BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNSTARTCOLOR),
}

BTNQUIT = {
	"focus": True,
	"font": ("Source Code Pro", BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNQUITCOLOR),
}

BTNRESETC = {
	"focus": True,
	"font": ("Source Code Pro", BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNRESETCOLOR),
}

BTNTASK = {
	"focus": True,
	"font": ("Source Code Pro", BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNTASKCOLOR),
}

BTNTASKDOWN = {
	"focus": True,
	"font": ("Source Code Pro", BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNTASKDOWNCOLOR),
}

BTNZEROSTUFF = {
	"focus": True,
	"font": ("Source Code Pro", BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNZEROCOLOR),
}

CYCLESCOLUMN = [
	[
		SG.Text("cycles", size=(5, 1), text_color=CYCLECOUNTERCOLOR, font=("Source Code Pro", COUNTERFONTSZ), justification="center", key="_cycleCount_"),
	],
	[
		SG.Checkbox("cycle", font=("Source Code Pro", SPACEFONTSZ), default=currentData[CYCLE]),
	],
	[
		SG.Btn("resetC", **BTNRESETC)
	],
]

SPACE1 = {
	"size": (58, 1),
	"text_color": SPACECOLOR,
	"font": ("Source Code Pro", SPACEFONTSZ),
}

SPACE2 = {
	"size": (1, 1),
	"text_color": SPACECOLOR,
	"font": ("Source Code Pro", SPACEFONTSZ),
}

SPACE3 = {
	"size": (1, 1),
	"text_color": SPACECOLOR,
	"font": ("Source Code Pro", SPACEFONTSZ),
}

SPACE4 = {
	"size": (1, 1),
	"text_color": SPACECOLOR,
	"font": ("Source Code Pro", SPACEFONTSZ),
}

STARTSCOLUMN = [
	[
		SG.Text("(re)starts", size=(4, 1), text_color=STARTCOLOR, font=("Source Code Pro", COUNTERFONTSZ), justification="center", key="_startCount_"),
	],
	[
		SG.Text("starts", text_color=STARTSTOPBTNTXTCOLOR, font=("Source Code Pro", SPACEFONTSZ))
	],
]

TASK1COLUMN = [
	[
		SG.Text("", size=(3, 1), text_color=TASKCOUNTERCOLOR, font=("Source Code Pro", COUNTERFONTSZ), justification="center", key="_task1count_"),
	],
	[
		SG.Button("task1+", **BTNTASK),
	],
	[
		SG.Button("task1-", **BTNTASKDOWN),
	],
	[
		SG.Checkbox("autogo1", font=("Source Code Pro", SPACEFONTSZ), default=currentData[AUTOGO1]),
	],
]

TASK2COLUMN = [
	[
		SG.Text("", size=(3, 1), text_color=TASKCOUNTERCOLOR, font=("Source Code Pro", COUNTERFONTSZ), justification="center", key="_task2count_"),
	],
	[
		SG.Button("task2+", **BTNTASK),
	],
	[
		SG.Button("task2-", **BTNTASKDOWN),
	],
	[
		SG.Checkbox("autogo2", font=("Source Code Pro", SPACEFONTSZ), default=currentData[AUTOGO2]),
	],
]

TASK3COLUMN = [
	[
		SG.Text("", size=(3, 1), text_color=TASKCOUNTERCOLOR, font=("Source Code Pro", COUNTERFONTSZ), justification="center", key="_task3count_"),
	],
	[
		SG.Button("task3+", **BTNTASK),
	],
	[
		SG.Button("task3-", **BTNTASKDOWN),
	],
	[
		SG.Checkbox("autogo3", font=("Source Code Pro", SPACEFONTSZ), default=currentData[AUTOGO3]),
	],
]

TASK4COLUMN = [
	[
		SG.Text("", size=(3, 1), text_color=TASKCOUNTERCOLOR, font=("Source Code Pro", COUNTERFONTSZ), justification="center", key="_task4count_"),
	],
	[
		SG.Button("task4+", **BTNTASK),
	],
	[
		SG.Button("task4-", **BTNTASKDOWN),
	],
	[
		SG.Checkbox("autogo4", font=("Source Code Pro", SPACEFONTSZ), default=currentData[AUTOGO4]),
	],
]

TIMERCOLUMN = [
	[SG.Text("timer", size=(5, 1), text_color=TIMERCOLOR, font=("Source Code Pro", TIMERFONTSZ), justification="center", key="_timer_")],
	[
		SG.Button("Start/Stop", **BTNSTARTSTOP),
		SG.Button("Restart", **BTNRESTART),
		SG.Button("Quit", **BTNQUIT),
		SG.Btn("zero", **BTNZEROSTUFF),
	]
]

layout = [
	[
		SG.Col(TIMERCOLUMN),
		SG.Col(CYCLESCOLUMN),
		SG.Col(STARTSCOLUMN),
		SG.Col(TASK1COLUMN),
		SG.Col(TASK2COLUMN),
		SG.Col(TASK3COLUMN),
		SG.Col(TASK4COLUMN),
	],
	[
		SG.Text("up min", size=(8, 1), font=("Source Code Pro", SPACEFONTSZ)),
		SG.Slider(range=(0, 60), orientation="h", size=(20, 20), default_value=currentData[UPMIN], font=("Source Code Pro", 20)),
		SG.Text("up sec", size=(8, 1), font=("Source Code Pro", SPACEFONTSZ)),
		SG.Slider(range=(0, 60), orientation="h", size=(20, 20), default_value=currentData[UPSEC], font=("Source Code Pro", 20))
	],
	[
		SG.Text("down min", size=(8, 1), font=("Source Code Pro", SPACEFONTSZ)),
		SG.Slider(range=(0, 60), orientation="h", size=(20, 20), default_value=currentData[DOWNMIN], font=("Source Code Pro", 20)),
		SG.Text("down sec", size=(8, 1), font=("Source Code Pro", SPACEFONTSZ)),
		SG.Slider(range=(0, 60), orientation="h", size=(20, 20), default_value=currentData[DOWNSEC], font=("Source Code Pro", 20)),
	],
]

window = SG.Window("biditi", layout).finalize()
SG.SetOptions(element_padding=(0, 0))


def nowStr(dtObj=DT.now()):
	return dtObj.strftime("%Y%m%d.%H%M%S")


def updateTime():
	# update timer and cycleCount
	window.Element("_timer_").Update(value=("{:02d}:{:02d}".format(ticks // myFactor // 60, ticks // myFactor % 60)))
	window.Element("_cycleCount_").Update(value=("{:04d}".format(cycleCount)))
	window.Element("_startCount_").Update(value=("{:04d}".format(currentData[STARTCOUNT])))
	window.Element("_task1count_").Update(value=("{:03d}".format(currentData[TASK1COUNT])))
	window.Element("_task2count_").Update(value=("{:03d}".format(currentData[TASK2COUNT])))
	window.Element("_task3count_").Update(value=("{:03d}".format(currentData[TASK3COUNT])))
	window.Element("_task4count_").Update(value=("{:03d}".format(currentData[TASK4COUNT])))


def updateWindowBackground(COLOR):
	# put change background code
	window.Element("_timer_").Update(background_color=COLOR)


def doStartButton():
	window.find_element("Start/Stop").Update(**BTNSTART)


def doStopButton():
	window.find_element("Start/Stop").Update(**BTNSTOP)


def zeroStuff(modeIn):
	global ticks, cycleCount, directionUp, currentData
	ticks = 0
	directionUp = True
	updateTime()
	updateWindowBackground("Green")
	if modeIn == MODE_NORMAL:
		cycleCount = 0
		currentData = defaults()
		pickleIt(currentData[FILENAME], currentData)
	if modeIn == MODE_START:
		cycleCount = 0
	updateTime()


def startTimer():
	global timerRunning, currentData
	timerRunning = True
	updateWindowBackground("Green")
	doStopButton()
	currentData[STARTCOUNT] += 1
	updateTime()


def stopTimer(stopMode):
	global timerRunning, cycleCount
	timerRunning = False
	updateWindowBackground("Black")
	doStartButton()
	if stopMode == STOPMODE_CYCLE:
		cycleCount += 1
		cycleCount = cycleCount % 10000
	updateTime()


def addEvent(event2add):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	global currentData
	entryToAdd = [nowStr(DT.now()), event2add]
	currentData[EVENTS].append(entryToAdd)
	pickleIt(currentData[FILENAME], currentData)
	with open(currentData[TEXTNAME], "ta") as FDOut:
		outStr = ""
		outStr += f"""{entryToAdd}	{currentData[TASK1COUNT]}	{currentData[TASK2COUNT]}	{currentData[TASK3COUNT]}	{currentData[TASK4COUNT]}
	"""
		print(outStr)
		FDOut.writelines(outStr)
		FDOut.flush()
		FDOut.close()
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


getData(currentData[FILENAME])
updateTime()


while True:  # Event Loop
	event, values = window.Read(timeout=myScale)  # use as high of a timeout value as you can
	if event is None or event == "Quit":  # X or quit button clicked
		addEvent(event)
		stopTimer(STOPMODE_BUTTON)
		pickleIt(currentData[FILENAME], currentData)
		break
	elif event == "Start/Stop":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		timerRunning = (not timerRunning)
		if timerRunning:
			zeroStuff(MODE_START)
			startTimer()
		else:
			doStopButton()
			stopTimer(STOPMODE_BUTTON)
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "Restart":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		zeroStuff(MODE_RESTART)
		startTimer()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "zero":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		zeroStuff(MODE_NORMAL)
		stopTimer(STOPMODE_BUTTON)
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "task1+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK1COUNT] += 1
		updateTime()
		if currentData[AUTOGO1] and not timerRunning:
			zeroStuff(MODE_RESTART)
			startTimer()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "task2+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK2COUNT] += 1
		updateTime()
		if currentData[AUTOGO2] and not timerRunning:
			zeroStuff(MODE_RESTART)
			startTimer()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "task3+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK3COUNT] += 1
		updateTime()
		if currentData[AUTOGO3] and not timerRunning:
			zeroStuff(MODE_RESTART)
			startTimer()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "task4+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK4COUNT] += 1
		updateTime()
		if currentData[AUTOGO4] and not timerRunning:
			zeroStuff(MODE_RESTART)
			startTimer()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "task1-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK1COUNT] -= 1
		updateTime()
		if currentData[AUTOGO1] and timerRunning:
			stopTimer(STOPMODE_BUTTON)
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "task2-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK2COUNT] -= 1
		updateTime()
		if currentData[AUTOGO2] and timerRunning:
			stopTimer(STOPMODE_BUTTON)
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "task3-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK3COUNT] -= 1
		updateTime()
		if currentData[AUTOGO3] and timerRunning:
			stopTimer(STOPMODE_BUTTON)
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "task4-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[TASK4COUNT] -= 1
		updateTime()
		if currentData[AUTOGO4] and timerRunning:
			stopTimer(STOPMODE_BUTTON)
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "resetC":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		cycleCount = 0
		stopTimer(STOPMODE_BUTTON)

		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣

	currentData[AUTOGO1] = values[VALNDXAUTOGO1]
	currentData[AUTOGO2] = values[VALNDXAUTOGO2]
	currentData[AUTOGO3] = values[VALNDXAUTOGO3]
	currentData[AUTOGO4] = values[VALNDXAUTOGO4]
	currentData[CYCLE] = values[VALNDXCYCLE]  # cycle up and down until stopped checkbox
	currentData[DOWNMIN] = values[VALNDXDOWNMIN]
	currentData[DOWNSEC] = values[VALNDXDOWNSEC]
	currentData[UPMIN] = values[VALNDXUPMIN]
	currentData[UPSEC] = values[VALNDXUPSEC]

	upTicks = int((values[VALNDXUPMIN] * 60 + values[VALNDXUPSEC]) * myFactor)
	downTicks = int((values[VALNDXDOWNMIN] * 60 + values[VALNDXDOWNSEC]) * myFactor)

	if event != "__TIMEOUT__":
		addEvent(event)
	if timerRunning:
		if directionUp is True:
			ticks += 1
		else:
			ticks -= 1
		updateTime()
		if directionUp & (ticks >= upTicks):
			updateWindowBackground("Red")
			directionUp = False
			ticks = downTicks
		if directionUp is False and ticks <= myFactor:
			if currentData[CYCLE] is False:
				ticks = 0
				stopTimer(STOPMODE_CYCLE)
			else:
				updateWindowBackground("Green")
				directionUp = True
				cycleCount += 1
				ticks = 0
	else:
		doStartButton()
		updateWindowBackground("Black")
