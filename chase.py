import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write=False, brightness=1)

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

def chase():
    count = 0
    for i in range(np.n):
        np.fill(orange)
        for i in range(np.n):
            if (i + count) % 3 == 0:
                np[i] = (black)
        time.sleep(0.2)
        np.show()
        count = (count + i) % 3
        
while True:
    chase()
