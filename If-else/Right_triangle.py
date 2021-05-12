#Find given triangle is right angled or not
a,b,c = eval(input("Enter the sides of triangle :"))
if a**2 == b**2 + c**2:
    print('It is right angle triangle')
else :
    print('It is not a right angle triangle')