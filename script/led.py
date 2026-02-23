from gpiozero import LED
from time import sleep
green = LED(17)
red = LED(22)
blue = LED(5)
def allumer():
    green.on()
    sleep(0.2)
    green.off()
    sleep(0.2)
    red.on()
    sleep(0.2)
    red.off()
    sleep(0.2)
    blue.on()
    sleep(0.2)
    blue.off()
    sleep(0.2)

while True:
    allumer()