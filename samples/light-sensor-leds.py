# Reads the on-board light sensor and changes the
# color of a NeoPixel depending on the value.

import time
import board
import neopixel
import analogio

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.05, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

light = analogio.AnalogIn(board.LIGHT)

while True:
    current_light = light.value
    if current_light <= 1400:
        pixels[5] = (255, 0, 0)
    else:
        pixels[5] = (0, 0, 255)
    pixels.show()

    time.sleep(0.1)
