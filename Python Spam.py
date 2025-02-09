import pyautogui as pg
import time
count=1
while count <= 20:
    time.sleep(0.1)
    pg.write('Hi Bro')
    time.sleep(0.1)
    pg.press('Enter')
    time.sleep(0.1)
    count +=1