import pyautogui as pg      #alias of pyautogui
a= pg.alert(text='내용입니다', title= '제목입니다', button='OK')    
print(a)                                                        #prints a basic message box

a= pg.confirm(text='내용입니다', title='제목입니다', buttons=['OK', 'Cancel'])
print(a)                                                        #prints a box with 'OK' and 'cancel' buttons

a= pg.prompt(text='내용입니다', title='제목입니다', default='test')
print(a)                                                        #prints a message box with text input box.

                # all values are sent to the server right away.
                # IF you press "cancel" buttons, "None" will be returned.

a= pg.password(text='내용입니다', title='제목입니다', default='ㅁㅁㅁㅁㅁㅁㅁㅁ', mask='*')
print(a)

