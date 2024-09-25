n = int(input("Please, enter number:"))

if n < 0:
    print("Please, enter positive number")
    exit(1)

if n > 50:
    print("Please, enter number that is less than 50")
    exit(1)

count = 0
i = 0

print(n, "-", end=" ")
while count < 3:
    i += 1
    if n % i == 0:
        print(i, end = " ")
        count += 1
