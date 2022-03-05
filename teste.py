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
# x, y = pyautogui.locateCenterOnScreen('./assets/raio.png', confidence=0.95)
x, y = pyautogui.locateCenterOnScreen('./assets/0of10energy.png', confidence=0.95)
# x = (x-27) + round(random.uniform(0,54))
# y = (y-27) + round(random.uniform(0,54))
pyautogui.moveTo(x, y)
pyautogui.screenshot('my_screenshot.png', region=(x, y-20, 80, 50))
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

