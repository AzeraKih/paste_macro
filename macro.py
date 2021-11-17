from time import sleep
from pyautogui import click, hotkey, position, press
from pyperclip import copy

sleep_time=1.3
prefix=""

f = open("fm.txt", encoding="utf-8")
artists = f.read().splitlines()
f.close()

input("Posicione o mouse sobre o campo de texto.")
x1,y1=position()
input("Posicione o mouse sobre o console.")
x2,y2=position()

for artist in artists:
    sleep(sleep_time)
    click(x1, y1)
    copy(prefix + "" + artist)
    hotkey("ctrl", "v")
    press('enter')
    click(x2, y2)
    
