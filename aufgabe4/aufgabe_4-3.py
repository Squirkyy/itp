import time
import multiprocessing
import random

class Vehicle:
    def __init__(self, ID, num_tire, max_speed, color, brand, weight, year_con, short, lock, curser_pos):
        self.ID = ID
        self.num_tire = num_tire
        self.max_speed = max_speed
        self.color = color
        self.brand = brand
        self.weight = weight
        self.year_con = year_con
        self.short = short

        self.finished_distance = 0
        self.curser_pos = curser_pos
        self.clear = "\x1b[2K"
        self.move_up = f"\033[{4 - ID};1H"
        self.move_down = f"\033[{4 - ID};1H"


        self.lock = lock

    def run(self):
        result = self.max_speed * self.num_tire / self.weight * random.random() * 10
        return round(result)

    def draw(self, ticket, finished):
        if finished.value:
            with self.lock:
                ticket.value += 1
            return True

        self.finished_distance += self.run()
        self.print_at_line(ticket)
        
        return self.finished_distance >= 400

    def print_at_line(self, ticket):
        with self.lock:
            move_by = self.curser_pos.value - self.ID + 1
            if move_by > 0:
                curser = "\033[" + str(move_by) + "A"
            elif move_by < 0:
                curser = "\033[" + str(abs(move_by)) + "B"
            else:
                curser = ""
    
            print(curser + self.clear, end="")
            print(self.position_at_start())
            self.curser_pos.value = self.ID
            ticket.value += 1


    def position_at_start(self):
        if self.finished_distance == 0:
            return self.short + "-" * 40 + "|"
        elif self.finished_distance == 400:
            return "|" + "-" * 40 + self.short
        else:
            return "|" + "-" * round((self.finished_distance - 1)/10) + self.short + "-" * round((400 - self.finished_distance)/10) + "|"



def task(vehicle, finished, start_time, number_of_comp, ticket):
    while start_time > time.time():
        pass

    while not vehicle.draw(ticket, finished):
        while (ticket.value - vehicle.ID) % number_of_comp != 0:
            pass
        time.sleep(1/24)

    if not finished.value:
        with finished.get_lock():
            finished.value = vehicle.ID



def operate():
    finished = multiprocessing.Value('i', 0)
    last_pos = multiprocessing.Value('i', 3)
    ticket = multiprocessing.Value('i', 1)
    start_time = time.time() + 4
    lock = multiprocessing.Lock()

    gr_supra = Vehicle(1, 4, 257, "gray", "toyota", 1542, 2024, 'C', lock, last_pos)
    viper = Vehicle(2, 2, 333, "red", "Millyard", 540, 2023, 'M', lock, last_pos)
    w900 = Vehicle(3, 8, 160, "red/blue", "Kennworth", 9000, 2024, 'T', lock, last_pos)
    all_of_them = [gr_supra, viper, w900]

    car = multiprocessing.Process(target=task, args=(gr_supra, finished, start_time, len(all_of_them), ticket))
    motorcycle = multiprocessing.Process(target=task, args=(viper, finished, start_time, len(all_of_them), ticket))
    truck = multiprocessing.Process(target=task, args=(w900, finished, start_time, len(all_of_them), ticket))
    
    car.start()
    motorcycle.start()
    truck.start()
    
    while time.time() < (start_time - 3):
        pass
    with lock:
        print("\n")
        print(gr_supra.position_at_start())
        print(viper.position_at_start())
        print(w900.position_at_start())
        print(" \033[6A")

        for i in range (3, 0, -1):
            print(f"{i}!", end=" ", flush=True)
            time.sleep(1)
        print("Go! \033[4B")
    
    
    car.join()
    motorcycle.join()
    truck.join()
    
    time.sleep(0.01)
    print("\033[2B \nRennen ist beendet!")
    print(f"Gewinner: {all_of_them[finished.value - 1].short} (ID: {all_of_them[finished.value - 1].ID}, Marke: {all_of_them[finished.value - 1].brand})")

if __name__ == "__main__":
    operate()
