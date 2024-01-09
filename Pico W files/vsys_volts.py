from machine import Pin, ADC, I2C
import time
from credentials import secrets

DEBUG = secrets['DEBUG']

def measure_vsys():
    """
    # https://github.com/orgs/micropython/discussions/10421
    GPIO29 OP/IP wireless SPI CLK/ADC mode (ADC3) to measure VSYS/3
    GPIO29 WiFi chip SDIO_DATA3 / gate on FET between VSYS divider (FET drain) and GPIO29 (FET source)
    GPIO25 OP wireless SPI CS - when high also enables GPIO29 ADC pin to read VSYS
    """
    Pin(25, Pin.OUT, value=1) 
    Pin(29, Pin.IN, pull=None)
    reading = ADC(3).read_u16() * 9.9 / 2**16
    Pin(25, Pin.OUT, value=0, pull=Pin.PULL_DOWN)
    Pin(29, Pin.ALT, pull=Pin.PULL_DOWN, alt=7)
    if DEBUG:
        print("measure_vsys", reading)
    return reading

