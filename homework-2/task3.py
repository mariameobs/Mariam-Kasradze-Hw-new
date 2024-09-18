number = int(input("Please, enter number: "))

if number > 10:
    number = int(input("Please, reenter number that is less than or equal to 10"))
elif number < 0:
    number = int(input("Please, reenter number that is positive"))

if number % 2 == 0:
    print(2, end="")
    if number % 3 == 0:
        print(",",3)
    elif number % 5 == 0:
        print(",",5)
elif number % 3 == 0:
    print(3, end="")
    if number % 2 == 0:
        print(",",3)
elif number % 5 == 0:
    print(5)
elif number % 7 == 0:
    print(7)
