def make_readable(seconds):
	hrs = seconds/3600
	mins = (seconds%3600)/60
	secs = (seconds - (hrs * 3600) - (mins * 60))
	if hrs < 10 :
		hrs = "0"+str(hrs)
	else:
		hrs = str(hrs)
	if mins < 10 :
		mins = "0"+str(mins)
	else:
		mins = str(mins)
	if secs < 10 :
		secs = "0"+str(secs)
	else:
		secs = str(secs)

	return (hrs+":"+mins+":"+secs)