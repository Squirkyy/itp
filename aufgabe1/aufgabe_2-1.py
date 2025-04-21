def durchschnitt(list):
    summe = 0
    for i in list:
        summe += i
    return (summe / len(list))

print(durchschnitt([5, 10, 15]))
