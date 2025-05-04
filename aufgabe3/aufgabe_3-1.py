import math

def average(L: []):
    return sum(L) / len(L)

def isnumber(test: str):
    try:
        return (float(test), True)
    except:
        (0, False)

def main():
    L = []
    
    while True:
        i = input("Eingabe: ")
        match i.lower():
            case "q":
                break
            case "pi":
                L.append(math.pi)
            case "e":
                L.append(math.e)
            case "tau":
                L.append(math.tau)
            case _ if l := isnumber(i):
                L.append(l[0])
            case _:
                pass

    print("Eingabe: " + str(L))
    print("Durschnitt der Eingabe: " + str(average(L)))

main()
