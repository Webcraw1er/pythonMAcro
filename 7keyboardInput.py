import pyautogui as pg
import pyperclip as pyp
win= pg.getWindowsWithTitle('제목 없음')[0]
win.activate()
pg.write('hello', 0.2)

pyp.copy('한글 테스트')
pg.hotkey('ctrl', 'v')
