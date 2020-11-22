import pyautogui
import os
import time

os.chdir (r'C:\Users\Surface Book\Desktop\Programing\Banner w autogui')

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

snum = input('Enter student number: ')
term = input('Enter term code: ')
route = input('Would you like to route. Leave blank if no: ')
if bool(route): 
	team = input('Enter team numbe (1, 2, 3, 4, 5): ')

program = input('Enter program code: ')

pyautogui.click(pyautogui.locateCenterOnScreen('0 reset.png'))
pyautogui.click(pyautogui.locateCenterOnScreen('Start new batch.png'))
pyautogui.click(pyautogui.locateCenterOnScreen('2 Name click.png'))
pyautogui.typewrite(f'{snum}\n', interval=0.01)

pyautogui.click(pyautogui.locateCenterOnScreen('3 New file.png'))

time.sleep(1)

pyautogui.click(pyautogui.locateCenterOnScreen('4 Chose file.png'))

time.sleep(2)

pyautogui.hotkey('ctrl','f')

pyautogui.typewrite(f'{snum} {term} Deferral\n', interval=0.01)

time.sleep(25)

pyautogui.click(pyautogui.locateCenterOnScreen('6 newdoc.png'))
pyautogui.click(pyautogui.locateCenterOnScreen('7 id line.png'))

pyautogui.typewrite(f'{snum}\t\t\nc\n\t\t\t\t\n', interval=0.18)
time.sleep(0.8)

if bool(route): 
	pyautogui.typewrite(f'{term}\n\t\t\t\t\ni team {team}\n\t\t\t\t\t{comment}', interval=0.18)
else:
	pyautogui.typewrite(f'{term}\n\t\t\t\t\t\t\t\t\t{comment}', interval=0.18)
