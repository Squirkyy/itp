import random

def create_name():
    parts = ["DI", "DE", "AN", "A", "EI", "TE", "TIL", "LEX", "SE", "SA", "E", "ZE", "US"]
    s = ""

    for _ in range(0, random.randint(1, 3)): 
        s += random.choice(parts)
    return s


def create_data():
    return [(create_name(), random.randint(15, 25), random.randint(0, 100)) for _ in range(0, 71)]


def print_better(l: list):    
    print("Name | Alter | Punkte")
    print("-----|-------|-------")
    
    for i in l:
        print(i[0] + " | " + str(i[1]) + " | " + str(i[2])) 
    
    print("-----|-------|-------")



def main():
    data = create_data()

    new_data = list(filter(lambda data : (data[1] > 18 and data[2] >= 70), data))

    new_data = list(map(lambda data : (data[0], data[1], data[2] * 1.05), new_data))

    new_data = list(sorted(new_data, key=lambda x : x[2], reverse=True))

    print_better(new_data[:3])

main()
