a=int(input("Please enter a first number:"))
b=int(input("Please enter a second number:"))
for i in range(a,b+1):
    if i % 5 == 0 and i % 7 == 0:
        print(i)