import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write=False, brightness=2)

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 37)
purple = (255, 0, 255)
yellow = (255, 127, 0)
cyan = (0, 255, 255)
orange = (255, 64, 0)
white = (255,255,255)
black = (0,0,0)
color_list = [red, green, blue, purple, yellow, cyan, orange]
fire_list = [red, yellow, orange]


def sparkle(bg, fg, delay, spark):
    for i in range(spark):
        one = random.randint(0,29)
        two = random.randint(0,29)
        three = random.randint(0,29)
        np.fill(bg)
        np[one] = fg
        np[two] = fg
        np[three] = fg
        np.show()
        time.sleep(delay)


def fire(flicker = 15):
    for i in range(flicker):
        sparkle(orange , red, 0.1, 0.1)
        sparkle(orange, yellow, 0.2, 0.1)
        sparkle(orange, black, 0.02, 0.1)
            
while True:
    fire()
