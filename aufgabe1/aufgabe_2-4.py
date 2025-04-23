from collections import Counter

def count (text):
    return list(set([(letter, text.count(letter)) for letter in text]))

text = input("Eingabe:")
print(count(text))
