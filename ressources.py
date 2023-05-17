import pyautogui
import time
from PIL import Image


def checkBle():
    # Define the path to the folder containing the images
    image_folder = 'img/'
    
    # Load the template image to search for

    ble = pyautogui.locateOnScreen(image_folder + 'ble.png', confidence=0.8)
    
    if ble is not None:
        print("Ble found.")
        # If the template image is found, load the collectable image
        pyautogui.moveTo((ble[0]/2),(ble[1]/2))
        pyautogui.click()
        print("Clicked on the ble image.")
        print("Waiting 1 second...")
        time.sleep(2)
        # pyautogui.moveTo(1,1)
        pyautogui.moveRel(20,40)
        pyautogui.click()
        time.sleep(10)
    else:
        print("Ble not found.")

# checkOrge()
def checkOrge():
    # Define the path to the folder containing the images
    image_folder = 'img/'
    
    # Load the template image to search for
    orge = pyautogui.locateOnScreen(image_folder + 'orge.png', confidence=0.3)
    
    if orge is not None:
        print("Orge found.")
        # If the template image is found, load the collectable image
        pyautogui.moveTo((orge[0]/2),(orge[1]/2))
        pyautogui.click()
        print("Clicked on the orge image.")
        print("Waiting 10 seconds...")
        time.sleep(10)
        # pyautogui.moveTo(1,1)
        pyautogui.moveRel(20,40)
        pyautogui.click()
    else:
        print("Orge not found.")

# check Avoine
def checkAvoine():
    # Define the path to the folder containing the images
    image_folder = 'img/'
    
    # Load the template image to search for
    avoine = pyautogui.locateOnScreen(image_folder + 'avoine.png', confidence=0.3)
    
    if avoine is not None:
        print("Avoine found.")
        # If the template image is found, load the collectable image
        pyautogui.moveTo((avoine[0]/2),(avoine[1]/2))
        pyautogui.click()
        print("Clicked on the avoine image.")
        print("Waiting 10 seconds...")
        time.sleep(10)
        # pyautogui.moveTo(1,1)
        pyautogui.moveRel(20,40)
        pyautogui.click()
    else:
        print("Avoine not found.")

# check Houblon
def checkHoublon():
    # Define the path to the folder containing the images
    image_folder = 'img/'
    
    # Load the template image to search for
    houblon = pyautogui.locateOnScreen(image_folder + 'houblon.png', confidence=0.3)
    
    if houblon is not None:
        print("Houblon found.")
        # If the template image is found, load the collectable image
        pyautogui.moveTo((houblon[0]/2),(houblon[1]/2))
        pyautogui.click()
        print("Clicked on the houblon image.")
        print("Waiting 10 seconds...")
        time.sleep(10)
        # pyautogui.moveTo(1,1)
        pyautogui.moveRel(20,40)
        pyautogui.click()
    else:
        print("Houblon not found.")

# check Lin
def checkLin():
    # Define the path to the folder containing the images
    image_folder = 'img/'
    
    # Load the template image to search for
    lin = pyautogui.locateOnScreen(image_folder + 'lin.png', confidence=0.3)
    
    if lin is not None:
        print("Lin found.")
        # If the template image is found, load the collectable image
        pyautogui.moveTo((lin[0]/2),(lin[1]/2))
        pyautogui.click()
        print("Clicked on the lin image.")
        print("Waiting 10 seconds...")
        time.sleep(10)
        # pyautogui.moveTo(1,1)
        pyautogui.moveRel(20,40)
        pyautogui.click()
    else:
        print("Lin not found.")

# check Seigle
def checkSeigle():
    # Define the path to the folder containing the images
    image_folder = 'img/'
    
    # Load the template image to search for
    seigle = pyautogui.locateOnScreen(image_folder + 'seigle.png', confidence=0.3)
    
    if seigle is not None:
        print("Seigle found.")
        # If the template image is found, load the collectable image
        pyautogui.moveTo((seigle[0]/2),(seigle[1]/2))
        pyautogui.click()
        print("Clicked on the seigle image.")
        print("Waiting 10 seconds...")
        time.sleep(10)
        # pyautogui.moveTo(1,1)
        pyautogui.moveRel(20,40)
        pyautogui.click()
    else:
        print("Seigle not found.")

def checkRessources():
    if checkBle():
        sleep(1)
        return
    if checkOrge():
        sleep(10)
        return
    # if checkAvoine():
    #     sleep(10)
    #     return
    # if checkHoublon():
    #     sleep(10)
    #     return
    # if checkLin():
    #     sleep(10)
    #     return
    # if checkSeigle():
    #     sleep(10)
    #     return
    