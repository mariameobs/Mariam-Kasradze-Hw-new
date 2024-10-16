text = input("Please, enter text: ")
result = ""

for c in text:
    if c != "e" and text[1:].find(c) % 2 == 0:
        result += c

print(result)