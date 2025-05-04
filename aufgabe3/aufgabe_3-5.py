import string

def textanalyse(dateiname):
    try:
        with open(dateiname, 'r', encoding='utf-8') as file:
            text = file.read()

        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

        woerter = text.split()

        woerter_ueber_3_buchstaben = [wort for wort in woerter if len(wort) > 3]
        anzahl_woerter_ueber_3_buchstaben = len(woerter_ueber_3_buchstaben)

        haeufigkeit = {}
        for wort in woerter:
            if wort in haeufigkeit:
                haeufigkeit[wort] += 1
            else:
                haeufigkeit[wort] = 1

        haeufigstes_wort = max(haeufigkeit, key=haeufigkeit.get)

        laengstes_wort = max(woerter, key=len)

        durchschnittliche_laenge = sum(len(wort) for wort in woerter) / len(woerter)

        print(f"Anzahl der Wörter mit mehr als drei Buchstaben: {anzahl_woerter_ueber_3_buchstaben}")
        print(f"Das am häufigsten verwendete Wort: {haeufigstes_wort} mit {haeufigkeit[haeufigstes_wort]} Vorkommen")
        print(f"Das längste Wort im Text: {laengstes_wort} mit {len(laengstes_wort)} Buchstaben")
        print(f"Durchschnittliche Wortlänge im Text: {durchschnittliche_laenge:.2f}")

    except FileNotFoundError:
        print(f"Die Datei '{dateiname}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

textanalyse('py03.txt')
