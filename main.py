import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

import ST7789 as TFT
import datetime
import os
import time

import RPi.GPIO as GPIO

from PIL import Image, ImageDraw, ImageFont, ImageColor

import numpy as np

RST = 22            # Set GPIO pin# 15 (BCM 22) as reset control
DC  = 17            # Set GPIO pin# 11 (BCM 17) as DATA/command (NOT MOSI!)
LED = 27            # Set GPIO pin# 13 (BCM 27) as backlight control
SPI_PORT = 0
SPI_DEVICE = 0
SPI_MODE = 0b11
SPI_SPEED_HZ = 40000000
disp = TFT.ST7789(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=SPI_SPEED_HZ),
       mode=SPI_MODE, rst=RST, dc=DC, led=LED)

fnt = ImageFont.truetype("fonts/FreeMonoBold.otf", 30)

# Initialize display.
disp.begin()

# Clear display.
disp.clear()

# Set GPIO pin numbering mode
GPIO.setmode(GPIO.BCM)

def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

# Clear output and display a purple background

def HandleMenu(op):
    symbols = [" ", " ", " ", " ", " "]

    if op is not None:
        symbols[op] = ">"

    return symbols

# Example usage

def read_button_states(pins, op):
    # Set the pins as inputs with pull-up resistors
    for pin in pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Read the states of the buttons
    button_states = {}
    for pin in pins:
        button_states[pin] = GPIO.input(pin)

    # Process the button states
    return process_button_states(button_states, op)

def process_button_states(button_states, op):
    for pin, state in button_states.items():
        if state == GPIO.LOW:  # Button is pressed (GPIO.LOW indicates a button press)
            if pin == 26:
                return "back"
            
            elif pin == 23:
                op -= 1
                if op < 0:
                    op = 0
                return op
            
            elif pin == 24:
                op += 1
                if op > 4:
                    op = 4
                return op
            
            elif pin == 25:
                return "left"
            elif pin == 6:
                return "right"
            elif pin == 5:
                return "ok"

    return op


current_option = 0  # Variable to store the current option

def HandleMainCode():
    button_pins = [5, 6, 26, 25, 23, 24]
    option = 0  # Initialize option variable

    while True:
        option = read_button_states(button_pins, option)  # Pass option to read_button_states

        symbols = HandleMenu(option)

        with Image.open("black.png").convert("RGBA") as base:
            txt = Image.new("RGBA", (disp.width, disp.height), (255, 255, 255, 1))
            d = ImageDraw.Draw(txt)

            menu_items = ["NFC", "125 KHz", "Sub-1 GHz", "IR", ":)"]

            for i, item in enumerate(menu_items):
                symbol = symbols[i]
                d.text((5, 5 + i * 50), f"{symbol}{item}", font=fnt, fill=(0, 255, 0, 255))  # hacker green

            base = base.resize((disp.width, disp.height))
            txt = txt.resize((disp.width, disp.height))
            out = Image.alpha_composite(base, txt)
            disp.display(out)

if __name__ == '__main__':
    op = 0
    while True:
        HandleMainCode()
