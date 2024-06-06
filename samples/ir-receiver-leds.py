import pulseio
import board
import adafruit_irremote
import neopixel

# Create a 'pulseio' input, to listen to infrared signals on the IR receiver
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
# Create a decoder that will take pulses and turn them into numbers
decoder = adafruit_irremote.GenericDecode()

# Pixels is an array of ten NeoPixels on the board.
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=False)

# Constants for the color(s) of NeoPixels
PIXEL_OFF = (0,0,0)
PIXEL_PURPLE = (180, 0, 255)

while True:
    pulses = decoder.read_pulses(pulsein)
    try:
        # Attempt to convert received pulses into numbers
        received_code = decoder.decode_bits(pulses)
    except adafruit_irremote.IRNECRepeatException:
        # We got an unusual short code, probably a 'repeat' signal
        continue
    except adafruit_irremote.IRDecodeException:
        # Something got distorted or maybe its not an NEC-type remote?
        continue

    print("NEC Infrared code received: ", received_code)
    if received_code == (0, 253, 8, 247):
        if pixels[0] == PIXEL_OFF:
            pixels[0] = PIXEL_PURPLE
        else:
            pixels[0] = PIXEL_OFF
    if received_code == (0, 253, 136, 119):
        if pixels[1] == PIXEL_OFF:
            pixels[1] = PIXEL_PURPLE
        else:
            pixels[1] = PIXEL_OFF
    if received_code == (0, 253, 72, 183):
        if pixels[2] == PIXEL_OFF:
            pixels[2] = PIXEL_PURPLE
        else:
            pixels[2] = PIXEL_OFF
    if received_code == (0, 253, 40, 215):
        if pixels[3] == PIXEL_OFF:
            pixels[3] = PIXEL_PURPLE
        else:
            pixels[3] = PIXEL_OFF
    if received_code == (0, 253, 168, 87):
        if pixels[4] == PIXEL_OFF:
            pixels[4] = PIXEL_PURPLE
        else:
            pixels[4] = PIXEL_OFF
    if received_code == (0, 253, 104, 151):
        if pixels[5] == PIXEL_OFF:
            pixels[5] = PIXEL_PURPLE
        else:
            pixels[5] = PIXEL_OFF
    if received_code == (0, 253, 24, 231):
        if pixels[6] == PIXEL_OFF:
            pixels[6] = PIXEL_PURPLE
        else:
            pixels[6] = PIXEL_OFF
    if received_code == (0, 253, 152, 103):
        if pixels[7] == PIXEL_OFF:
            pixels[7] = PIXEL_PURPLE
        else:
            pixels[7] = PIXEL_OFF
    if received_code == (0, 253, 88, 167):
        if pixels[8] == PIXEL_OFF:
            pixels[8] = PIXEL_PURPLE
        else:
            pixels[8] = PIXEL_OFF
    
    pixels.show()