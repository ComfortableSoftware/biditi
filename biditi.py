#!/usr/bin/python


import PySimpleGUI as sg


sg.ChangeLookAndFeel("Reds")


AUTOGO1 = True
AUTOGO2 = False
AUTOGO3 = False
AUTOGO4 = False
BTNDEFAULTTXTCOLOR = "#222222"
BTNFONTSZ = 9
BTNQUITCOLOR = "#992222"
BTNRESETCOLOR = "#992233"
BTNSTARTCOLOR = "#116611"
BTNSTOPCOLOR = "#662200"
BTNTASKCOLOR = "#33CC88"
BTNTASKDNCOLOR = "#CC3322"
BTNZEROCOLOR = "#AA2233"
COUNTERFONTSZ = 20
CYCLE = False
CYCLECOUNTERCOLOR = "#773322"
DOWNMIN = 0
DOWNSEC = 7
GRN = "#44CC33"
LABELFONTSZ = 8
MODE_NORMAL = "MODE_NORMAL"
MODE_RESTART = "MODE_RESTART"
MODE_START = "MODE_START"
MYFACTOR = 10
MYSCALE = 100
PNK = "#FF2266"
SPACECOLOR = "#888888"
SPACEFONTSZ = 9
STARTCOL = "#44CC33"
STARTCOUNT = 0
STARTSTOPBTNTXTCOLOR = "#118822"
STOPMODE_BUTTON = "STOPMODE_BUTTON"
STOPMODE_CYCLE = "STOPMODE_CYCLE"
TASK1COUNT = 0
TASK2COUNT = 0
TASK3COUNT = 0
TASK4COUNT = 0
TASKCOUNTERCOLOR = "#448811"
TIMERCOL = "#2F0004"
TIMERFONTSZ = 70
UPMIN = 0
UPSEC = 10


autogo1 = AUTOGO1
autogo2 = AUTOGO2
autogo3 = AUTOGO3
autogo4 = AUTOGO4
cycle = CYCLE
cycleCount = 0  # counted at the end of the cycle
directionUp = True
myFactor = MYFACTOR
myScale = MYSCALE
startCount = STARTCOUNT  # counted when (re)start is pushed
task1count = TASK1COUNT
task2count = TASK2COUNT
task3count = TASK3COUNT
task4count = TASK4COUNT
ticks = 0
timerRunning = False


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

BTNTASKDN = {
	"focus": True,
	"font": ("Source Code Pro", BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNTASKDNCOLOR),
}

BTNZEROSTUFF = {
	"focus": True,
	"font": ("Source Code Pro", BTNFONTSZ),
	"button_color": (BTNDEFAULTTXTCOLOR, BTNZEROCOLOR),
}

CYCLESCOLUMN = [
	[
		sg.Text("cycles", size=(5, 1), text_color=CYCLECOUNTERCOLOR, font=("Source Code Pro", COUNTERFONTSZ), justification="center", key="_cycleCount_"),
	],
	[
		sg.Checkbox("cycle", font=("Source Code Pro", SPACEFONTSZ), default=CYCLE),
	],
	[
		sg.Btn("resetC", **BTNRESETC)
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
		sg.Text("(re)starts", size=(4, 1), text_color=STARTCOL, font=("Source Code Pro", COUNTERFONTSZ), justification="center", key="_startCount_"),
	],
	[
		sg.Text("starts", text_color=STARTSTOPBTNTXTCOLOR, font=("Source Code Pro", SPACEFONTSZ))
	],
]

TASK1COLUMN = [
	[
		sg.Text("", size=(3, 1), text_color=TASKCOUNTERCOLOR, font=("Source Code Pro", COUNTERFONTSZ), justification="center", key="_task1count_"),
	],
	[
		sg.Button("task1+", **BTNTASK),
	],
	[
		sg.Button("task1-", **BTNTASKDN),
	],
	[
		sg.Checkbox("autogo1", font=("Source Code Pro", SPACEFONTSZ), default=AUTOGO1),
	],
]

