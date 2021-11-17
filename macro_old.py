from time import sleep
from pyautogui import click, hotkey, position, press
from pyperclip import copy

f = open("fm.txt")
artists = f.read().splitlines()
f.close()

input("Posicione o mouse sobre o campo de texto.")
x1,y1=position()
input("Posicione o mouse sobre o console.")
x2,y2=position()

for artist in artists:
    sleep(1.5)
    click(x1, y1)
    copy(".fmw " + artist)
    hotkey("ctrl", "v")
    press('enter')
    click(x2, y2)
