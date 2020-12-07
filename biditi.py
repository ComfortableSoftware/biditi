#!/usr/bin/python


from datetime import datetime as DT
from os import path as PATH
import pickle as PD
import PySimpleGUI as SG


CWD = PATH.abspath(".")
if CWD.find("_DEV") > -1:
	SG.ChangeLookAndFeel("DarkGreen5")
	CONFIGDIRECTORY = "/home/will/.config/biditi_DEV/"
elif CWD.find("_android") > -1:
	CONFIGDIRECTORY = ""
	SG.ChangeLookAndFeel("DarkPurple6")
else:
	CONFIGDIRECTORY = "/home/will/.config/biditi/"
	SG.ChangeLookAndFeel("DarkPurple6")


BLACK = "#000000"
BTNDEFAULTTXTCOLOR = "#111111"
BTNDOWNCOLOR = "#FF0044"
BTNFONTSZ = 12
BTNQUITCOLOR = "#992222"
BTNRESETCOLOR = "#992233"
BTNSTARTCOLOR = "#116611"
BTNSTOPCOLOR = "#662200"
BTNTASKCOLOR = "#33CC88"
BTNTASKDOWNCOLOR = "#CC3322"
BTNUPCOLOR = "#55CC00"
BTNZEROCOLOR = "#AA2233"
COUNTERFONTSZ = 20
COUNTERCOLOR = "#009999"
CYCLECOUNTERCOLOR = "#773322"
FONT = "Source Code Pro"
GRN = "#44CC33"
LABELFONTSZ = 12
LASTFILENAME = "biditi.last"
MODE_NORMAL = "MODE_NORMAL"
MODE_RESTART = "MODE_RESTART"
MODE_START = "MODE_START"
MYFACTOR = 10
MYSCALE = 100
PNK = "#FF2266"
SPACECOLOR = "#888888"
SPACEFONTSZ = 10
STARTCOL = "#44CC33"
STARTSTOPBTNTXTCOLOR = "#888822"
STOPMODE_BUTTON = "STOPMODE_BUTTON"
STOPMODE_CYCLE = "STOPMODE_CYCLE"
TASKCOUNTERCOLOR = "#448811"
TIMERCOL = "#2F0004"
TIMERDOWNBKGNDCOLOR = "#FF0000"
TIMERUPBKGNDCOLOR = "#00FF00"
TIMEROFFBKGNDCOLOR = "#000000"
TIMERFONTSZ = 60


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


VALDXCYCLE = 0
VALDXAUTOGO1 = 1
VALDXAUTOGO2 = 2
VALDXAUTOGO3 = 3
VALDXAUTOGO4 = 4


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
	(UPSEC, 14,),
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
	# print(f"filename is {fileName}")
	with open(CONFIGDIRECTORY + fileName, 'wb') as FD_OUT_:
		PD.dump(dataToPickle, FD_OUT_)
		FD_OUT_.flush()
		FD_OUT_.close()
	with open(CONFIGDIRECTORY + LASTFILENAME, "tw") as FD_OUT_:
		FD_OUT_.writelines(fileName)
		FD_OUT_.flush()
		FD_OUT_.close()


def unPickleIt(fileName):
	with open(CONFIGDIRECTORY + fileName, "rb") as FD_IN_:
		dataToRTN_ = PD.load(FD_IN_)
	return dataToRTN_


def getData(fileName):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	global currentData
	if PATH.exists(CONFIGDIRECTORY + fileName):
		currentData = unPickleIt(fileName)
	else:
		currentData = defaults()
		pickleIt(fileName, currentData)
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


def myInit():
	if PATH.exists(CONFIGDIRECTORY + LASTFILENAME):
		# print(f"lastfilename {LASTFILENAME} being opened\n")
		with open(CONFIGDIRECTORY + LASTFILENAME, "tr") as FD_IN_:
			filename = FD_IN_.readline()
		getData(filename)
	else:
		pickleIt(LASTFILENAME, currentData)


myInit()


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# buttons defined here, don't forget to ** double unpack these when used
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

BTNDOWNMINMINUS = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNDOWNCOLOR),
}

BTNDOWNMINPLUS = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNUPCOLOR),
}

BTNDOWNSECMINUS = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNDOWNCOLOR),
}

BTNDOWNSECPLUS = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNUPCOLOR),
}

BTNQUIT = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNQUITCOLOR),
}

BTNRESETC = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNRESETCOLOR),
}

BTNRESTART = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNSTARTCOLOR),
}

BTNSTART = {
	"button_color": (BTNDEFAULTTXTCOLOR, BTNSTARTCOLOR),
}

