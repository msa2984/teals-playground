# TEALS Playground
This repository contains files for a high school lab using Adafruit's Circuit Playground platform. 

## Overview
The goal of the code in this repository is to support a lab environment for students of an AP Computer Science Principles course. Since the course is focused on python knowledge, this environment uses python to teach students about interacting with hardware using code. 

## Structure

- [samples](./samples/)
  - The base code snippets used in the lab.
- [libraries](./libraries/)
  - The libraries required on the Circuit Playground board to run all of the samples in the previous directory.
- [documentation](./documentation/)
  - Additional documentation for the lab, other than what is available online for the Circuit Playground
- [Gitlab Actions](./actions.yaml)
  - A simple Gitlab Actions implementation which lints the code in the repository.

## Library Usage

Like most python projects, the Circuit Playground uses libraries for many functionalities. These libraries are not necessarily part of the /lib package initially, however preparation for the lab has loaded the .mpy files from the ./libraries directory onto the Circuit Playground used in the labs. If you want to run this code yourself, we recommend downloading the most updated libraries from Adafruit's repositories, such as the [NeoPixel CircuitPython repository](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel)

## References

- [Adafruit Circuit Playground](https://learn.adafruit.com/category/circuit-playground)
- [Adafruit Samples](https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/main)
- [What is an LED?](https://learn.adafruit.com/all-about-leds/what-is-an-led)
- [Capacitive Touch](https://learn.adafruit.com/make-it-sense/using-capacitive-touch)
- [Light Sensor](https://learn.adafruit.com/adafruit-circuit-playground-express/playground-light-sensor)
- [What is a Phototransistor?](https://www.build-electronic-circuits.com/phototransistor/)
- [Infrared Transmit + Receive](https://learn.adafruit.com/infrared-ir-receive-transmit-circuit-playground-express-circuit-python/overview)
- [Electromagnetic spectrum](https://en.wikipedia.org/wiki/Electromagnetic_spectrum)
