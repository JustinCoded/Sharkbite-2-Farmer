from time import sleep
import keyboard
from random import randint
import pyautogui
import time
import platform

print("Create by: Me\n")
print("Click the Roblox Game Window & Press the 'F1' Key!\n")
print("Ctrl-C to exit")

localtime = time.asctime(time.localtime(time.time()))

print(platform.system)

keyboard.wait('f1')

def detectMode():
    # detect lobby or game mode 
    if (isAFKDisplayed()):
        print("AFK Handled")     
    elif (isInGame()):
        if (isLobby()):
            print("Detected Lobby Mode") 
        else:
            if (isShark()):
    #            sharkMovement()
                print("Detected Shark Mode")
            elif (isDriving()):
                print("Detected Driving Mode") 
    #            hunterMovement()
            elif (isBoatPlayerSelection()):
                sleep(20)

    elif (isGameEntry()):
        print("Detected Game Entry")
    elif (isPrizeWindow()):
        print("Detected Prize Windw")
    
    else: 
        print("Unknown Mode") 
        # pyautogui.screenshot(str(time.time()) + '_unknown_mode.png')
    
def mainLoop():
    detectMode()

def sharkMovement():
    shark_movement = randint(1,6)
    if shark_movement == 1:
        keyboard.press('a')
        print("       Player moved 'Left' as the shark.")
        sleep(randint(2,10))
        keyboard.release('a')

    if shark_movement == 2:
        keyboard.press('w')
        print("       Player moved 'Forward' as the shark.")
        sleep(randint(2,10))
        keyboard.release('w')

    if shark_movement == 3:
        keyboard.press('s')
        print("       Player moved 'Backward' as the shark.")
        sleep(randint(2,10))
        keyboard.release('s')

    if shark_movement == 4:
        keyboard.press('d')
        print("       Player moved 'Right' as the shark.")
        sleep(randint(2,10))
        keyboard.release('d')
    
    if shark_movement == 5:
        print("       Player Used The 'Speed Special' as the shark.")
        sleep(randint(1,4))
        keyboard.press_and_release('Space')

def hunterMovement():
    hunter_movement = randint(1,6)
    if hunter_movement == 1:
        keyboard.press('a')
        print("       Player moved 'Left' as the hunter.")
        sleep(randint(2,10))
        keyboard.release('a')

    if hunter_movement == 2:
        keyboard.press('w')
        print("       Player moved 'Forward' as the hunter.")
        sleep(randint(2,10))
        keyboard.release('w')

    if hunter_movement == 3:
        keyboard.press('s')
        print("       Player moved 'Backward' as the hunter.")
        sleep(randint(2,10))
        keyboard.release('s')

    if hunter_movement == 4:
        keyboard.press('d')
        print("       Player moved 'Right' as the hunter.")
        sleep(randint(2,10))
        keyboard.release('d')

def isShark() -> bool:
    # Detect Shark by Special
    goButton = pyautogui.locateOnScreen('samples/shark_accel.png', confidence=0.55)
    if (goButton != None):
        return True
    else:
        return False 

def isDriving() -> bool:
    # Detect Shark by Special
    speedo = pyautogui.locateOnScreen('samples/speedo.png', confidence=0.25)
    if (speedo != None):
        return True
    else:
        return False 

def isAFKDisplayed() -> bool:
    afkBox = pyautogui.locateOnScreen('samples/afk_box.png', confidence=0.55)
    if (afkBox != None):
        afk_yesButtonCenter = pyautogui.center(afkBox)
        pyautogui.click(x= (afk_yesButtonCenter.x /2)+20, y= (afk_yesButtonCenter.y /2)+20)
    else:
        return False 

def isLobby() -> bool:
    spectateButton = pyautogui.locateOnScreen('samples/spectate.png', confidence=0.55)
    if (spectateButton != None):
        screenSizeX, screenSizeY = pyautogui.size()
        pyautogui.moveTo(screenSizeX / 2, screenSizeY / 2)
        return True
    else:
        return False 

def isGameEntry() -> bool: 
    playButton = pyautogui.locateOnScreen('samples/play.png', confidence=0.55)
    if (playButton != None):
        playButtonCenter = pyautogui.center(playButton)
        print("Center of Play at: " + str(playButtonCenter))
        pyautogui.click(x=playButtonCenter.x / 2, y=playButtonCenter.y / 2)
        return True
    else:
        return False 

def isPrizeWindow() -> bool: 
    prizeWindow = pyautogui.locateOnScreen('samples/prize.png', confidence=0.55)
    if (prizeWindow != None):
        closeButton = prizeWindow = pyautogui.locateOnScreen('samples/close_button.png', confidence=0.55)
        closeButtonCenter = pyautogui.center(closeButton)
        pyautogui.click(x=closeButtonCenter.x / 2, y=closeButtonCenter.y / 2)
        return True
    else:
        return False 

def isInGame() -> bool:
    inGameIcons = pyautogui.locateOnScreen('samples/in_game.png', confidence=0.55)
    if (inGameIcons != None):
        return True
    else:
        return False 

#def isSurvivor(): 

def isBoatPlayerSelection(): 
    otherPlayersText = pyautogui.locateOnScreen('samples/boat_player_selection.png', confidence=0.55)
    if (otherPlayersText != None):
        return True
    else:
        return False 

print("Detecting Mode")
while True: 
    try:
        mainLoop()
        time.sleep(3)
    except KeyboardInterrupt:
        break

exit()