# Datei: Gruppe_07_P01_A03_A08.py
from gpiozero import LED, Button, Buzzer
import time

# Pin-Belegung
led_rot = LED(17)
led_gelb = LED(27)
led_gruen = LED(22)
buzzer = Buzzer(18)
taster = Button(23, pull_up=True, bounce_time=0.1)

counter = 0

def taster_gedrueckt():
    print("Taster gedrückt")

def taster_freigegeben():
    print("Taster losgelassen")

# Taster-Interrupt (Events)
taster.when_pressed = taster_gedrueckt
taster.when_released = taster_freigegeben

def main():
    global counter
    try:
        while True:
            time.sleep(3)
            counter += 1
            print(f"Zähler: {counter}")
            # Rote LED toggeln
            led_rot.toggle()
            # Buzzer ertönen lassen, wenn der Zähler durch 3 teilbar ist
            if counter % 3 == 0:
                buzzer.on()
                time.sleep(0.5)
                buzzer.off()
    except KeyboardInterrupt:
        print("Programm beendet")
    finally:
        # LEDs und Buzzer ausschalten
        led_rot.off()
        led_gelb.off()
        led_gruen.off()
        buzzer.off()

# Gelbe LED blinken alle 1 Sekunde
led_gelb.blink(on_time=1, off_time=1)
# Grüne LED blinken alle 5 Sekunden
led_gruen.blink(on_time=5, off_time=5)
main()

