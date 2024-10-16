entered_number = int(input("Please, enter number that is between 0 and 10000: "))

if entered_number < 0:
    print("Please, enter positive number")
if entered_number > 10000:
    print("Please, enter number that is less 10000")

reversed = ""
count = 0
while count != len(str(entered_number)):
    reversed += str(entered_number)[-1-count]
    count += 1

sum = 0
i = 0
while i != len(str(entered_number)):
    sum += int(str(entered_number)[i])
    i += 1

print("Reversed number is", reversed)
print("Sum of digits:",sum)