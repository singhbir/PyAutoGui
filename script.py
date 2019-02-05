# Importing the required Libraries
import pyautogui,time
import webbrowser
import pyfiglet

# For the Figlet(cool stuff)
result = pyfiglet.figlet_format("singhbir")

# To open up a browser
webbrowser.open("https://www.google.com/")

# This will stop the prrogram execution for 5 seconds
time.sleep(5)

#All the pyautogui commands will go from here
pyautogui.hotkey("ctrl","n")
time.sleep(1)
pyautogui.typewrite("https://hack.chat/?singhbir")
pyautogui.press("enter")
time.sleep(3)
pyautogui.typewrite("singhbir",interval=0.1)
pyautogui.press("enter")
pyautogui.typewrite("Hello There",interval=0.1)
pyautogui.press("enter")
pyautogui.typewrite("Don't worry, i have just taken a little control over your system",interval=0.1)
pyautogui.press("enter")
pyautogui.typewrite("SIT BACK AND RELAX",interval=0.1)
pyautogui.press("enter")
pyautogui.typewrite("P.S. Hacked By singhbir!",interval=0.1)
pyautogui.press("enter")
pyautogui.typewrite(result)
pyautogui.press("enter")
