import os

for filename in os.listdir("States"):
	state = open("States/" + filename, "r")
	count = 0
	flip = True
	for line in state.readlines():
		if line == "\n":
			flip = True
		if flip == True:
			count += 1
			flip = False
	print(filename,count)
		