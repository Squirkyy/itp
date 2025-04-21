from random import randint

print("Geben Sie eine Zahl ein: ")
prediction = input()
random_number = randint(1,6)

print(f"Die Zahl wurde korrekt vorhergesagt (Vorhersage: {prediction}, Tatsächliche Zahl: {random_number})") if int(prediction)== random_number else print(f"Die Zahl wurde inkorrekt vorhergesagt (Vorhersage: {prediction}, Tatsächliche Zahl: {random_number})") 
