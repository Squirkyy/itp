def add_to_list():
    list = []
    i = 0
    while i < 5:
        try:
            list.append(float(input("your number:")))
            i += 1
        except ValueError:
            print("not a number")
    return list

print(add_to_list())
