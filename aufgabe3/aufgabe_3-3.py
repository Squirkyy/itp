def main():
    print("Format: Name ENTER Note ENTER")
    data = dict()
    while(True):
        print("Name: ", end='')
        name = input()
        if name.upper() == 'Q':
            break
        print("Note: ", end='')
        note = input()
        print()
        data[name] = note
    print(data)
    with open ("grades.csv", "a") as f:
        f.write("Name,Note\n")
        for name,grade in data.items():
            f.write(f"{name},{grade}\n")

main()
