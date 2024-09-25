n = int(input("Please, enter number:"))

if n < 0:
    print("Please, enter positive number")
    exit(1)

if n > 50:
    print("Please, enter number that is less than 20")
    exit(1)

print(n * " ", "*")
height = 1

while height < n: #1<5
    print(" " * (n - height), "/" * height, end="")
    print("|", end="")
    print("\\" * height)
    height += 1
print(n * " ", "|")