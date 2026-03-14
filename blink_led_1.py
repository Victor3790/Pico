# Make a led blink every X amount of time
import machine
import utime

led = machine.Pin(1, machine.Pin.OUT)

while True:
    led.toggle()
    utime.sleep(0.5) # Blink every x seconds