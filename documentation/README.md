# Documentation README 

## Overview

This README pertains to the documentation stored in this directory, as well as including some other pertinent information.

## Files
  
- [Embedded Software Lab Powerpoint](/documentation/Embedded_Software_Lab.pptx)
  - The original PowerPoint for the lab experiment(s).
- [Embedded Software Lab PDF](/documentation/Embedded_Software_Lab.pdf)
  - The PowerPoint, in PDF form.

## Sensors Used in the Lab 

### NeoPixels

NeoPixels are individually addressable LEDs. They're built by Adafruit, and they use WS2812, WS2811, and SK6812 drivers. Not all individually addressable LEDs are NeoPixels, but if they use these same drivers, they likely work in similar ways!

learn.adafruit.com/adafruit-neopixel-uberguide/the-magic-of-neopixels

Using CircuitPython, some common colors can be defined for NeoPixels

| Color | Value |
| ---- | ---- |
| RED | (255, 0, 0) | |
| YELLOW | (255, 150, 0) | | 
| GREEN | (0, 255, 0) | |
| CYAN | (0, 255, 255) | |
| BLUE | (0, 0, 255) | |
| PURPLE | (180, 0, 255) | |

### Touch Sensors (Capacitive Sensors) 

There are 14 "Alligator Pads" on the Circuit Playground. While some of these allow the developer to tap into voltages on the board such as 3.3V and GND, the non-power pads can be used for capacitive touch capabilities. Essentially, when something is pressed against these capacitive touch pads, the board can measure how much current is generated. Different objects generate different current values. Fruit can generate similar current levels to the human finger!

learn.adafruit.com/circuit-playground-lesson-number-0/alligator-pads-pinout#capacitive-touch


### Light Sensor (Phototransistor) 
There is an integrated phototransistor on the Circuit Playground. This sensor measure the *amount* of light it receives, and the developer can use this value to control output from the board. Phototransistors are similar to capacitive touch sensors in that when a certain state is reach, current is generated.

https|//learn.adafruit.com/circuit-playground-lesson-number-0/light-sensor

The values read by the phototransistor range between 0 and 1023, where 0 is no light detected and 1023 is maximum light detected. 

### Speaker

All Circuit Playground devices have a speaker which can output simple WAV files.

### IR Receiver (IR Remote Control) 
The Circuit Playground and Circuit Playground Express have both an integrated IR transmitter and receiver, however during the lab we used the IR receiver with the [Adafruit mini remote control](https|//www.adafruit.com/product/389) |.


The following values are transmitted from the mini remote control, following [NEC codes](https|//en.wikipedia.org/wiki/National_Electrical_Code)

| Button | Code |
| ---- | ---- |
| VOL | (0,253,0,255) |
| PLAY / PAUSE | (0, 253,128,127) |
| VOL + | (0,253,64,191) |
| SETUP | (0,253,32,223) |
| UP | (0,253,160,95) |
| STOP / MODE | (0,253,96,159) |
| LEFT | (0,253,16,239) |
| ENTER / SAVE | (0,253,144,111) |
| RIGHT | (0,253,80,175) |
| 0 / 10+ | (0,253,48,207) |
| DOWN | (0,253,176,79) |
| BACK | (0,253,112,143) |
| 1 | (0,253,8,247) |
| 2 | (0.253.136,119) |
| 3 | (0,253,72,183) |
| 4 | (0,253,40,215) |
| 5 | (0,253,168,87) |
| 6 | (0,253,104,151) |
| 7 | (0,253,24,231) |
| 8 | (0,253,152,103) |
| 9 | (0,253,88,167) |