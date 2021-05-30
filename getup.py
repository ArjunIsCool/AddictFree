from PIL import Image
from time import sleep
from keyboard import is_pressed
from threading import Thread
from os import _exit
from ctypes import windll

mins = 0
blockMins = 0
noOfTimes = 0

print("Copyright© ArjunIsCool")
print("Welcome to AddictFree!")


def getMins():
    global mins
    try:
        mins = float(input("How many mins until i block the system? "))
    except:
        print("Bad input, you noob!")
        getMins()

def getBlockMins():
    global blockMins
    try:
        blockMins = float(input("For how many mins should it be blocked? "))
    except:
        print("Bad input, you noob!")
        getBlockMins()

def getnoOfTimes():
    global noOfTimes
    try:
        noOfTimes = int(input("How many times should i repeat this? "))
    except:
        print("Bad input, you noob!")
        getnoOfTimes()
        


def checkForInput():
    while(True):
        if(is_pressed("shift + ctrl + k")):
            _exit(101)
            break
        sleep(0.2)

Thread(target=checkForInput).start()
getMins()
getBlockMins()
getnoOfTimes()
print("All set, go ahead and do your work now!")
print("NOTE: You can always kill the program using the hotkey Ctrl+Shift+K, but use it only during emergency :)")

for i in range(noOfTimes):
    windll.user32.BlockInput(False)

    
    sleep(mins*60)

    img = Image.open("getup.jpg")
    windll.user32.BlockInput(True)
    img.show()
    sleep(blockMins*60)



