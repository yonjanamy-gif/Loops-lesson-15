word = input ("Enter a word: ")
ch= input ("Enter a character: ")
for i in word:
    if(i == ch):
        print(ch, "is found")
        break
    else:
        print(ch, "is not found")
        