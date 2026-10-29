weight=int(input("Please enter your weight: "))
height=int(input("Please enter your height: "))
bmi=weight/(height*height)
if bmi < 18.5:
    print(f'Your BMI is {bmi}, which is considered underweight.')
elif bmi >= 18.5 and bmi < 25:
    print(f'Your BMI is {bmi}, which is considered normal.')
elif bmi >= 25 and bmi < 30:
    print(f'Your BMI is {bmi}, which is considered overweight.')
else:
    print(f'Your BMI is {bmi}, which is considered obese.')