from math import sin
from random import randrange
from time import sleep
from neopixel import Neopixel

numpix = 144
strip = Neopixel(numpix, 0, 28, "GRB")

red = (255, 0 ,0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
purple = (130, 0 , 255)

colors_rgb = [blue, indigo, violet]
solid_colors = [red, green, blue, indigo, violet, purple]
color_patterns = [[blue, violet, green, purple],
                  [red, violet, blue, purple],
                  [blue, green, purple],
                  [green, purple],
                  [blue, purple]
                  ]

colors = colors_rgb

#strip.brightness(50)

def colorWave(cycle, colorStart, colorEnd, strip):
    timer = 0
    cycle = cycle

    strip.brightness(50)

    step = round(numpix / len(colors))
    current_pixel = 0

    for color1, color2 in zip(colors, colors[1:]):
        strip.set_pixel_line_gradient(current_pixel, current_pixel + step, color1, color2)
        current_pixel += step

        strip.set_pixel_line_gradient(current_pixel, numpix - 1, colorStart, colorEnd)
    while timer < cycle:
        strip.rotate_right(1)
        sleep(0.15)
        strip.show()
        timer = timer + 1

def colorTransition(color, brightness, strip):
    color = color
    
    strip.brightness(brightness)
    for pix in range(numpix):
        strip.set_pixel(pix, color)
        sleep(0.15)
        strip.show()

def colorBreathing(cycle, color, minBrightness, maxBrightness, strip):
    timer = 0
    cycle = cycle
    color = color

    colorTransition(color, 50, strip)
    while timer < cycle:
        strip.brightness((maxBrightness/2)*sin(timer/30.0)+minBrightness)
        strip.fill(color)
        sleep(0.01)
        strip.show()
        timer = timer + 1

def colorWheel(cycle, colors, brightness, strip):
    timer = 0
    cycle = cycle

    strip.brightness(brightness)

    segmentSize = round(numpix/len(colors))
    for segment in range(len(colors)):
        strip.set_pixel_line(segment*segmentSize, ((segment+1)*segmentSize)-1, colors[segment])
    while timer < cycle:
        strip.rotate_right(1)
        sleep(0.15)
        strip.show()
        timer = timer + 1

def colorChase(cycle, color, brightness, strip):
    timer = 0
    cycle = cycle

    strip.brightness(brightness)

    strip.set_pixel_line_gradient(0, numpix-1, color, (0, 0, 0,))
    strip.show()
    while timer < cycle:
        strip.rotate_right(1)
        sleep(.05)
        strip.show()
        timer = timer + 1

def colorRandom(cycle, brightness, strip):
    timer = 0
    cycle = cycle

    strip.brightness(brightness)
    strip.show()
    while timer < cycle:
        strip.set_pixel(randrange(0,numpix-1), solid_colors[randrange(0, len(solid_colors))])
        sleep(0.01)
        strip.show()
        timer = timer + 1

def getSolidColor():
    colorchoice = solid_colors[randrange(0, len(solid_colors))]
    return colorchoice

def getColorPattern():
    color_pattern = color_patterns[randrange(0,len(color_patterns))]
    return color_pattern

def getCycleTime():
    cycletime = randrange(10000,100000)
    return cycletime


actions = [colorTransition, colorWave, colorBreathing, colorWheel, colorChase, colorRandom]

while True:
    # colorTransition(purple, 20, strip)
    # colorWave(40000, violet, blue, strip)
    # colorBreathing(20000, purple, 20, 80, strip)
    # colorTransition(blue, 40, strip)
    # colorWheel(1000, [blue, green, purple], 50, strip)
    # colorTransition(green, 60, strip)
    # colorWheel(30000, [green, purple], 50, strip)
    # colorChase(1000, purple, 50, strip)

    action = randrange(0, len(actions))
    # action = 5

    if action == 0:
        colorTransition(getSolidColor(), randrange(20,50), strip)
    elif action == 1:
        colorWave(getCycleTime(), violet, blue, strip)
    elif action == 2:
        colorBreathing(getCycleTime(), getSolidColor(), 20, 80, strip)
    elif action == 3:
        colorWheel(getCycleTime(), getColorPattern(), 50, strip)
    elif action == 4:
        colorChase(getCycleTime(), getSolidColor(), 50, strip)
    elif action == 5:
        colorRandom(getCycleTime(), 50, strip)