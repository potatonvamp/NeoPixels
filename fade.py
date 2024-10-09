import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write=False, brightness=0.3)


def fade_out(color):
    red_ratio = color[0] / 50
    red_org = color[0]
    for i in range(1, 51):
        red = red_org - i * red_ratio
        np.fill((red, 0, 0))
        np.show()
        time.sleep(0.03)

def fade_in(color2):
    red_ratio = color2[0] / 50
    red_org = color2[0]
    for i in range(1, 51):
        red = red_org + i * red_ratio
        np.fill((red, 0, 0))
        np.show()
        time.sleep(0.03)

while True:
    fade_out((255,0,0))
    fade_in((255,0,0))

