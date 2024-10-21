import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write=False, brightness=2)

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 37)
purple = (255, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
orange = (255, 64, 0)
white = (255,255,255)
black = (0,0,0)
color_list = [red, green, blue, purple, yellow, cyan, orange]

def lightning(bg = blue, flash = white):
    yes = random.randint(1,2)
    for i in range(yes):
        no = random.randint(1, 8)
        no = no / 50
        np.fill(flash)
        np.show()
        time.sleep(no)
        np.fill(bg)
        np.show()
        time.sleep(no)
            
while True:
    lightning()
    time.sleep(2)
