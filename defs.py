from PIL import ImageGrab, ImageEnhance, ImageFilter, ImageOps
import pyautogui
import time
import pytesseract
import pyperclip
from datetime import datetime
from id import *
from sites import *

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR"'

# sites


def sreenGrab(x1, y1, x2, y2):
    ''' grab a screenshot of the game - box is the area of the screen to capture '''
    img = ImageGrab.grab((x1, y1, x2, y2)) 
    
    # These image manipulations are required to help tesseract read the data properly
    img = img.convert('L') # greyscale
    img = img.resize((img.size[0]*3, img.size[1]*3), 1)
    img = ImageEnhance.Contrast(img).enhance(12.0) # 5.0 12.0
    img = ImageOps.equalize(img)
    #img = ImageOps.invert(img)
    return img

def goSpin(x1, y1, x2, y2):
    ''' captures the balance and converts it into a Python float '''
    img = sreenGrab(x1, y1, x2, y2)
    img = img.filter(ImageFilter.MaxFilter(1))
    # img.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG') # for debugging
    numStr = pytesseract.image_to_string(img, lang='eng')
    return str(numStr)
    
def numGrab(x1, y1, x2, y2):
    ''' grab a screenshot of the game - box is the area of the screen to capture '''
    img = ImageGrab.grab((x1, y1, x2, y2)) 
    
    # These image manipulations are required to help tesseract read the data properly
    img = img.convert('L') # greyscale
    img = img.resize((img.size[0]*3, img.size[1]*3), 1)
    img = ImageEnhance.Contrast(img).enhance(8.0) # 5.0 12.0
    img = ImageOps.equalize(img)
    #img = ImageOps.invert(img)
    return img

def checkNumbers(x1, y1, x2, y2):
    ''' captures the balance and converts it into a Python float '''
    img = numGrab(x1, y1, x2, y2)
    img = img.filter(ImageFilter.MaxFilter(1))
    # img.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG') # for debugging
    numStr = pytesseract.image_to_string(img, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    return str(numStr)

#for i in range(1000):
#   print(checkNumbers(630, 640, 660, 680))    
    
    
def getPosition(par):
    input("Point the " + par + " then press Enter...")
    return (pyautogui.position())

def click(pos):
    pyautogui.click(pos)
    
def wait(timei):
    time.sleep(timei)

def move2Tab():
    pyautogui.hotkey('ctrl', '2')
    
def move1Tab():
    pyautogui.hotkey('ctrl', '1')
    wait(0.5)
    
def writeSite(a):
    pyautogui.write(a)

def getBalance(balancePos):
        pyautogui.click(balancePos, clicks=2, interval=0.1)
        wait(0.3)
        pyautogui.hotkey('ctrl', 'c')
        wait(0.3)
        
        a = float(pyperclip.paste().replace('.', '').replace(',' , '.'))
        
        wait(0.1)
        return(a)

def saveToTxt(nome_file, i, balance, startBalance, target):
    with open(nome_file, 'a') as file:
        file.write(str(i) + ' ' + str(balance) + '\n')
    file.close()


       

"""
Mouse
pyautogui.click()  # click the mouse
pyautogui.click(x=100, y=200)



Keyboard
pyautogui.write('Hello world!', interval=0.25)
pyautogui.press('enter')  # press the Enter key

"""