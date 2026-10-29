time = int(input("Please enter the time in 24-hour format (0-23): "))
if time  > 0  and time < 12:
    print('good morning')  
elif time >= 12 and time < 16:
    print('good afternoon')
elif time >= 16 and time < 23:
    print('good evening')
else:
    print('invalid input.')