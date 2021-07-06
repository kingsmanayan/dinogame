import pyautogui
import webbrowser 
from PIL import Image, ImageGrab
import time
#from numpy import asarray
webbrowser.open("https://chromedino.com/") 
print("game start in  5 second")
def hit(key):
    pyautogui.keyDown(key)
def isCollide(data):
    for i in range(488, 540):
            for j in range(310, 330):
                if data[i, j] < 100:
                    hit('up')
                    return True
    for i in range(485, 551):
        for j in range(200, 300):
            if data[i, j] < 100:
                hit('down')
                return True
                
    return False

def takeScreenshot():
    image = ImageGrab.grab().convert('L')


if __name__== "__main__":
    print("game start 5 s")
    time.sleep(3)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
   
        data = image.load()
        isCollide(data)

