import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400], color = "black", units = 'pix')
square = visual.Rect(win, lineColor = "black", fillColor = "blue", size = [100, 100])

square.ori = 0
Hz = 60
degrees = 360
incr = degrees / Hz
while(square.ori < degrees):
	square.ori += incr
	square.draw()
	win.flip()
square.ori = 0
core.wait(0.5)