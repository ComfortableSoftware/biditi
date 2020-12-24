

def setTimer(timeInt):
	bits_ = timeInt % 100
	timeInt = timeInt // 100
	mins_ = int(timeInt // 60)
	secs_ = int(timeInt % 60)
	tens_ = int(bits_)
	print(f"""{timeInt}  {mins_}:{secs_}:{tens_}""")