TASK2COLUMN = [
	[
		sg.Text("", size=(3, 1), text_color=TASKCOUNTERCOLOR, font=("Source Code Pro", COUNTERFONTSZ), justification="center", key="_task2count_"),
	],
	[
		sg.Button("task2+", **BTNTASK),
	],
	[
		sg.Button("task2-", **BTNTASKDN),
	],
	[
		sg.Checkbox("autogo2", font=("Source Code Pro", SPACEFONTSZ), default=AUTOGO2),
	],
]

TASK3COLUMN = [
	[
		sg.Text("", size=(3, 1), text_color=TASKCOUNTERCOLOR, font=("Source Code Pro", COUNTERFONTSZ), justification="center", key="_task3count_"),
	],
	[
		sg.Button("task3+", **BTNTASK),
	],
	[
		sg.Button("task3-", **BTNTASKDN),
	],
	[
		sg.Checkbox("autogo3", font=("Source Code Pro", SPACEFONTSZ), default=AUTOGO3),
	],
]

TASK4COLUMN = [
	[
		sg.Text("", size=(3, 1), text_color=TASKCOUNTERCOLOR, font=("Source Code Pro", COUNTERFONTSZ), justification="center", key="_task4count_"),
	],
	[
		sg.Button("task4+", **BTNTASK),
	],
	[
		sg.Button("task4-", **BTNTASKDN),
	],
	[
		sg.Checkbox("autogo4", font=("Source Code Pro", SPACEFONTSZ), default=AUTOGO4),
	],
]

TIMERCOLUMN = [
	[sg.Text("timer", size=(5, 1), text_color=TIMERCOL, font=("Source Code Pro", TIMERFONTSZ), justification="center", key="_timer_"),],
	[
		sg.Button("Start/Stop", **BTNSTARTSTOP),
		sg.Button("Restart", **BTNRESTART),
		sg.Button("Quit", **BTNQUIT),
		sg.Btn("00", **BTNZEROSTUFF),
	]
]

layout = [
	[
		sg.Col(TIMERCOLUMN),
		sg.Col(CYCLESCOLUMN),
		sg.Col(STARTSCOLUMN),
		sg.Col(TASK1COLUMN),
		sg.Col(TASK2COLUMN),
		sg.Col(TASK3COLUMN),
		sg.Col(TASK4COLUMN),
	],
	[
		sg.Text("up min", size=(8, 1), font=("Source Code Pro", SPACEFONTSZ)),
		sg.Slider(range=(0, 60), orientation="h", size=(20, 20), default_value=UPMIN, font=("Source Code Pro", 20)),
		sg.Text("up sec", size=(8, 1), font=("Source Code Pro", SPACEFONTSZ)),
		sg.Slider(range=(0, 60), orientation="h", size=(20, 20), default_value=UPSEC, font=("Source Code Pro", 20))
	],
	[
		sg.Text("down min", size=(8, 1), font=("Source Code Pro", SPACEFONTSZ)),
		sg.Slider(range=(0, 60), orientation="h", size=(20, 20), default_value=DOWNMIN, font=("Source Code Pro", 20)),
		sg.Text("down sec", size=(8, 1), font=("Source Code Pro", SPACEFONTSZ)),
		sg.Slider(range=(0, 60), orientation="h", size=(20, 20), default_value=DOWNSEC, font=("Source Code Pro", 20)),
	],
]

window = sg.Window("biditi", layout).finalize()
sg.SetOptions(element_padding=(0, 0))


