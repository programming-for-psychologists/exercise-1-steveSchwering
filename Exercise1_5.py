import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400], color = "black", units = 'pix')
square = visual.Rect(win, lineColor = "black", fillColor = "blue", size = [100, 100])

seq = ["blue", "red"]
repeats = 3
seq = seq * 3
for color in seq:
	square.fillColor = color
	square.draw()
	win.flip()
	core.wait(1)
	win.flip()
	core.wait(0.5)
core.wait(0.5)