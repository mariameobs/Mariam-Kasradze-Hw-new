text = input("Please, enter a word: ")
result = ""

for c in text:
    if c != "a" and c != "e" and c != "i" and c != "o" and c != "u":
        result += c
print(result)