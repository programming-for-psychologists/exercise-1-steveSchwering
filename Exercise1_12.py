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
square2 = visual.Rect(win, lineColor = "black", fillColor = "orange", size = [100, 100], pos = [100, 0])
square3 = visual.Rect(win, lineColor = "black", fillColor = "green", size = [100, 100], pos = [-100, 0])
while quitKey not in keyPress:
	keyPress = event.getKeys(keyList = [quitKey])
	square2.ori += incr
	square3.ori -= incr
	square2.draw()
	square3.draw()
	win.flip()