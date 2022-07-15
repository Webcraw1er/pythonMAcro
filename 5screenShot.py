import pyautogui as pg
img= pg.screenshot()        
img.save('full.png')                # line 2, 3 takes a shot and then saves it.
img2= pg.screenshot('full2.png')    # line 4 just saves the shot right away.
img3= pg.screenshot('region.png', region=(100, 100, 600, 600))      # saves the specified region

