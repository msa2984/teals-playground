import time
import board
import touchio
import neopixel

# There are 7 capacitive touch sensors on the board.
touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)
touch_A3 = touchio.TouchIn(board.A3)
touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)
touch_A6 = touchio.TouchIn(board.A6)
touch_TX = touchio.TouchIn(board.TX)

# Pixels is an array of ten NeoPixels on the board.
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=False)

# Constants for the color(s) of NeoPixels
PIXEL_OFF = (0,0,0)
PIXEL_PURPLE = (180, 0, 255)

# While the program is running,
# If a particular capacitive touch sensor
# is touched, light up a corresponding
# NeoPixel. Otherwise, the NeoPixel should
# remain off.
while True:
    if touch_A1.value:
        pixels[0] = PIXEL_PURPLE
    else:
        pixels[0] = PIXEL_OFF
    if touch_A2.value:
        pixels[1] = PIXEL_PURPLE
    else:
        pixels[1] = PIXEL_OFF
    if touch_A3.value:
        pixels[2] = PIXEL_PURPLE
    else:
        pixels[2] = PIXEL_OFF
    if touch_A4.value:
        pixels[3] = PIXEL_PURPLE
    else:
        pixels[3] = PIXEL_OFF
    if touch_A5.value:
        pixels[4] = PIXEL_PURPLE
    else:
        pixels[4] = PIXEL_OFF
    if touch_A6.value:
        pixels[5] = PIXEL_PURPLE
    else:
        pixels[5] = PIXEL_OFF
    if touch_TX.value:
        pixels[6] = PIXEL_PURPLE
    else:
        pixels[6] = PIXEL_OFF

    # If all of the sensors are touched, light up all 10 NeoPixels.
    if touch_A1.value and touch_A2.value and touch_A3.value and touch_A4.value and touch_A5.value and touch_A6.value and touch_TX.value:
        pixels[0] = PIXEL_PURPLE
        pixels[1] = PIXEL_PURPLE
        pixels[2] = PIXEL_PURPLE
        pixels[3] = PIXEL_PURPLE
        pixels[4] = PIXEL_PURPLE
        pixels[5] = PIXEL_PURPLE
        pixels[6] = PIXEL_PURPLE
        pixels[7] = PIXEL_PURPLE

    pixels.show()

    time.sleep(0.01)
