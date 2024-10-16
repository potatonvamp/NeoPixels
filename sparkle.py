import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write=False, brightness=1)

white = (255, 255, 255)


def sparkle(bg=(30,0,30), fg=white, delay=.08, spark=3):
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


while True:
    sparkle()
