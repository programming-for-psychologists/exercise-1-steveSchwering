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
while (stopKey not in keyPress):
	square.ori += incr
	square.draw()
	win.flip()
	keyPress = event.getKeys(keyList=[stopKey])
square.ori = 0
core.wait(0.5)