speed = int(input("Please, enter speed: "))


if speed < 0:
    speed = int(input("Please, enter positive number: "))
    
if speed <= 30:
    print("SLOW")
elif speed >= 120:
    print("VERY FAST")
elif speed >= 60:
    print("FAST")
else:
    print("MODERATE")