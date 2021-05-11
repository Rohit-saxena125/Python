# Find the factorial of a number using while loop
num = int(input("Enter the number :"))
fact = 1
ans = 1
while fact <= num :
    ans *= fact
    fact += 1
print('Factorial of ',num,'=',ans)