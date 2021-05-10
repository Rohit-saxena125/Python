# check number is divisible by 5 and 10 or by 5 or 10
num = int(input("Enter the number:"))
if num % 5 == 0 and num % 10 == 0:
    print(num,'is divisible by both 5 and 10')
elif num % 5 == 0 or num % 10 == 0:
    print(num, 'is divisible by  5 or 10')
else :
    print(num,'is not divisible by either 5 or 10')