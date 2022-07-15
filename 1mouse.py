"""

"""
import pyautogui
import time
print(pyautogui.size())                     #current size of the window

time.sleep(2)                               # set the time latency
print(pyautogui.position())                 # current position of the cursor

pyautogui.moveTo(950, 450)                  # move the cursor to the position right away
pyautogui.click(button='right')             # right clicks
time.sleep(2)
pyautogui.moveTo(900, 500, 0.3)               # move the cursor  FOR 1 SECOND!
pyautogui.click()                           # left clicks
time.sleep(0.5)
pyautogui.doubleClick()                     # doubleclicks
time.sleep(0.5)
pyautogui.click(clicks=3, interval= 0.3)       # clicks 3 times, with 1 sec of interval.

pyautogui.moveTo(800, 400, 0.3)               # move to position
pyautogui.dragTo(1000, 500, 0.3)              # DRAG to position
time.sleep(1)       
pyautogui.click()                
pyautogui.click(600, 300)                   # click the selected position right away
pyautogui.moveRel(100, 100, 0.3)              # move as the specified pixel from the current position

pyautogui.click()                             # just like "press()" includes "keyDown" and "keyUP",         
pyautogui.mouseDown()                       # "click" contains "mouseDown" and "mouseUp"/
pyautogui.moveRel(-100, -100, 0.4)          # you can use this to break down "dragTo", 
pyautogui.mouseUp()                         # into "mouseDown" -> "moveRel or moveTo" -> "mouseUp".
pyautogui.click()  
pyautogui.scroll(500)                      # scrolls the mouse 500pixels upwards

pyautogui.mouseInfo()                       # will pop up an application that shows the info of your cursor
