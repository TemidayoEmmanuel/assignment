guess=76
number=int(input("Please enter a number between 1 and 100: "))
if number < guess:
    print('Your guess is too low.')
elif number > guess:
    print('Your guess is too high.')
else:
    print('Congratulations! You guessed the number.')