number = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))
if number < number2:
    print(f'{number} is less than {number2}.')
elif number > number2:
    print(f'{number} is greater than {number2}.')
else:
    print(f'{number} is equal to {number2}.')