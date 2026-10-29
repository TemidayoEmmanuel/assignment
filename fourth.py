age=int(input("Please enter your age : "))
if age <= 15:
    print(f'age below {age} pays a ticket price of 10')
elif age > 15 and age <= 20:
    print(f'age between {age} pays a ticket price of 15')
elif age > 20 and age <= 30:
    print(f'age between {age} pays a ticket price of 30')
else:
    print(f'age above {age} pays a ticket price of 15')
