import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400], color = "black", units = 'pix')
square = visual.Rect(win, lineColor = "black", fillColor = "blue", size = [100, 100])

square.draw()
win.flip()
core.wait(1.5)
win.flip()
for i in range(3):
	square.draw()
	win.flip()
	core.wait(0.3)
	win.flip()
core.wait(0.5)