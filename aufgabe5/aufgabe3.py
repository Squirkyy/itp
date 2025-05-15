from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)
steps = [x * 0.01 for x in range(0,100)]
while True:
    for x in steps:
        led.value = x
        sleep(0.05)
    print("Reached max. Reversing...")
    steps.reverse()
    for x in steps:
        led.value = x
        sleep(0.05)
    steps.reverse()
    print("Reached min. Reversing...")