BTNGOSTOP = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BLACK),
}

BTNSTOP = {
	"button_color": (BTNDEFAULTTXTCOLOR, BTNSTOPCOLOR),
}

BTNTASKUP = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNUPCOLOR),
}

BTNTASKDOWN = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNDOWNCOLOR),
}

BTNUPMINMINUS = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNDOWNCOLOR),
}

BTNUPMINPLUS = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNUPCOLOR),
}

BTNUPSECMINUS = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNDOWNCOLOR),
}

BTNUPSECPLUS = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNUPCOLOR),
}

BTNZEROSTUFF = {
	"focus": True,
	"font": (FONT, BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNZEROCOLOR),
}


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# columns, remember to ** unpack as appropriate
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

ADJDOWNTIMEMINSCOLUMN = [
	[SG.Btn(
		"dnMin+",
		**BTNDOWNMINPLUS,
	),],
	[SG.Text(
		currentData[DOWNMIN],
		size=(3, 1),
		text_color=CYCLECOUNTERCOLOR,
		font=(FONT, COUNTERFONTSZ),
		justification="center",
		key="_dnMin_",
	),],
	[SG.Btn(
		"dnMin-",
		**BTNDOWNMINMINUS,
	),],
]

ADJDOWNTIMESECSCOLUMN = [
	[SG.Btn(
		"dnSec+",
		**BTNDOWNSECPLUS,
	),],
	[SG.Text(
		currentData[DOWNSEC],
		size=(3, 1),
		text_color=CYCLECOUNTERCOLOR,
		font=(FONT, COUNTERFONTSZ),
		justification="center",
		key="_dnSec_",
	),],
	[SG.Btn(
		"dnSec-",
		**BTNDOWNSECMINUS,
	),],
]

ADJUPTIMEMINSCOLUMN = [
	[SG.Btn(
		"upMin+",
		**BTNUPMINPLUS,
	),],
	[SG.Text(
		currentData[UPMIN],
		size=(3, 1),
		text_color=CYCLECOUNTERCOLOR,
		font=(FONT, COUNTERFONTSZ),
		justification="center",
		key="_upMin_",
	),],
	[SG.Btn(
		"upMin-",
		**BTNUPMINMINUS,
	),],
]

ADJUPTIMESECSCOLUMN = [
	[SG.Btn(
		"upSec+",
		**BTNUPSECPLUS,
	),],
	[SG.Text(
		currentData[UPSEC],
		size=(3, 1),
		text_color=CYCLECOUNTERCOLOR,
		font=(FONT, COUNTERFONTSZ),
		justification="center",
		key="_upSec_",
	),],
	[SG.Btn(
		"upSec-",
		**BTNUPSECMINUS,
	),],
]

CYCLESCOLUMN = [
	[SG.Text(
		"cycles", size=(5, 1),
		text_color=CYCLECOUNTERCOLOR,
		font=(FONT, COUNTERFONTSZ),
		justification="center",
		key="_cycleCount_",
	),],
	[SG.Checkbox(
		"cycle",
		font=(FONT, SPACEFONTSZ),
		default=currentData[CYCLE],
	),],
	[SG.Btn(
		"reset^",
		**BTNRESETC)],
]

MAINBTNSCOLUMN = [
	[SG.Button(
		"Go/Stop",
		**BTNGOSTOP,
	),],
	[SG.Button(
		"Restart",
		**BTNRESTART,
	),],
	[SG.Button(
		"Quit",
		**BTNQUIT,
	),],
	[SG.Btn(
		"ZEROALL",
		**BTNZEROSTUFF,
	),],
]

STARTSCOLUMN = [
	[SG.Text(
		"(re)starts",
		size=(4, 1),
		text_color=STARTCOL,
		font=(FONT, COUNTERFONTSZ),
		justification="center",
		key="_startCount_",
	),],
	[SG.Text(
		"starts",
		text_color=STARTSTOPBTNTXTCOLOR,
		font=(FONT, SPACEFONTSZ),
	),],
]

TASK1COLUMN = [
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
	[SG.Checkbox(
		"autogo1",
		font=(FONT, SPACEFONTSZ),
		default=currentData[AUTOGO1],
	),],
]

TASK2COLUMN = [
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
	[SG.Checkbox(
		"autogo2",
		font=(FONT, SPACEFONTSZ),
		default=currentData[AUTOGO2],
	),],
]

TASK3COLUMN = [
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
		key="_task3count_"
	),],
	[SG.Button(
		"task3-",
		**BTNTASKDOWN,
	),],
	[SG.Checkbox(
		"autogo3",
		font=(FONT, SPACEFONTSZ),
		default=currentData[AUTOGO3],
	),],
]

