import pyautogui as pg

from time import sleep 

#pg.mouseInfo()

pg.press('win')
pg.write('chrome')
pg.press('enter')
pg.sleep(2)
pg.write('www.youtube.com')
pg.press('enter')
pg.sleep(3)
pg.press(';')
pg.write('welcome to the jungle')
pg.press('enter')
pg.moveTo(603, 692)
pg.sleep(1)
pg.click()
pg.moveTo(1166, 860)
pg.sleep(1)
pg.click()