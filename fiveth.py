guess=76
i=0 
limit=3
while i < limit:
    number=int(input("Please enter a number between 1 and 100: ")) 
    i += 1
    if number < guess:
        print('Your guess is too low.')
    elif number > guess:
        print('Your guess is too high.')
    elif number == guess:
        print('Congratulations! You guessed the number.')
        break
    else:
        print('invaild input.')     