TASK4COLUMN = [
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
	[SG.Checkbox(
		"autogo4",
		font=(FONT, SPACEFONTSZ),
		default=currentData[AUTOGO4],
	),],
]

TIMERCOLUMN = [
	[SG.Text(
		"timer", size=(5, 1),
		text_color=TIMERCOL,
		font=(FONT, TIMERFONTSZ),
		justification="center",
		key="_timer_",
	),],
]

layout = [
	[
		SG.Col(TIMERCOLUMN),
		SG.Col(MAINBTNSCOLUMN),
	],
	[
		SG.Col(CYCLESCOLUMN),
		SG.Col(STARTSCOLUMN),
	],
	[
		SG.Col(TASK1COLUMN),
		SG.Col(TASK2COLUMN),
		SG.Col(TASK3COLUMN),
		SG.Col(TASK4COLUMN),
	],
	[
		SG.Col(ADJUPTIMEMINSCOLUMN),
		SG.Col(ADJUPTIMESECSCOLUMN),
		SG.Col(ADJDOWNTIMEMINSCOLUMN),
		SG.Col(ADJDOWNTIMESECSCOLUMN),
	],
]


window = SG.Window("biditi", layout, location=(0, 0), element_padding=(0, 0)).finalize()


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
	window.Element("_dnMin_").Update(value=f"{currentData[DOWNMIN]:d}")
	window.Element("_dnSec_").Update(value=f"{currentData[DOWNSEC]:d}")
	window.Element("_upMin_").Update(value=f"{currentData[UPMIN]:d}")
	window.Element("_upSec_").Update(value=f"{currentData[UPSEC]:d}")


def updateWindowBackground(COLOR):
	# put change background code
	window.Element("_timer_").Update(background_color=COLOR)


def doStartButton():
	window.find_element("Go/Stop").Update(**BTNSTART)


def doStopButton():
	window.find_element("Go/Stop").Update(**BTNSTOP)


def zeroStuff(modeIn):
	global ticks, cycleCount, directionUp, currentData
	ticks = 0
	directionUp = True
	updateTime()
	updateWindowBackground(TIMEROFFBKGNDCOLOR)
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
	updateWindowBackground(TIMERUPBKGNDCOLOR)
	doStopButton()
	currentData[STARTCOUNT] += 1
	updateTime()


def stopTimer(stopMode):
	global timerRunning, cycleCount
	timerRunning = False
	updateWindowBackground(TIMEROFFBKGNDCOLOR)
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
		addEvent(event)
		stopTimer(STOPMODE_BUTTON)
		pickleIt(currentData[FILENAME], currentData)
		break
	elif event == "":
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
	elif event == "ZEROALL":
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
	elif event == "dnMin+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[DOWNMIN] += 1
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "dnMin-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[DOWNMIN] -= 1
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "dnSec+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[DOWNSEC] += 1
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "downSec-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[DOWNSEC] -= 1
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "upMin+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[UPMIN] += 1
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "upMin-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[UPMIN] -= 1
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "upSec+":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[UPSEC] += 1
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif event == "upSec-":
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		currentData[UPSEC] -= 1
		updateTime()
		# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣

	currentData[AUTOGO1] = values[VALDXAUTOGO1]
	currentData[AUTOGO2] = values[VALDXAUTOGO2]
	currentData[AUTOGO3] = values[VALDXAUTOGO3]
	currentData[AUTOGO4] = values[VALDXAUTOGO4]
	currentData[CYCLE] = values[VALDXCYCLE]  # cycle up and down until stopped checkbox

	upTicks = int((currentData[UPMIN] * 60 + currentData[UPSEC]) * myFactor)
	downTicks = int((currentData[DOWNMIN] * 60 + currentData[DOWNSEC]) * myFactor)

	if event != "__TIMEOUT__":
		addEvent(event)
	if timerRunning:
		if directionUp is True:
			ticks += 1
		else:
			ticks -= 1
		# print(ticks)
		updateTime()
		if directionUp & (ticks >= upTicks):
			updateWindowBackground(TIMERDOWNBKGNDCOLOR)
			directionUp = False
			ticks = downTicks
		if directionUp is False and ticks <= myFactor:
			if currentData[CYCLE] is False:
				ticks = 0
				stopTimer(STOPMODE_CYCLE)
			else:
				updateWindowBackground(TIMERUPBKGNDCOLOR)
				directionUp = True
				cycleCount += 1
				ticks = 0
	else:
		doStartButton()
		updateWindowBackground(TIMEROFFBKGNDCOLOR)


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# end of biditi.property
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
