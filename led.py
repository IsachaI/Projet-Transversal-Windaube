from gpiozero import LED
from time import sleep
green = LED(17)
def allumer():
    green.on
    sleep(1)
    green.off
    sleep(1)