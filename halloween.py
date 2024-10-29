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
fire_list = [red, yellow, orange]
halloween_list = [orange, purple, green]


def sparkle(bg, fg, delay, spark):
    """
    
    
    Args:
        bg(tuple): the color used in the background of the NeoPixels
        fg(tuple): the color that blinks around in the NeoPixels
        delay(float): the length the function sleeps for.
        Spark(int): the length of time it wil sparkle for.
    
    Return: none
    """
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
    """
    
    Args:
    
    Return: none
    """
    for i in range(flicker):
        sparkle(orange , purple, 0.1, 0.1)
        sparkle(orange, green, 0.2, 0.1)
        sparkle(orange, black, 0.02, 0.1)

def lightning(bg, flash):
    """
    
    Args:
    
    Return: none
    """
    yes = random.randint(1,2)
    for i in range(yes):
        no = random.randint(1, 3)
        no = no / 50
        np.fill(flash)
        np.show()
        time.sleep(no)
        np.fill(bg)
        np.show()
        time.sleep(no)
        
def fade_out(color, fade_time, number = 50):
    """
    
    Args:
    
    Return: none
    """
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

def fade_in(color2, fade_time2, number2 = 50):
    """
    
    Args:
    
    Return: none
    """
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
        
def chase(col1, col2):
    """
    
    Args:
    
    Return: none
    """
    count = 0
    for i in range(np.n):
        np.fill(col1)
        for i in range(np.n):
            if (i + count) % 3 == 0:
                np[i] = (col2)
        time.sleep(0.2)
        np.show()
        count = (count + i) % 3
        
def chase2(col1, col2):
    """
    
    Args:
    
    Return: none
    """
    count = 0
    for i in range(np.n):
        np.fill(col1)
        for i in range(np.n):
            if (i - count) % 3 == 0:
                np[i] = (col2)
        time.sleep(0.2)
        np.show()
        count = (count + i) % 3
            
while True:
    nice = random.choice(halloween_list)
    fade_in(purple, .02)
    chase(orange, black)
    chase2(purple, black)
    fade_out(purple, .02)
    fade_in(green, .02)
    for i in range(3):
        lightning(purple, red)
    sparkle(purple, red, .2, 5)
    fire()
    fade_out(orange, .02)
    for i in range(3):
        lightning(black, red)
    fade_in(red, .02)
    sparkle(red, black, .2, 10)
    for i in range(5):
        lightning(red, white)
    fade_out(red, .02)
