import random
guess_number = random.randint(0, 100)


count = 0

while count < 10:
    count += 1
    entered_number = int(input("Please, enter number between 0 and 100: "))
    if count == 10:
        print("Computer is winner!")
    elif entered_number == guess_number:
        print("You are winner!")
        break
    elif entered_number > guess_number:
        print("High")
    elif entered_number < guess_number:
        print("Low")

