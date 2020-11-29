import PySimpleGUI as sg


layout = [[sg.Text('Stopwatch', size=(20, 2), justification='center')],
					[sg.Text('', size=(10, 2), font=('Helvetica', 20), justification='center', key='_OUTPUT_')],
					[sg.T(' ' * 5), sg.Button('Start/Stop', focus=True), sg.Quit()]]

window = sg.Window('Stopwatch Timer', layout)

timer_running, i = True, 0

while True:  # Event Loop
	event, values = window.Read(timeout=10)  # Please try and use as high of a timeout value as you can
	if event is None or event == 'Quit':  # if user closed the window using X or clicked Quit button
		break
	elif event == 'Start/Stop':
		timer_running = not timer_running
	if timer_running:
		window.Element('_OUTPUT_').Update('{:02d}:{:02d}.{:02d}'.format((i // 100) // 60, (i // 100) % 60, i % 100))
		i += 1
