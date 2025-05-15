import adafruit_dht as DHT
from time import sleep
from board import D4
dht = DHT.DHT22(D4)

while True:
    try:
        print(dht.temperature)
        sleep(3)
    except RuntimeError as e:
        print("Error: ", e.args)
