# sum of the digits of a given numbers
num = int(input("Enter the number:"))
x = num
sum = 0
rem = 0
while num>0:
    rem = num%10
    num //= 10
    sum +=rem
print("sum of digit of an entered number",x,"=",sum)