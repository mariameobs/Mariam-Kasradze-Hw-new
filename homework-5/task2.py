height = 0

while height <= 9:
    for i in range(1, height + 1):
        print(i,"*",height,"=",i * height, end=" ")
    print()
    height += 1
