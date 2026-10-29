year=int(input("Please enter your year of birth : "))
if year == 366:
    print('this is a leap year')
elif year == 365:
    print('this is not a leap year')
else:
    print('invalid input.')
