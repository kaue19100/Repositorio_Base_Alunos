import pyautogui as pg

from time import sleep 

#pg.mouseInfo()



pg.press('win')
pg.write('chrome')
pg.press('enter')
sleep(2)
pg.write('https://renderz.app/24/squadbuilder/create')
pg.press('enter')
sleep(5)
pg.moveTo(944, 641)
pg.click()
sleep(1)
pg.moveTo(58, 825)
pg.click()
sleep(4)
pg.moveTo(1004, 698)
pg.click()