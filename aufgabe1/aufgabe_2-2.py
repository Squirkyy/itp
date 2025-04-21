def vocale(zeichenkette):
    count = 0
    for letter in zeichenkette:
        match letter:
            case 'a' | 'e' | 'i' | 'o'| 'u':
                count += 1
            case _:
                pass
    return count

print(vocale("Hallo world"))
