# check the person age is eligible or not for voting
age = int(input('Enter your age :'))
if age >= 18:
    print(age, 'is valid for voting')
else:
    print('sorry your age is {} is not valid for voting'.format(age))