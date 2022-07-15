import pyautogui as pg
import time

print('size of the window: ', pg.size())
fore= pg.getActiveWindow()
print(fore.title)
print(fore.size)
print(fore.left, fore.top, fore.right, fore.bottom)     #Infos of the currently active window

for win in pg.getAllWindows():      #모든 윈도우 정보 가져오기
    print(win)
print('\n\n')
for win in pg.getWindowsWithTitle('제목 없음'):     # title이 '제목없음'인 창들 정보
    print(win)

win=pg.getWindowsWithTitle('제목 없음')[0]      # getWindowsWithTitle 은 list 형식으로 오기 떄문에
print('\n\n', win)

time.sleep(1)
if win.isActive == False:       # when the window is inactive(it is different with 'minimized'.
    win.activate()              # if minimized, omits this step.

time.sleep(1)
if win.isMaximized == False:
    win.maximize()


time.sleep(1)
win.close()

if 'windowCancel.png':
    print('yes, the png is present')
else:
    print('the png isnt present.')
    quit()

time.sleep(1)
pg.moveTo(957, 462, 1)      # when something is not freaking detected, you just need to wait for a few secs, 
pg.click()                  # click anywhere on the screen that does not matter, and run the locateOnScreen().
                # when the error message says that you cannot subscript a "none" to something, 
                # its because there is a value "none" to what you want to subscript to or with.
                # in other words, yuo never got the value you were looking for.
                # I think r=the error here occured because once the alert pops out, it is not 
                # regarded as "activated". so you need to click on it to actually bring it to your screen.
cancelIcon= pg.locateOnScreen('windowCancel.png', grayscale='True', confidence='0.5')
if cancelIcon is None:
    print('cancelIcon is NOT detected!')
    quit()
else:
    print('cancelIcon IS detected!')

cancelCenter= pg.center(cancelIcon)
pg.click(cancelCenter)
pg.moveRel(100, 300, 3)
pg.moveTo(cancelCenter)





