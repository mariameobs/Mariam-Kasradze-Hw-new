import random

count_players = int(input("Enter players number: "))

if count_players < 0 :
    count_players = int(input("Please enter positive number of players: "))
else:
    count_players = int(count_players)


x = 0 #To check iteration
for i in range(count_players):
    x += 1
    if x == count_players:
        print(random.randint(1,6),end="")
    else:
        print(random.randint(1,6),end=",")