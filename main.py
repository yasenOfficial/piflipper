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


disp.begin()


disp.clear()


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



def HandleMenu(op, submenu_active):
    symbols = [" ", " ", " ", " ", " "]

    if op is not None and op < 5:
        symbols[op] = ">"

    if not submenu_active:
        symbols[0] = ">"
        if(op != 0):
            symbols[0] = " "

    return symbols



def read_button_states(pins, op):
  
    for pin in pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  
    button_states = {}
    for pin in pins:
        button_states[pin] = GPIO.input(pin)

    
    return process_button_states(button_states, op)

def process_button_states(button_states, op):
    for pin, state in button_states.items():
        if state == GPIO.LOW:  
            if pin == 26:
                return 2626
            
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
                return 555

    return op


current_option = 0 

def HandleMainCode():
    button_pins = [5, 6, 26, 25, 23, 24]
    option = 0  
    submenu_active = False  

    
    while True:
        if not submenu_active:
            option = read_button_states(button_pins, option)  
            symbols = HandleMenu(option, submenu_active)

            with Image.open("black.png").convert("RGBA") as base:
                txt = Image.new("RGBA", (disp.width, disp.height), (255, 255, 255, 1))
                d = ImageDraw.Draw(txt)

                menu_items = ["NFC", "125 KHz", "Sub-1 GHz", "IR", ":)"]

                for i, item in enumerate(menu_items):
                    symbol = symbols[i]
                    d.text((5, 5 + i * 50), f"{symbol}{item}", font=fnt, fill=(0, 255, 0, 255)) 

                base = base.resize((disp.width, disp.height))
                txt = txt.resize((disp.width, disp.height))
                out = Image.alpha_composite(base, txt)
                disp.display(out)

                if option == 555: 
                    submenu_active = True  
                    time.sleep(0.2) 

        elif op == 0 and submenu_active:
            # Display the submenu
            with Image.open("black.png").convert("RGBA") as base:
                txt = Image.new("RGBA", (disp.width, disp.height), (255, 255, 255, 1))
                d = ImageDraw.Draw(txt)

                submenu_items = ["Saved", "Read", "Write" , "Emulate"]

                for i, item in enumerate(submenu_items):
                    d.text((5, 5 + i * 50), item, font=fnt, fill=(0, 255, 0, 255)) 

                base = base.resize((disp.width, disp.height))
                txt = txt.resize((disp.width, disp.height))
                out = Image.alpha_composite(base, txt)
                disp.display(out)

            submenu_option = read_button_states(button_pins, None)

            if submenu_option == 2626:
                submenu_active = False 
                symbols = HandleMenu(option, submenu_active)
        

if __name__ == '__main__':
    op = 0
    while True:
        HandleMainCode()
