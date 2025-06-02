# Datei: Gruppe_07_P01_A09_A10.py
from gpiozero import LED, Button, DistanceSensor, PWMLED
import time

# Pin-Belegung
led_rot = LED(17)
led_gelb = LED(27)
led_gruen = LED(22)
buzzer = PWMLED(18, frequency=440)
sensor = DistanceSensor(echo=20, trigger=21, max_distance=0.4)
taster = Button(23, pull_up=True, bounce_time=0.1)

def map_range(x, in_min, in_max, out_min, out_max):
    """Skaliert x von Bereich in_min..in_max nach out_min..out_max."""
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def drucke_entfernung():
    dist = sensor.distance * 100
    print(f"Entfernung: {dist:.1f} cm")

# Taster-Event für Abstandsausgabe
taster.when_pressed = drucke_entfernung

def main():
    try:
        while True:
            dist = sensor.distance * 100  # Abstand in cm
            if dist < 2 or dist > 20:
                # Außerhalb des Messbereichs: alle Ausgänge ausschalten
                led_rot.off()
                led_gelb.off()
                led_gruen.off()
                buzzer.off()
            else:
                # Buzzer-Lautstärke abhängig von der Entfernung (2..20 cm -> 1.0..0.2)
                volume = map_range(dist, 2, 20, 1.0, 0.2)
                buzzer.value = volume
                # LEDs entsprechend der Abstandskategorie schalten
                if dist <= 7:
                    led_rot.on()
                    led_gelb.off()
                    led_gruen.off()
                elif dist <= 13:
                    led_rot.off()
                    led_gelb.on()
                    led_gruen.off()
                else:
                    led_rot.off()
                    led_gelb.off()
                    led_gruen.on()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Programm beendet")
    finally:
        # Alle Ausgänge ausschalten
        led_rot.off()
        led_gelb.off()
        led_gruen.off()
        buzzer.off()

if __name__ == "__main__":
    main()

