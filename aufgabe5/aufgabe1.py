from gpiozero import LED
from time import sleep

led1 = LED(27)
led2 = LED(17)

while True:
    led1.on()
    led2.off()
    sleep(1)
    led1.off()
    led2.on()
    sleep(1)