def updateTime():
	# update timer and cycleCount
	window.Element("_timer_").Update(value=("{:02d}:{:02d}".format(ticks // myFactor // 60, ticks // myFactor % 60)))
	window.Element("_cycleCount_").Update(value=("{:04d}".format(cycleCount)))
	window.Element("_startCount_").Update(value=("{:04d}".format(startCount)))
	window.Element("_task1count_").Update(value=("{:03d}".format(task1count)))
	window.Element("_task2count_").Update(value=("{:03d}".format(task2count)))
	window.Element("_task3count_").Update(value=("{:03d}".format(task3count)))
	window.Element("_task4count_").Update(value=("{:03d}".format(task4count)))


def updateWindowBackground(COLOR):
	# put change background code
	window.Element("_timer_").Update(background_color=COLOR)


def doStartButton():
	window.find_element("Start/Stop").Update(**BTNSTART)


def doStopButton():
	window.find_element("Start/Stop").Update(**BTNSTOP)


def zeroStuff(modeIn):
	global ticks, cycleCount, directionUp, startCount, task1count, task2count, task3count, \
		task4count, cycle, autogo1, autogo2, autogo3, autogo4
	ticks = 0
	directionUp = True
	updateTime()
	updateWindowBackground("Green")
	if modeIn == MODE_NORMAL:
		cycleCount = 0
		startCount = STARTCOUNT
		task1count = TASK1COUNT
		task2count = TASK2COUNT
		task3count = TASK3COUNT
		task4count = TASK4COUNT
		cycle = CYCLE
		autogo1 = AUTOGO1
		autogo2 = AUTOGO2
		autogo3 = AUTOGO3
		autogo4 = AUTOGO4
	if modeIn == MODE_START:
		cycleCount = 0
	updateTime()


def startTimer():
	global timerRunning, startCount
	timerRunning = True
	updateWindowBackground("Green")
	doStopButton()
	startCount += 1
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


updateTime()
zeroStuff(MODE_NORMAL)


while True:  # Event Loop
	event, values = window.Read(timeout=myScale)  # use as high of a timeout value as you can
	if event is None or event == "Quit":  # X or quit button clicked
		break
	elif event == "Start/Stop":
		timerRunning = (not timerRunning)
		if timerRunning:
			zeroStuff(MODE_START)
			startTimer()
		else:
			doStopButton()
			stopTimer(STOPMODE_BUTTON)
	elif event == "Restart":
		zeroStuff(MODE_RESTART)
		startTimer()
	elif event == "00":
		zeroStuff(MODE_NORMAL)
		stopTimer(STOPMODE_BUTTON)
	elif event == "task1+":
		task1count += 1
		updateTime()
		if AUTOGO1 and not timerRunning:
			zeroStuff(MODE_RESTART)
			startTimer()
	elif event == "task2+":
		task2count += 1
		updateTime()
		if AUTOGO2 and not timerRunning:
			zeroStuff(MODE_RESTART)
			startTimer()
	elif event == "task3+":
		task3count += 1
		updateTime()
		if AUTOGO3 and not timerRunning:
			zeroStuff(MODE_RESTART)
			startTimer()
	elif event == "task4+":
		task4count += 1
		updateTime()
		if AUTOGO4 and not timerRunning:
			zeroStuff(MODE_RESTART)
			startTimer()
	elif event == "task1-":
		task1count -= 1
		updateTime()
		if AUTOGO1 and timerRunning:
			stopTimer(STOPMODE_BUTTON)
	elif event == "task2-":
		task2count -= 1
		updateTime()
		if AUTOGO2 and timerRunning:
			stopTimer(STOPMODE_BUTTON)
	elif event == "task3-":
		task3count -= 1
		updateTime()
		if AUTOGO3 and timerRunning:
			stopTimer(STOPMODE_BUTTON)
	elif event == "task4-":
		task4count -= 1
		updateTime()
		if AUTOGO4 and timerRunning:
			stopTimer(STOPMODE_BUTTON)
	elif event == "resetC":
		cycleCount = 0
		stopTimer(STOPMODE_BUTTON)

	cycle = values[0]  # cycle up and down until stopped checkbox
	upTicks = int((values[5] * 60 + values[6]) * myFactor)
	downTicks = int((values[7] * 60 + values[8]) * myFactor)
	AUTOGO1 = values[1]
	AUTOGO2 = values[2]
	AUTOGO3 = values[3]
	AUTOGO4 = values[4]

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
			if cycle is False:
				ticks = 0
				stopTimer(STOPMODE_CYCLE)
			else:
				updateWindowBackground("Green")
				directionUp = True
				cycleCount += 1
				ticks = 0
	else:
		doStartButton()
