#!/usr/bin/python

import PySimpleGUI as sg


sg.ChangeLookAndFeel('Reds')


CYCLE = False
GRN = "#44CC33"
PNK = "#FF22CC"
TIMERCOL = "#2F0004"
CYCLECOL = "#442233"
TASKCOL = "#444411"
STARTCOL = GRN


BTNSTART = {
	"focus":True,
	"font":("Source Code Pro", 12),
	"button_color":("#114422", "#000000"),
	}

BTNSTOP = {
	"focus":True,
	"font":("Source Code Pro", 12),
	"button_color":("#441122", "#000000"),
	}

BTNRESTART = {
	"focus":True,
	"font":('Source Code Pro', 12),
	"button_color":("#44DD22", "#440000"),
	}

BTNQUIT = {
	"focus":True,
	"font":('Source Code Pro', 10),
	"button_color":("#CC2255", "#440000"),
	}

BTNTASK = {
	"focus":True,
	"font":('Source Code Pro', 8),
	"button_color":(TASKCOL, "#FF0000"),
	"background_color":"#441122"
	}


layout = [
		[sg.Text('', size=(180, 7), text_color=PNK, font=('Source Code Pro', 8), justification='left', key='_label_'),],
	[
		sg.Text('timer', size=(5, 1), text_color=TIMERCOL, font=('Source Code Pro', 70), justification='center', key='_timer_'),
		sg.Text('cycles', size=(5, 1), text_color=CYCLECOL, font=('Source Code Pro', 20), justification='center', key='_cycleCount_'),
		sg.Text('(re)starts', size=(5, 1), text_color=STARTCOL, font=('Source Code Pro', 20), justification='center', key='_startCount_'),
		sg.Text('', size=(4, 1), text_color=TASKCOL, font=('Source Code Pro', 20), justification='center', key='_task1count_'),
		sg.Text('', size=(4, 1), text_color=TASKCOL, font=('Source Code Pro', 20), justification='center', key='_task2count_'),
		sg.Text('', size=(4, 1), text_color=TASKCOL, font=('Source Code Pro', 20), justification='center', key='_task3count_'),
		sg.Text('', size=(4, 1), text_color=TASKCOL, font=('Source Code Pro', 20), justification='center', key='_task4count_'),
	],
	[
		sg.Text(' ' * 5),
		sg.Button('Start/Stop', **BTNSTART),
		sg.Button('Restart', **BTNRESTART),
		sg.Button('Quit', **BTNQUIT),
		sg.Checkbox('cycle', font=('Source Code Pro', 12), default=CYCLE),
		sg.Button("task1+", BTNTASK),
		sg.Button("task2+", BTNTASK),
		sg.Button("task3+", BTNTASK),
		sg.Button("task4+", BTNTASK),
		sg.Button('zeroStuff', focus=True, font=('Source Code Pro', 8)),
	],
	[
		sg.Text('up min', size=(8, 1), font=('Source Code Pro', 20)),
		sg.Slider(range=(0, 60), orientation='h', size=(20, 20), default_value=0, font=('Source Code Pro', 20)),
		sg.Text('up sec', size=(8, 1), font=('Source Code Pro', 20)),
		sg.Slider(range=(0, 60), orientation='h', size=(20, 20), default_value=10, font=('Source Code Pro', 20))
	],
	[
		sg.Text('down min', size=(8, 1), font=('Source Code Pro', 20)),
		sg.Slider(range=(0, 60), orientation='h', size=(20, 20), default_value=0, font=('Source Code Pro', 20)),
		sg.Text('down sec', size=(8, 1), font=('Source Code Pro', 20)),
		sg.Slider(range=(0, 60), orientation='h', size=(20, 20), default_value=7, font=('Source Code Pro', 20)),
	],
]


window = sg.Window('biditi', layout).finalize()


cycle = CYCLE
cycleCount = 0  # counted at the end of the cycle
directionUp = True
myFactor = 10
myScale = 100
startCount = 0  # counted when (re)start is pushed
ticks = 0
timer_running = False
task1count = 0
task2count = 0
task3count = 0
task4count = 0


MODE_NORMAL = "MODE_NORMAL"
MODE_RESTART = "MODE_RESTART"
MODE_START = "MODE_START"


def updateWindowBackground(COLOR):
	# put change background code
	window.Element('_timer_').Update(background_color=COLOR)


