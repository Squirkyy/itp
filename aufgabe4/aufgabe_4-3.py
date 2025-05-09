import time
import multiprocessing
from multiprocessing import Value

done = Value('b', True)


class Fahrzeug:
    def __init__(self, ID, num_tire, max_speed, color, brand, weight, year_con):
        self.ID = ID
        self.num_tire = num_tire
        self.max_speed = max_speed
        self.color = color
        self.brand = brand
        self.weight = weight
        self.year_con = year_con

    def run():
        pass

    def draw():
        pass


def delete_line(i):
    CURSOR_UP = "\033[1A"
    CLEAR = "\x1b[2K"

    for _ in range(abs(i)):
        print(CURSOR_UP + CLEAR, end="")


def task(i, done):
    while done.value:
        print(str(i) + ": " + str(done.value))
        time.sleep(1)
        done.acquire()
    print("process" + str(i) +" says bye")

def race(done):
    time.sleep(3)
    done = multiprocessing.Value('b', False)
    done.release()
    print(str(done.value) + "somthing long really really long so long i can find it between all the long things")



if __name__ == '__main__':
    print("Rennen Startet")
    for i in range(3, 0, -1):
        print(i)
        """time.sleep()"""

    delete_line(4)

    p1 = multiprocessing.Process(name="p1",target=task, args=(1,done))
    p2 = multiprocessing.Process(target=task, args=(2, done))
    p3 = multiprocessing.Process(name="race", target=race, args=(done,))

    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()
