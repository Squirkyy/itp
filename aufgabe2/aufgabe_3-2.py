import random

def create_name():
    parts = ["DI", "DE", "AN", "A", "EI", "TE", "TIL", "LEX", "SE", "SA", "E"]
    s = ""

    for _ in range(0, random.randint(1, 3)): 
        s += random.choice(parts)
    return s

def create_data():
    return [(create_name(), random.randint(15, 25), random.randint(0, 100)) for _ in range(0, 71)]



def main():
    data = create_data()

    print(data)

main()
