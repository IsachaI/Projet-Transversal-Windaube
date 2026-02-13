from gpiozero import LED
from time import sleep
green = LED(17)
red = LED(22)
def allumer():
    green.on
    sleep(1)
    green.off
    sleep(1)
    red.on
    sleep(1)
    red.off
    sleep(1)