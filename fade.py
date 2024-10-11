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
color_list = [red, green, blue, purple, yellow, cyan, orange]


def fade_out(color, fade_time = .02, number = 50):
    red_ratio = color[0] / number
    red_org = color[0]
    green_ratio = color[1] / number
    green_org = color[1]
    blue_ratio = color[2] / number
    blue_org = color[2]
    for i in range(1, 51):
        r = red_org - i * red_ratio
        g = green_org - i * green_ratio
        b = blue_org - i * blue_ratio
        np.fill((r, g, b))
        np.show()
        time.sleep(fade_time)

def fade_in(color2, fade_time2 = .02, number2 = 50):
    red_ratio = color2[0] / number2
    red_org = color2[0]
    green_ratio = color2[1] / number2
    green_org = color2[1]
    blue_ratio = color2[2] / number2
    blue_org = color2[2]
    for i in range(1, 51):
        r = red_org + i * red_ratio
        g = green_org + i * green_ratio
        b = blue_org + i * blue_ratio
        np.fill((r, g, b))
        np.show()
        time.sleep(fade_time2)

while True:
    nice = random.choice(color_list)
    fade_in(nice)
    fade_out(nice)

