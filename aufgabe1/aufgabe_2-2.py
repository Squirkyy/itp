def vocale(text):
    count = 0
    for letter in text:
        match letter:
            case 'a' | 'e' | 'i' | 'o'| 'u':
                count += 1
            case _:
                pass
    return count


text = input("Eingabe: ")
print("Ausgabe: " + str(vocale(text)))
