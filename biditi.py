#!/usr/bin/python

import PySimpleGUI as sg


sg.ChangeLookAndFeel('Reds')

layout = \
	[
		[
			sg.Text('', size=(5, 1), text_color='#2F0004', font=('Source Code Pro', 90), justification='center', key='_OUTPUT_'),
			sg.Text('', size=(6, 1), text_color='#400040', font=('Source Code Pro', 80), justification='center', key='_cyclecount_')
			sg.Text('', size=(6, 1), text_color='#400040', font=('Source Code Pro', 80), justification='center', key='_startcount_')
		],
		[
			sg.T(' ' * 5),
			sg.Button('Start/Stop', focus=True, font=('Source Code Pro', 20)),
			sg.Button('Restart', focus=True, font=('Source Code Pro', 20)),
			sg.Button('zeroStuff', focus=True, font=('Source Code Pro', 15))
			sg.Button('Quit', font=('Source Code Pro', 20), focus=True),
			sg.Checkbox('cycle', font=('Source Code Pro', 20), default=True),
		],
		[
			sg.Text('up min', size=(8, 1), font=('Source Code Pro', 20)),
			sg.Slider(range=(0, 60), orientation='h', size=(20, 20), default_value=0, font=('Source Code Pro', 20)),
			sg.Text('up sec', size=(8, 1), font=('Source Code Pro', 20)),
			sg.Slider(range=(0, 60), orientation='h', size=(20, 20), default_value=8, font=('Source Code Pro', 20))
		],
		[
			sg.Text('down min', size=(8, 1), font=('Source Code Pro', 20)),
			sg.Slider(range=(0, 60), orientation='h', size=(20, 20), default_value=0, font=('Source Code Pro', 20)),
			sg.Text('down sec', size=(8, 1), font=('Source Code Pro', 20)),
			sg.Slider(range=(0, 60), orientation='h', size=(20, 20), default_value=6, font=('Source Code Pro', 20)),
		],
	]

window = sg.Window('biditi', layout).finalize()


cycle = True
cyclecount = 0
directionUp = True
myFactor = 10
myScale = 100
startcount = 0
ticks = 0
timer_running = True


MODE_NORMAL = "MODE_NORMAL"
MODE_RESTART = "MODE_RESTART"
MODE_START = "MODE_START"


def updateWindowBackground(COLOR):
	# put change background code
	window.Element('_OUTPUT_').Update(background_color=COLOR)


def updateTime():
	# update timer and cyclecount
	window.Element('_OUTPUT_').Update(value=('{:02d}:{:02d}'.format(ticks // myFactor // 60, ticks // myFactor % 60)))
	window.Element('_cyclecount_').Update(value=('{:04d}'.format(cyclecount)))


def zeroStuff(modeIn):
	global ticks, cyclecount, directionUp, startcount
	ticks = 0
	directionUp = True
	updateTime()
	updateWindowBackground('Green')
	if modeIn == MODE_NORMAL:
		cyclecount = 0
	elif modeIn == MODE_RESTART:
		startcount += 1
	elif modeIn == MODE_START:
		startcount += 1


updateTime()
zeroStuff()
updateWindowBackground('Black')

while True:  # Event Loop
	event, values = window.Read(timeout=myScale)  # use as high of a timeout value as you can
	if event is None or event == 'Quit':  # X or quit button clicked
		break
	elif event == 'Start/Stop':
		timer_running = (not timer_running)
		print(timer_running)
		if timer_running:
			zeroStuff()
		else:
			updateWindowBackground('Black')
	elif (event == 'Restart') and timer_running:
		zeroStuff()
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
			if not cycle:
				timer_running = False
				ticks = 0
				updateWindowBackground('Black')
				updateTime()
			else:
				cyclecount += 1
				cyclecount = cyclecount % 10000
				updateWindowBackground('Green')
				directionUp = True
				ticks = 0
