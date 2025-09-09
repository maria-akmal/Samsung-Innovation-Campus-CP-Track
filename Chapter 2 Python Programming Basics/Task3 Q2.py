numbers = input("Enter numbers separated by space: ").split()
numbers = [int(num) for num in numbers]
number={}
for num in numbers:
    if num in number:
        number[num]+=1
    else:
        number[num]=1
print(number)