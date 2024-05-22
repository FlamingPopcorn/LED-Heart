from math import sin
from math import pi
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

# strip.brightness(50)

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
        strip.brightness(((maxBrightness-minBrightness)/2)*sin(timer/25.0)+((minBrightness+maxBrightness)/2))
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

def colorFallSolid(cycle, color, brightness, strip):
    timer = 0
    cycle = cycle

    strip.brightness(brightness)
    num_side_pixels = round(numpix/2)
    while timer < cycle:
        
        for pixel in range(0, num_side_pixels):
            pixel_pair = abs(pixel-(numpix-1))
            if (pixel-timer) % 4 == 0:
                strip.set_pixel(pixel, color)
                strip.set_pixel(pixel_pair, color)
            elif (pixel-timer) % 4 == 1:
                strip.set_pixel(pixel, (.6*color[0], .6*color[1], .6*color[2]))
                strip.set_pixel(pixel_pair, (.6*color[0], .6*color[1], .6*color[2]))
            elif (pixel-timer) % 4 == 2:
                strip.set_pixel(pixel, (.3*color[0], .3*color[1], .3*color[2]))
                strip.set_pixel(pixel_pair, (.3*color[0], .3*color[1], .3*color[2]))
            elif (pixel-timer) % 3 == 3:
                strip.set_pixel(pixel, (0, 0, 0))
                strip.set_pixel(pixel_pair, (0, 0, 0))
        strip.show()
        sleep(.05)
        timer = timer + 1

def colorFallPair(cycle, colorL, colorR, brightness, strip):
    timer = 0
    cycle = cycle

    strip.brightness(brightness)
    num_side_pixels = round(numpix/2)
    while timer < cycle:
        
        for pixel in range(0, num_side_pixels):
            pixel_pair = abs(pixel-(numpix-1))
            if (pixel-timer) % 4 == 0:
                strip.set_pixel(pixel, colorR)
                strip.set_pixel(pixel_pair, colorL)
            elif (pixel-timer) % 4 == 1:
                strip.set_pixel(pixel, (.6*colorR[0], .6*colorR[1], .6*colorR[2]))
                strip.set_pixel(pixel_pair, (.6*colorL[0], .6*colorL[1], .6*colorL[2]))
            elif (pixel-timer) % 4 == 2:
                strip.set_pixel(pixel, (.3*colorR[0], .3*colorR[1], .3*colorR[2]))
                strip.set_pixel(pixel_pair, (.3*colorL[0], .3*colorL[1], .3*colorL[2]))
            elif (pixel-timer) % 3 == 3:
                strip.set_pixel(pixel, (0, 0, 0))
                strip.set_pixel(pixel_pair, (0, 0, 0))
        strip.show()
        sleep(.05)
        timer = timer + 1

def colorFallRainbow(cycle, brightness, strip):
    timer = 0
    cycle = cycle

    strip.brightness(brightness)
    num_side_pixels = round(numpix/2)
    while timer < cycle:
        hue = timer * 128 % 65535

        for pixel in range(0, num_side_pixels-1):
            pixel_pair = abs(pixel-(numpix-1))
            if (pixel-timer) % 4 == 0:
                strip.set_pixel(pixel, strip.colorHSV(hue, 255, 255))
                strip.set_pixel(pixel_pair, strip.colorHSV(hue, 255, 255))
            elif (pixel-timer) % 4 == 1:
                strip.set_pixel(pixel, strip.colorHSV(hue, 255, int(.6*255)))
                strip.set_pixel(pixel_pair, strip.colorHSV(hue, 255, int(.6*255)))
            elif (pixel-timer) % 4 == 2:
                strip.set_pixel(pixel, strip.colorHSV(hue, 255, 255 // 3))
                strip.set_pixel(pixel_pair, strip.colorHSV(hue, 255, 255 // 3))
            elif (pixel-timer) % 4 == 3:
                strip.set_pixel(pixel, (0, 0, 0))
                strip.set_pixel(pixel_pair, (0, 0, 0))
        strip.show()
        sleep(.05)
        timer = timer + 1

def colorFade(cycle, brightness, strip):
    timer = 0
    cycle = cycle

    strip.brightness(brightness)
    while timer < cycle:
        hue = timer * 128 % 65535
        color = strip.colorHSV(hue, 255, 255)
        strip.fill(color)
        strip.show()
        sleep(.025)
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

actions = [colorTransition, colorWave, colorBreathing, colorWheel, colorChase, colorRandom, colorFallSolid, colorFallPair, colorFallRainbow, colorFade]

while True:    
    action = randrange(0, len(actions))
    # action = 2

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
    elif action == 6:
        colorFallSolid(getCycleTime(), getSolidColor(), 50, strip)
    elif action == 7:
        colorFallPair(getCycleTime(), getSolidColor(), getSolidColor(), 50, strip)
    elif action == 8:
        colorFallRainbow(getCycleTime(), 50, strip)
    elif action == 9:
        colorFade(getCycleTime(), 50, strip)