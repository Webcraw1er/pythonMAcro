import pyautogui as pg
import time

if 'button5.png':   # check if button5.png is present
    print("yes")
if 'topright.png':   # check if button5.png is present
    print("yes")
if 'calIcon.png':
    print('yes')

calIconLocation= pg.locateOnScreen('calIcon.png', grayscale='false', confidence='0.8')
if calIconLocation:
    print("calIcon found!")
    calIconCenter= pg.center(calIconLocation)       # center(boxPosition) returns the center position of the box
else:
    print("calIcon not found!")
pg.click(calIconCenter)

time.sleep(2)
button5Location= pg.locateOnScreen('button5.png', grayscale='true', confidence='.8')
time.sleep(1)
toprightLocation= pg.locateOnScreen('topright.png', grayscale='true', confidence='.5')
print("position of cursor: ", pg.position())
print("button5Location: ", button5Location, "center: ", pg.center(button5Location))
print("toprightLocation: ", toprightLocation)



"""
1. first check if the original image sample is present in your storage.

2. grayscale will make your shade your targets; will decrease confidence but easier and faster to find something.

3. confidence need another pip to be installed, but makes the program much more generous to spot something.
    the original scale is 1, and the lesser it gets, the precision will decrease, thus more eager to make a mistake
    but at the same time more likely to find something.


"""