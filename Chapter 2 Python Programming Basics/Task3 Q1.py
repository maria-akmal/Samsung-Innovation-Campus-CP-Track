words=[]
word1=input("Enter a first word:")
words.append(word1)
word2=input("Enter a secound word:")
words.append(word2)
word3=input("Enter a third word:")
words.append(word3)
word4=input("Enter a fourth word:")
words.append(word4)
word5=input("Enter a fifth word:")
words.append(word5)
print(words)
shortest_lenght=len(words[0])
for word in words:
    if len(word)<shortest_lenght:
        shortest_lenght=len(word)
print("shortest word(s):")
for word in words:
    if len(word)==shortest_lenght:
        print(word)