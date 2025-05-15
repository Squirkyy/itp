from gpiozero import LED
from gpiozero import Button
from time import sleep

class car_traffic:
    def __init__(self):
        self.red = LED(17)
        self.orange = LED(27)
        self.green = LED(22)
        
        self.red.off()
        self.orange.off()
        self.green.on()
        
        self.drive = True

    def change(self):
        if self.drive:
            self.green.off()
            self.orange.on()
            
            sleep(1)

            self.orange.off()
            self.red.on()
            
            self.drive = False
        else:
            self.orange.on()

            sleep(1)

            self.red.off()
            self.orange.off()
            self.green.on()

            self.drive = True


class other_traffic:
    def __init__(self):
        self.red = LED(23)
        self.green = LED(24)

        self.red.on()
        self.green.off()

        self.move = False

    def change(self):
        if not self.move:
            self.red.off()
            self.green.on()

            self.move = True
        else:
            self.red.on()
            self.green.off()
            self = False






def main():
    button = Button(2)
    car = car_traffic()
    other = other_traffic()

    while True:
        if button.is_pressed:
            car.change()
            sleep(1)
            other.change()
            sleep(3)

            other.change()
            sleep(1.5)
            car.change()



main()
