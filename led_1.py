# Turn on a led.
from machine import Pin

led = Pin(1, Pin.OUT)
led.value(1)