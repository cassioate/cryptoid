import pyautogui
import random
import time
import dotenv
import os
import datetime

dotenv.load_dotenv()

def confidence():
    confidence = os.getenv("CONFIDENCE")
    return confidence

def durationChoosed():
    durationChoosed = float(os.getenv("DURATION")) + round(random.uniform(0,1.5), 10)
    return durationChoosed

def reiniciarAPagina():
    pyautogui.keyDown("ctrl")
    pyautogui.press("f5")
    pyautogui.keyUp("ctrl")
    time.sleep(5)

def procurarLocalizacaoDaImagemPelosEixos(imagem):
    contador = 0
    while contador < 35:
        if procurarImagemSemRetornarErro(imagem):
            try:
                x, y = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence())
                if x != None:
                    if imagem != 'endTurn' and imagem != 'receiveEnergy':
                        print('Clicando em: ' + str(x)+ ', ' + str(y))
                    return x, y
                else:
                    print('Erro na func procurarLocalizacaoDaImagemPelosEixos')
            except:
                print("ERRO - FUNÇÃO: procurarLocalizacaoDaImagemPelosEixos - Nao achei a imagem: "+imagem+' - '+ str(contador))         
        else:
             contador += 1
    return None, None

def procurarImagemSemRetornarErro(imagem):
    img = None
    contador = 0
    # if (imagem == "metamaskNotification"):
    #     time.sleep(10)
    while img == None:
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence())
        if img != None:
            if imagem != '0energyInTheGame':
                print('Achei a imagem: ' + imagem)
            return True
        contador += 1
        if contador >= 5:
            img = True
    return False

def procurarImagemSemRetornarErroComARegiaoDasCartas(imagem, x, y):
    img = None
    contador = 0
    while img == None:
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence(), region=(0, y, x, 325))
        if img != None:
            if imagem != '0energyInTheGame':
                print('Achei a imagem: ' + imagem)
            return True
        contador += 1
        if contador >= 5:
            img = True
    return False

def adventureClick():
    if procurarImagemSemRetornarErro('adventure'):
        x, y = pyautogui.locateCenterOnScreen('./assets/adventure.png', confidence=confidence())
        x = (x-140) + round(random.uniform(0,280))
        y = (y-25) + round(random.uniform(0,50))
        pyautogui.click(x, y, duration=durationChoosed())

def clickStart():
    if procurarImagemSemRetornarErro('start'):
        x, y = pyautogui.locateCenterOnScreen('./assets/start.png', confidence=confidence())
        x = (x-140) + round(random.uniform(0,280))
        y = (y-25) + round(random.uniform(0,50))
        pyautogui.click(x, y, duration=durationChoosed())

def chooseCard():
    endOfTheGame = False
    while endOfTheGame == False:
        if not procurarImagemSemRetornarErro('0energyInTheGame'):
            if procurarImagemSemRetornarErro('endTurn'):
                x, y = procurarLocalizacaoDaImagemPelosEixos('endTurn')
                energyInTheGame = procurarImagemSemRetornarErro('0energyInTheGame')
                contador = 0
                while energyInTheGame == False:
                    energy = 2
                    if procurarImagemSemRetornarErroComARegiaoDasCartas('0energy', x, y):
                        clickInTheCard('0energy', 0, x, y)
                    elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card1', x, y):
                        clickInTheCard('cards/card1', energy, x, y)
                    elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card2', x, y):
                        clickInTheCard('cards/card2', energy, x, y)
                    elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card3', x, y):
                        clickInTheCard('cards/card3', energy, x, y)
                    elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card4', x, y):
                        clickInTheCard('cards/card4', energy, x, y)
                    elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card5', x, y):
                        clickInTheCard('cards/card5', energy, x, y)
                    elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card6', x, y):
                        clickInTheCard('cards/card6', energy, x, y)
                    elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card7', x, y):
                        clickInTheCard('cards/card7', energy, x, y)
                    elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card8', x, y):
                        clickInTheCard('cards/card8', energy, x, y)
                    elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card9', x, y):
                        clickInTheCard('cards/card9', energy, x, y)
                    elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card10', x, y):
                        clickInTheCard('cards/card10', energy, x, y)
                    elif procurarImagemSemRetornarErroComARegiaoDasCartas('2energy', x, y):
                        clickInTheCard('2energy', energy, x, y)
                    elif contador >= 10:
                        energyInTheGame = True
                    contador+=1
                    energyInTheGame = procurarImagemSemRetornarErro('0energyInTheGame')
                x = (x-100) + round(random.uniform(0,200))
                y = (y-30) + round(random.uniform(0,60))
                pyautogui.click(x, y, duration=durationChoosed())

        endOfTheGame = findEnd()

