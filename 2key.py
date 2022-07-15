import pyautogui
import pyperclip

print(pyautogui.position())
pyautogui.moveTo(1354, 563, 0.5)

pyautogui.write("\nhello, world")                 # writes the following string.
pyautogui.write("\nmy name is ", 0.1)     # write the following string for 0.1 second INTERVAL for each words
pyperclip.copy("김진혁\n\n")                    #pyperclip lets you use KOrean(via copy and paste of the clipboard.)                   
pyautogui.hotkey('ctrl', 'v')               #in order to use "ctrl" or "shifts", you apparently need to use 
                                            # keyDown() and keyUp() everytime. hotkey makes this easier.


pyautogui.press('ctrl')                     # press means literally "one press". includes both keyDown and keyUp.
pyautogui.keyDown('ctrl')                  # presses the key
pyautogui.press('v')                        # presses then releases.
pyautogui.keyUp('ctrl')                    # releases the key

pyautogui.keyDown('shift')
pyautogui.write("\n\nprint all these in upper case", 0.1)
pyautogui.keyUp('shift')

pyautogui.press(['left', 'left', 'right']) # press the left arrow keys three times
pyautogui.press('left', presses=3)          # presses the left arrow three times
pyautogui.press('enter', presses=3, interval= 0.1)  # press enter three times with 0.1 sec of interval.









"""
1. you can't press shifts and Ctrls with a write() function.
    to press these you need a press() function.


2. lists of all keys in the keyboard

'\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright'
"""