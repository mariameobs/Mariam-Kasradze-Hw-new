import random

n=int(input("Please, enter number: "))
if n <= 0:
    print("Input should be higher than 0")
    exit(1)
    
if n >= 20:
    print("Input should be less than 20")
    exit(1)

a = 0 #zeroth position
b = 1 #first position in the sequence
for i in range(1,n):
    i = a + b
    a, b = b, i
print(i)

