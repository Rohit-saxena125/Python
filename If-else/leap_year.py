year = int(input('enter year: '))
if year %4 == 0 and year %100!=0:
    print("a leap year")
elif year %100 == 0:
    print("not a leap year")
elif year %400 ==0:
    print("a leap year")
else:
    print("not a leap year")
