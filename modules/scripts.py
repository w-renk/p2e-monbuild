import os

def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ResizeWindow(width=120, height=64):
    os.system('mode con: cols={w} lines={h}'.format(w = width, h = height))