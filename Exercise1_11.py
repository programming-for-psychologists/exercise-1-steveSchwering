import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400], color = "black", units = 'pix')
square = visual.Rect(win, lineColor = "black", fillColor = "blue", size = [100, 100])

square.ori = 0
Hz = 60
degrees = 360
incr = degrees / Hz
stopKey = 's'
keyPress = []
startKey = 'r'
quitKey = 'q'
shrinkKey = "right"
growKey = "left"
keyPress = []
while (quitKey not in keyPress):
	keyPress = ["a"]
	keyPress = event.getKeys(keyList = [quitKey, growKey, shrinkKey])
	currSize = square.size
	width = currSize[0] * .1
	if shrinkKey in keyPress:
		square.size += [width, 0]
	elif growKey in keyPress:
		square.size += [-width, 0]
	square.draw()
	win.flip()
square.size = [100, 100]