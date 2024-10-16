action = input("Please, enter action (e/d): ")
text = input("Please, enter text: ")
result = ""

row_1 = "qwertyuiop"
row_2 = "asdfghjkl"
row_3 = "zxcvbnm"

if "e" == action:
    for c in text:
        if c in row_1:
            if c == "p":
                result += row_1[0]
            else:
                result += row_1[row_1.find(c)+1]
        if c in row_2:
            if c == "l":
                result += row_2[0]
            else:
                result += row_2[row_2.find(c)+1]
        if c in row_3:
            if c == "m":
                result += row_3[0]
            else:
                result += row_3[row_3.find(c)+1]

if "d" == action:
    for c in text:
        if c in row_1:
            if c == "q":
                result += row_1[-1]
            else:
                result += row_1[row_1.find(c)-1]
        if c in row_2:
            if c == "a":
                result += row_2[-1]
            else:
                result += row_2[row_2.find(c)-1]
        if c in row_3:
            if c == "z":
                result += row_3[-1]
            else:
                result += row_3[row_3.find(c)-1]

print(result)
