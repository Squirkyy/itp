from functools import reduce

def main():
    arr = ["Apfel", "Banane", "Kirsche", "Mango", "Erdbeere", "Ananas"]

    print("Gegebene Liste von Woertern: " + str(arr))

    print("Berechnen der Laenge jedes Wortes: " + str(list(map((lambda x : len(x)), arr))))

    print("Filtern nach Woertern mit mehr als fuenf Buchstaben" + str(list(filter(lambda x : len(x) > 5, arr))));

    print("Berechnen der Gesamtlaenge der verbleibenden Woerter: " + str(reduce(lambda x,y :x + y, map(lambda x : len(x), filter(lambda x : len(x) > 5, arr)))))
main()