def clickInTheCard(card, energy, x, y):   
    if card == '2energy' or card == '0energy':
        xEnergy, yEnergy = pyautogui.locateCenterOnScreen('./assets/'+card+'.png', confidence=confidence(), region=(0, y, x, 325))
        xEnergy = xEnergy + round(random.uniform(0,110))
        yEnergy = yEnergy + round(random.uniform(0,160))
        pyautogui.click(xEnergy, yEnergy, duration=durationChoosed())
    else:
        xEnergy, yEnergy = pyautogui.locateCenterOnScreen('./assets/'+card+'.png', confidence=confidence(), region=(0, y, x, 325))
        xEnergy = (xEnergy-52) + round(random.uniform(0,104))
        yEnergy = (yEnergy-80) + round(random.uniform(0,160))
        pyautogui.click(xEnergy, yEnergy, duration=durationChoosed())

def findEnd():
    if procurarImagemSemRetornarErro('victory'):
        vitoria = True
        while vitoria:
            time.sleep(1)
            x, y = procurarLocalizacaoDaImagemPelosEixos('victory')
            pyautogui.click(x, y, duration=durationChoosed())
            if x != None:
                vitoria = False
        print("VITORIA!")
        return True
    elif procurarImagemSemRetornarErro('defeat'):
        time.sleep(1)
        x, y = procurarLocalizacaoDaImagemPelosEixos('defeat')
        pyautogui.click(x, y, duration=durationChoosed())
        print("DERROTA!")
        return True
    else:
        return False

## PARTE DE RECUPERAR ENERGIA ##

def clickInTheArrowBackButton():
    x, y = pyautogui.locateCenterOnScreen('./assets/returnArrow.png', confidence=0.95)
    x = (x-50) + round(random.uniform(0,100))
    y = (y-35) + round(random.uniform(0,70))
    pyautogui.click(x, y, duration=durationChoosed())

def clickIntheQuestButton():
    time.sleep(2)
    if procurarImagemSemRetornarErro('quests'):
        x, y = procurarLocalizacaoDaImagemPelosEixos('quests')
        x = (x-32) + round(random.uniform(0,64))
        y = (y-20) + round(random.uniform(0,40))
        pyautogui.click(x, y, duration=durationChoosed())

def clickInTheClaimButton():
    time.sleep(5)
    if procurarImagemSemRetornarErro('claim'):
        x, y = procurarLocalizacaoDaImagemPelosEixos('claim')
        x = (x-55) + round(random.uniform(0,110))
        y = (y-20) + round(random.uniform(0,40))
        pyautogui.click(x, y, duration=durationChoosed())

def clickInTheXRedButton():
    time.sleep(2)
    if procurarImagemSemRetornarErro('xRed'):
        x, y = procurarLocalizacaoDaImagemPelosEixos('xRed')
        x = (x-27) + round(random.uniform(0,54))
        y = (y-27) + round(random.uniform(0,54))
        pyautogui.click(x, y, duration=durationChoosed())
    
def checkEnergy():
    if procurarImagemSemRetornarErro('0of10energy'):
        clickInTheArrowBackButton()

def clickInTheFriendsButton():
    if procurarImagemSemRetornarErro('friends'):
        x, y = procurarLocalizacaoDaImagemPelosEixos('friends')
        x = x + round(random.uniform(0,50))
        y = (y-50) + round(random.uniform(0,100))
        pyautogui.click(x, y, duration=durationChoosed())

def takeEnergy():
    clickInTheReceiveEnergyAndSendEnergy()
    dragInTheMenu1x()
    clickInTheReceiveEnergyAndSendEnergy()

def clickInTheReceiveEnergyAndSendEnergy():
    for i in range(4):
        if procurarImagemSemRetornarErro('receiveEnergy'):
            x, y = procurarLocalizacaoDaImagemPelosEixos('receiveEnergy')
            x = (x-21) + round(random.uniform(0,42))
            y = (y-21) + round(random.uniform(0,42))
            pyautogui.click(x, y, duration=durationChoosed())
            pyautogui.click(x+85, y, duration=durationChoosed())

def dragInTheMenu1x():
    x, y = procurarLocalizacaoDaImagemPelosEixos("friendsToDrag")
    pyautogui.moveTo(x, y+800)
    pyautogui.mouseDown(button='left')
    #BEM MELHOR usar moveTo no lugar de dragTO
    pyautogui.moveTo(x, y+20, duration=2)
    # pyautogui.dragTo(x, y+40, duration = 3)
    time.sleep(2)
    pyautogui.mouseUp(button='left')
    time.sleep(2)

def recorverEnergy():
    checkEnergy()
    clickInTheFriendsButton()
    takeEnergy()
    clickInTheArrowBackButton()
    clickIntheQuestButton()
    for i in range(4):
        clickInTheClaimButton()
    clickInTheXRedButton()

def start(loop, contador):
    adventureClick()
    try:
        while contador <= 10:
            clickStart()
            chooseCard()     
            contador+=1
            # if procurarImagemSemRetornarErro('360'):
            #     contador = 10
            #     loop = False
        recorverEnergy()
        # if not procurarImagemSemRetornarErro('360'):
        #     recorverEnergy()
        return loop, contador
    except BaseException as err:
        return loop, contador

contador = 0
loop = True
while loop:
    try:
        loop, contador = start(loop, contador)
        if contador < 10:
            raise Exception("Erro antes de realizar 10 partidas")
        else:
            contador = 0
    except BaseException as err:
        print("OCORREU UM ERRO!")
