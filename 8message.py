import pyautogui as pg
pg.countdown(5)             # every one second, print 5 to 1
pg.alert('error!')
con= pg.confirm('continue?', 'ok')
print(con)

pg.mouseInfo()