import time
import busio
import board
import adafruit_aw9523
import neopixel
import random

i2c = busio.I2C(board.SCL, board.SDA)
aw_board = adafruit_aw9523.AW9523(i2c)
print("Found AW9523")

# Set all pins to outputs and LED (const current) mode
aw_board.LED_modes = 0xFFFF
aw_board.directions = 0xFFFF

# control the on-board neopixel
# boardPixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

# boardPixel.brightness = 0.02

pixels = neopixel.NeoPixel(board.A0, 4)
# pixels.fill((234,111,222))
# stepper = [1, 1, 1, 1]
# r = [10, 10, 10, 10]

noods_brightness = 50
noods_io = 1

dir = 1
noodDir = 1

bright_pixel = 0
pixel_dance_frequency = 10
pixel_dance_count = 0

# backlights
backlight_brightness = 255
backlight_io = 0


while True:
    # for i in range(4):
    #     r[i] = r[i] + stepper[i]
        
    #     if stepper[i] < 0 and r[i] <= 1 :
    #         # direction: down - got to minimum
    #         print("hit min for i")
    #         print(i)
    #         r[i] = 1
    #         stepper[i] = random.randint(1,4)
    #     elif stepper[i] > 0 and r[i] >= 255 :
    #         print("hit max for i")
    #         print(i)
    #         r[i] = 255
    #         stepper[i] = random.randint(1,4) * -1
    #     pixels[i] = (r[i], 0, 0)
    # print(pixels)

    # Neopixel Control
    pixels[0] = (50, 0, 0)
    pixels[1] = (50, 0, 0)
    pixels[2] = (50, 0, 0)
    pixels[3] = (50, 0, 0)

    pixels[bright_pixel] = (255, 0, 0)

    pixel_dance_count = pixel_dance_count + 1
    if pixel_dance_count > pixel_dance_frequency:
        bright_pixel = bright_pixel + 1
        if bright_pixel > 3:
            bright_pixel = 0
        pixel_dance_count = 0

    pixels.show()

    # noods control
    aw_board.set_constant_current(noods_io, noods_brightness)
    # adjust noods power for next time
    noods_brightness = (noods_brightness + noodDir)
    # max for noods is 255
    if (noods_brightness > 128):
        noodDir = -1
    elif (noods_brightness < 10):
        noodDir = 1

    # backlights control
    aw_board.set_constant_current(backlight_io, backlight_brightness)

    time.sleep(.01)
    
    # color = (random.randint(0, 255), random.randint(0, 50), random.randint(0, 50))
    # # boardPixel.fill(color)
    # pixels.fill(color)
    # time.sleep(2)


backlights = 0
noods_brightness = 0
dir = 1
noodDir = 1
while True:
    aw_board.set_constant_current(0, backlights)
    aw_board.set_constant_current(1, noods_brightness)
    # n increments to increase the current from 0 to 255, then wraps around
    backlights = (backlights + dir)
    noods_brightness = (noods_brightness + noodDir)
    # max 254 here (so n only goes to 255)
    if (backlights > 254):
        dir = -1
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        boardPixel.fill(color)
        
        print(color)
        print("hit max")
    elif (backlights < 1):
        dir = 1
        print("hit min")
    
    if (noods_brightness > 128):
        noodDir = -1
    elif (noods_brightness < 1):
        noodDir = 1
        
    
    
    time.sleep(0.005)

