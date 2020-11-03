import pyautogui
import time
#Make sure to be on the MHS page
#Press escape to stop the program
pyautogui.alert('This program will open MHS and login lots of lots of times!')
while True:
    pyautogui.click(x=1139, y=445)
    time.sleep(1.5)
    pyautogui.click(x=988, y=562)
    time.sleep(0)
    pyautogui.click(x=846, y=545)
    time.sleep(2)
    pyautogui.click(x=1710, y=134)
    time.sleep(1.5)
def on_press(key):
    if key == keyboard.Key.f12:
        return False
