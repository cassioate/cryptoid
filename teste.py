import pyautogui
import random
import time
import dotenv
import os
import cv2
from tkinter import *
import datetime

dotenv.load_dotenv()

# print(random.uniform(0,160), 10)
# img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence(), region=(0, y, x, 325))
# x, y = procurarLocalizacaoDaImagemPelosEixos('returnArrow')
# time.sleep(1)
x, y = pyautogui.locateCenterOnScreen('./assets/10EnergyIntheGame.png', confidence=0.95)
# # x = (x-27) + round(random.uniform(0,54))
# # y = (y-27) + round(random.uniform(0,54))
# print(x, y)
pyautogui.moveTo(x, y)

# x+1800, y+280
# x+900, y+235

pyautogui.screenshot('my_screenshot.png', region=(x+900, y+235, 900, 35))
# pyautogui.screenshot('my_screenshot.png', region=(x-25,(newY+54+variacaoDoY), 45,40))
# print(img)
# print(pyautogui.position())
# round(random.uniform(0,3), 10)
contador = 0
# while True:
# img = pyautogui.locateCenterOnScreen('./assets/addFriend.png', confidence=0.95)
# x, y = pyautogui.locateCenterOnScreen('./assets/addFriend.png', confidence=0.95)
# img2 = pyautogui.locateCenterOnScreen('./assets/receiveEnergy.png', confidence=0.95)
# print(img)
# print(img2)
# pyautogui.moveTo(x-372, y+202)
#     try:
        
#         if contador <= 10:
#             print(contador)
#         raise Exception("Erro ao tentar realizar o login")
#     except BaseException as err:
#         contador+=1
        

# x, y = pyautogui.locateCenterOnScreen('./assets/returnArrow.png', confidence=0.95)
# print(x, y)
# x = (x-50) + round(random.uniform(0,100))
# y = (y-35) + round(random.uniform(0,70))
# pyautogui.moveTo(x, y)

# img = pyautogui.locateCenterOnScreen('./assets/2energy.png', confidence=0.95)
# print(img)

