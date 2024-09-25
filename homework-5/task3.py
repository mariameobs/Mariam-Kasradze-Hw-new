n = int(input("Please, enter number:"))

if n < 0:
    print("Please, enter positive number")
    exit(1)

if n > 20:
    print("Please, entet number that is less than 20")
    exit(1)

count = 0
a = 0
b = 1

print(a, b, end=" ")
while count + 1 < n:
    for i in range(1, n):
        i = a + b
        a, b = b, i
        print(i, end=" ")
        count += 1