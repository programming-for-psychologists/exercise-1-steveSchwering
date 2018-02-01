import time
import sys
from psychopy import visual,event,core

### Original stimuli 
win = visual.Window([400,400], color = "black", units = 'pix')
square = visual.Rect(win, lineColor = "black", fillColor = "blue", size = [100, 100])
text = visual.TextStim(win, text = "Begin", height = 40, color = "white", pos = [0, 100])
text.setAutoDraw(True)
square.draw()
win.flip()
core.wait(.5) #pause for 500 ms (half a second)
win.flip()
core.wait(.5)


### Make the square red
square.fillColor = "red"
text.text = "Part 1"
square.draw()
win.flip()
core.wait(0.5)
win.flip()
core.wait(0.5)

### Appear for 1.5 seconds
text.text = "Part 2"
square.draw()
win.flip()
core.wait(1.5)
win.flip()

### Red square for 1 then blue for 1
text.text = "Part 3"
square.draw()
win.flip()
core.wait(1)
win.flip()
square.fillColor = "blue"
square.draw()
win.flip()
core.wait(1)
win.flip()
core.wait(0.5)

### Make square appear for 1.5 seconds and then flash 3 times for 30 ms
text.text = "Part 4"
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

### Show the following sequence: blue, red, blue, red, blue, red (with each square appearing for 1 s with a 50 ms blank screen in the middle).
text.text = "Part 5"
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

### Show a red square for 1 s then change its orientation by 45-deg
text.text = "Part 6"
square.draw()
win.flip()
core.wait(1)
win.flip()
square.ori += 45
square.draw()
win.flip()
core.wait(0.5)
win.flip()
core.wait(0.5)

### Now make a square rotate continuously, one full revolution (360 degrees) per second
### ### There are 1000 ms in a second. I need the square to increment an amount by the
### ### degrees of a circle divided by the number of refreshes per second. Assuming 60 Hz.
text.text = "Part 7"
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

### Make a rotating square stop rotating when you press the 's' key
text.text = "Part 8"
stopKey = 's'
keyPress = []
while (stopKey not in keyPress):
	square.ori += incr
	square.draw()
	win.flip()
	keyPress = event.getKeys(keyList=[stopKey])
square.ori = 0
core.wait(0.5)

### Make a square stop rotating when you press 's' and then start rotating again when you press 'r'
text.text = "Part 9"
startKey = 'r'
quitKey = 'q'
keyPress = []
while (quitKey not in keyPress):
	while (stopKey not in keyPress):
		square.ori += incr
		square.draw()
		win.flip()
		keyPress = event.getKeys(keyList = [stopKey, quitKey])
		if quitKey in keyPress:
			break
	if quitKey in keyPress:
		break
	keyPress = event.waitKeys(keyList = [startKey, quitKey])
square.ori = 0

### Display a blue square and increase its width (making it a rectangle) by 10 pixels whenever the
### user presses the left-arrow key. Decrease the width by 10 pixels when the user presses the right-arrow key
text.text = "Part 10"
shrinkKey = "right"
growKey = "left"
keyPress = []
while (quitKey not in keyPress):
	keyPress = ["a"]
	keyPress = event.getKeys(keyList = [quitKey, growKey, shrinkKey])
	if shrinkKey in keyPress:
		square.size += [-10, 0]
	elif growKey in keyPress:
		square.size += [10, 0]
	square.draw()
	win.flip()
square.size = [100, 100]

### Make the rectangle decrease/increase its width by 10% of its current width with each keypress instead of 10 pixels
text.text = "Part 11"
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

### Show two rotating squares simultaneously, one left of center rotating clockwise, the other right of center, rotating counterclockwise
text.text = "Part 12"
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

### Other
### ### Time out

### EXIT PROGRAM
sys.exit()