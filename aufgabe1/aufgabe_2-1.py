#def average(list):
#    return sum(list) / len(list)

def average(list):
    sum = 0
    for i in list: sum += i
    return sum / len(list)

input = [5, 10, 15]
print("Eingabe: " + str(input))
print("Ausgabe:" + str(average(input)))
