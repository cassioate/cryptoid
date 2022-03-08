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
    durationChoosed = float(os.getenv("DURATION")) + round(random.uniform(0,float(os.getenv("DURATION_RANGE"))), 10)
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
    img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence())
    if img != None:
        if imagem != '0energyInTheGame':
            print('Achei a imagem: ' + imagem)
        return True
    return False

def procurarImagemSemRetornarErroComARegiaoDasCartas(imagem, x, y):
    img = None
    contador = 0
    img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence(), region=(0, y, x, 325))
    if img != None:
        if imagem != '0energyInTheGame':
            print('Achei a imagem: ' + imagem)
        return True
    return False

def adventureClick():
    while procurarImagemSemRetornarErro('adventure'):
        reconnect()
        x, y = pyautogui.locateCenterOnScreen('./assets/adventure.png', confidence=confidence())
        x = (x-140) + round(random.uniform(0,280))
        y = (y-25) + round(random.uniform(0,50))
        pyautogui.click(x, y, duration=durationChoosed())
        time.sleep(5)

def clickStart():
    chooseLevel()
    while procurarImagemSemRetornarErro('start'):
        reconnect()
        x, y = pyautogui.locateCenterOnScreen('./assets/start.png', confidence=confidence())
        x = (x-140) + round(random.uniform(0,280))
        y = (y-25) + round(random.uniform(0,50))
        pyautogui.click(x, y, duration=durationChoosed())
        time.sleep(5)

def chooseLevelFeature(valor):
    valor = str(valor)
    if procurarImagemSemRetornarErro(valor):
        pyautogui.click(procurarLocalizacaoDaImagemPelosEixos(valor), duration=durationChoosed())
        time.sleep(2)

def chooseLevel():
    contador = 12
    while procurarImagemSemRetornarErro('30de30'):
        chooseLevelFeature(contador)
        contador -=1

def chooseCardInTheGame():
    contador = 0
    reconnect()
    x, y = procurarLocalizacaoDaImagemPelosEixos('endTurn')
    if x != None:
        energyInTheGame = procurarImagemSemRetornarErro('0energyInTheGame')
        while not energyInTheGame:
            entroNoElse = False
            reconnect()
            if procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card0', x, y):
                clickInTheCard('cards/card0', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card1', x, y):
                clickInTheCard('cards/card1', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card2', x, y):
                clickInTheCard('cards/card2', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card3', x, y):
                clickInTheCard('cards/card3', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card4', x, y):
                clickInTheCard('cards/card4', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card5', x, y):
                clickInTheCard('cards/card5', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card6', x, y):
                clickInTheCard('cards/card6', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card7', x, y):
                clickInTheCard('cards/card7', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card8', x, y):
                clickInTheCard('cards/card8', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card9', x, y):
                clickInTheCard('cards/card9', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card10', x, y):
                clickInTheCard('cards/card10', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card11', x, y):
                clickInTheCard('cards/card11', x, y)
            else:
                print("NÃO ACHEI MAIS CARTAS")
                entroNoElse = True
                energyInTheGame = True
            if not entroNoElse and not procurarImagemSemRetornarErro('10EnergyIntheGame'): 
                energyInTheGame = procurarImagemSemRetornarErro('0energyInTheGame')
            contador+=1
            if contador > 7:
                entroNoElse = True
                energyInTheGame = True
            ## apenas para evitar que jogue uma carta desnecessaria, devido ao delay na mudança de imagem na tela
            if contador > 4:
                time.sleep(2)
        x = (x-100) + round(random.uniform(0,200))
        y = (y-30) + round(random.uniform(0,60))
        pyautogui.click(x, y, duration=durationChoosed())

def chooseCardInTheGameW1W2():
    contador = 0
    reconnect()
    x, y = procurarLocalizacaoDaImagemPelosEixos('endTurn')
    if x != None:
        energyInTheGame = procurarImagemSemRetornarErro('0energyInTheGame')
        while not energyInTheGame:
            entroNoElse = False
            reconnect()
            if procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card2', x, y):
                clickInTheCard('cards/card2', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card3', x, y):
                clickInTheCard('cards/card3', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card4', x, y):
                clickInTheCard('cards/card4', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card5', x, y):
                clickInTheCard('cards/card5', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card6', x, y):
                clickInTheCard('cards/card6', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card7', x, y):
                clickInTheCard('cards/card7', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card8', x, y):
                clickInTheCard('cards/card8', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card9', x, y):
                clickInTheCard('cards/card9', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card10', x, y):
                clickInTheCard('cards/card10', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card11', x, y):
                clickInTheCard('cards/card11', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card0', x, y):
                clickInTheCard('cards/card0', x, y)
            elif procurarImagemSemRetornarErroComARegiaoDasCartas('cards/card1', x, y):
                clickInTheCard('cards/card1', x, y)
            else:
                print("NÃO ACHEI MAIS CARTAS")
                entroNoElse = True
                energyInTheGame = True
            if not entroNoElse and not procurarImagemSemRetornarErro('10EnergyIntheGame'): 
                energyInTheGame = procurarImagemSemRetornarErro('0energyInTheGame')
            contador+=1
            if contador > 7:
                entroNoElse = True
                energyInTheGame = True
            ## apenas para evitar que jogue uma carta desnecessaria, devido ao delay na mudança de imagem na tela
            if contador > 4:
                time.sleep(2)
        x = (x-100) + round(random.uniform(0,200))
        y = (y-30) + round(random.uniform(0,60))
        pyautogui.click(x, y, duration=durationChoosed())

def chooseCard():
    endOfTheGame = False
    while endOfTheGame == False:
        if procurarImagemSemRetornarErro('w1w2'):
            chooseCardInTheGameW1W2()
        else:
            chooseCardInTheGame()
        endOfTheGame = findEnd()

def clickInTheCard(card, x, y):   
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
    elif procurarImagemSemRetornarErro('start'):
        print("VITORIA OU DERROTA? NUM SABO!")
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
    clickInTheArrowBackButton()
    clickInTheFriendsButton()
    takeEnergy()
    clickInTheArrowBackButton()
    clickIntheQuestButton()
    for i in range(5):
        clickInTheClaimButton()
    clickInTheXRedButton()
    time.sleep(15)

def find0of10energy():
    img = None
    imgRaio = pyautogui.locateCenterOnScreen('./assets/raio.png', confidence=0.95)
    if imgRaio != None:
        x, y = imgRaio
        img = pyautogui.locateCenterOnScreen('./assets/0of10energy.png', confidence=confidence(), region=(x, y-20, 80, 50))
        if img != None:
            return True
        return False

def reconnect():
    if procurarImagemSemRetornarErro('reconnect'):
        x, y = pyautogui.locateCenterOnScreen('./assets/tips.png', confidence=confidence())
        pyautogui.click(x, y, duration=durationChoosed())
        reiniciarAPagina()
        while not procurarImagemSemRetornarErro('adventure'):
            time.sleep(1)
        raise Exception("Encontado botão de reconnect na tela - clickStart")

def start(loop, noNeedEnergy):
    adventureClick()
    loopWhile = True
    while loopWhile:
        reconnect()
        if find0of10energy() and not noNeedEnergy:
            loopWhile = False
        elif procurarImagemSemRetornarErro('360') and find0of10energy():
            loopWhile = False
            loop = False
        else:
            clickStart()
            chooseCard()
    return loop

loop = True
noNeedEnergy = False
while loop:
    try:
        loop = start(loop, noNeedEnergy)
        if not noNeedEnergy:
            recorverEnergy()
            noNeedEnergy = True
    except BaseException as err:
        print("OCORREU UM ERRO!")
        print(err)