def updateTime():
	# update timer and cycleCount
	window.Element('_timer_').Update(value=('{:02d}:{:02d}'.format(ticks // myFactor // 60, ticks // myFactor % 60)))
	window.Element('_cycleCount_').Update(value=('{:04d}'.format(cycleCount)))
	window.Element('_startCount_').Update(value=('{:04d}'.format(startCount)))
	window.Element('_task1count_').Update(value=('{:03d}'.format(task1count)))
	window.Element('_task2count_').Update(value=('{:03d}'.format(task2count)))
	window.Element('_task3count_').Update(value=('{:03d}'.format(task3count)))
	window.Element('_task4count_').Update(value=('{:03d}'.format(task4count)))


def doLabels():
	label1pos = 0
	label2pos = 49
	label3pos = 14
	label4pos = 14
	label5pos = 12
	label6pos = 12
	label7pos = 12

	TLabel = "TIMER\n"

	TLabel += "|" + " " * label2pos
	TLabel += "cycle counter (start clears)\n"

	TLabel += "|" + " " * label2pos
	TLabel += "|" + " " * label3pos
	TLabel += "(re)start counter\n"

	TLabel += "|" + " " * label2pos
	TLabel += "|" + " " * label3pos
	TLabel += "|" + " " * label4pos
	TLabel += "task 1 counter\n"

	TLabel += "|" + " " * label2pos
	TLabel += "|" + " " * label3pos
	TLabel += "|" + " " * label4pos
	TLabel += "|" + " " * label5pos
	TLabel += "task 2 counter\n"

	TLabel += "|" + " " * label2pos
	TLabel += "|" + " " * label3pos
	TLabel += "|" + " " * label4pos
	TLabel += "|" + " " * label5pos
	TLabel += "|" + " " * label6pos
	TLabel += "task 3 counter\n"

	TLabel += "|" + " " * label2pos
	TLabel += "|" + " " * label3pos
	TLabel += "|" + " " * label4pos
	TLabel += "|" + " " * label5pos
	TLabel += "|" + " " * label6pos
	TLabel += "|" + " " * label7pos
	TLabel += "task 4 counter\n"
	# print(TLabel)
	TLabel1 = f"""timer
|           cycle counter
|           |       start counter
|           |       |    task 1 counter
|           |       |    |     task 2 counter
|           |       |    |     |     task 3 counter
|           |       |    |     |     |    task 4 counter
"""
	window.Element("_label_").Update(value=TLabel)


def zeroStuff(modeIn):
	global ticks, cycleCount, directionUp, startCount, task1count, task2count, task3count, task4count
	ticks = 0
	directionUp = True
	updateTime()
	updateWindowBackground('Green')
	if modeIn == MODE_NORMAL:
		cycleCount = 0
		startCount = 0
		task1count = 0
		task2count = 0
		task3count = 0
		task4count = 0
	elif modeIn == MODE_RESTART or modeIn == MODE_START:
		startCount += 1
	elif modeIn == MODE_START:
		cycleCount = 0


updateTime()
zeroStuff(MODE_NORMAL)
updateWindowBackground('Black')
doLabels()


while True:  # Event Loop
	event, values = window.Read(timeout=myScale)  # use as high of a timeout value as you can
	if event is None or event == 'Quit':  # X or quit button clicked
		break
	elif event == 'Start/Stop':
		timer_running = (not timer_running)
		print(timer_running)
		if timer_running:
			zeroStuff(MODE_START)
		else:
			updateWindowBackground('Black')
	elif event == 'Restart':
		zeroStuff(MODE_RESTART)
		timer_running = True
	elif event == "zeroStuff":
		zeroStuff(MODE_NORMAL)
		updateWindowBackground('Black')
		timer_running = False
	cycle = values[0]  # cycle up and down until stopped checkbox
	upTicks = int((values[1] * 60 + values[2]) * myFactor)
	downTicks = int((values[3] * 60 + values[4]) * myFactor)
	if timer_running:
		if directionUp:
			ticks += 1
		else:
			ticks -= 1
		updateTime()
		if directionUp & (ticks >= upTicks):
			updateWindowBackground('Red')
			directionUp = False
			ticks = downTicks
		if (not directionUp) & (ticks < myFactor + 1):
			cycleCount += 1
			cycleCount = cycleCount % 10000
			if not cycle:
				timer_running = False
				ticks = 0
				updateWindowBackground('Black')
				updateTime()
			else:
				updateWindowBackground('Green')
				directionUp = True
				ticks = 0
