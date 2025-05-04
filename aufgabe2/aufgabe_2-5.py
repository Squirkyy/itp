def main():
    thisdict = {}
    while True:
        print("Menue:\n1 - Hinzufuegen\n2 - Loeschen\n3 - Modifizieren\n4 - Leeren\n0 - Beenden")
        i = input("Eingabe: ")
        match i:
            case "0":
                break

            case "1":
                key = input("Geben Sie den Schluessel ein: ")
                thisdict[key] = input("Geben Sie den Wert ein: ")

            case "2":
                if thisdict and (key := input("Welchen Schluessel-Wert-Paar moechtest du loeschen? ")) in thisdict:
                    thisdict.pop(key)
                else:
                    print("Fehler: Das Dictionary ist leer/Schluessel existiert nicht. Loeschen nicht moeglich.")
            
            case "3":
                if (key := input("Welcher Schluessel soll geaendert werden?")) in thisdict:
                    thisdict[key] = input("neuer Wert: ")
                else:
                    print("Schluessel existiert nicht")
            
            case "4":
                if thisdict:
                    thisdict.clear()
                else:
                    print("Fehler: Das Dictionary ist leer. Loeschen nicht moeglich.")

            case _:
                print("Keine richtige Eingabe")

        print("Aktuelles Dictionary: " + str(thisdict))

main()
