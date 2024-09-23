import random
n = int(input("Please enter number: "))

if n < 0:
    print("Input should be positive number")
    exit(1)

if n > 30:
    print("Input should be less than 30")
    exit(1)

generated_number = random.randint(0,1000)

max = 0
for i in range(n):
    if generated_number > max:
       max = generated_number

print(max)