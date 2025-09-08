import random
integer = random.randint(1,100)
tries = 0
while True:
    choice = int(input("Please enter a number between 1 and 100:"))
    tries +=1
    if choice == integer:
        print("Congratulations. Total try =" , tries)
        break
    elif choice > integer:
        print("Your choice is higher than the number")
    else:
        print("Your choice is lower than the number")