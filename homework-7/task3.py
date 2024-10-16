text = input("Please, enter a word: ")

i = 0
while i in range(5):
    print("Last character: ",text[-1])
    print("First character: ",text[0])
    if len(text) % 2 != 0:
        print("Middle character: ",text[-(int((len(text)-1)/2+1))])
    else:
        print("Middle characters: ",text[int(len(text)/2-1)],text[int(len(text)/2)])
    i += 1
