import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write=False, brightness=2)

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
purple = (255, 0, 255)
yellow = (255, 127, 0)
cyan = (0, 255, 255)
orange = (255, 64, 0)
white = (255,255,255)
black = (0,0,0)
dark_blue = (0,0,50)
color_list = [red, green, blue, purple, yellow, cyan, orange]




def scan(col1, col2, bounces = 16):
    pix = 0
    direct = 1
    bounce_count = 0
    while bounce_count < bounces:
        np.fill(col1)
        np[pix] = col2
        np.show()
        pix += direct
        if pix >= (np.n-1) or pix <=0:
            direct *= -1
            bounce_count += 1
        time.sleep(0.02)
    

        
while True:
    scan(black, red)
