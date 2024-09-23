number = input("Please enter number: ")

number_float = float(number)
number_int = int(number_float)

if number_float != number_int:
    print("Please, enter integer")
    exit(1)
    
if number_float < 0:
    print("Please, enter positive number")
    exit(1)


for i in range(1,100):
    if int(number) % i == 0:
        print(i, end=" ")