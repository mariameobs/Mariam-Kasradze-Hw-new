entered_number = int(input("Please, enter positive number that is between 0 and 1000: "))

if entered_number < 0:
    print("Please, enter positive number")
if entered_number > 1000:
    print("Please, enter number that is less 1000")

calculate = 0
while calculate != 1:
    if entered_number % 2 == 0:
        print(entered_number, end=" -> ")
        calculate = int(entered_number / 2)
        entered_number = calculate
    else:
        calculate = int(entered_number * 3 + 1)
        entered_number = calculate
        print(entered_number, end=" -> ")
else:
    print(entered_number)
