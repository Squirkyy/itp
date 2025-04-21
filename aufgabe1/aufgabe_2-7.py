def trapez(height, rotation=0):
    if rotation not in [0, 180]:
        print("Ungültiger Drehwinkel")
        return

    gesamtbreite = 4 + 2 * (height - 1)  # Breite der untersten Zeile
    
    if rotation == 0:
        for i in range(height):
            stars = 4 + 2 * i
            seitenabstand = (gesamtbreite - stars) // 2
            print(" " * seitenabstand + "*" * stars + " " * seitenabstand)
    elif rotation == 180:
        for i in range(height-1, -1, -1):
            stars = 4 + 2 * i
            seitenabstand = (gesamtbreite - stars) // 2
            print(" " * seitenabstand + "*" * stars + " " *seitenabstand)


print("Trapez mit Höhe=4 und Rotation=0 \n")
trapez(4)
print("\nTrapez mit Höhe=4 und Rotation=180 \n")
trapez(4, 180)
