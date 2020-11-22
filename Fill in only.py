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

comment = input('Enter comment line: ')

pyautogui.click(pyautogui.locateCenterOnScreen('6 newdoc.png'))
pyautogui.click(pyautogui.locateCenterOnScreen('7 id line.png'))

pyautogui.typewrite(f'{snum}\t\t\nc \n\t\t\t\t\n', interval=0.2)
time.sleep(0.8)

if bool(route): 
	pyautogui.typewrite(f'{term}\n\t\t\t\t\ni team {team} \n\t\t\t\t\t{comment}', interval=0.1)

else:
	pyautogui.typewrite(f'{term}   \n\t\t\t\t\t\t\t\t\t{comment}', interval=0.1)
