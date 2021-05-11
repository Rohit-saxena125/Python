# check the number is prime or not
num = int(input('Enter the number :'))
for i in range (2,num):
    if num % i ==0:
        flag = 0
        break
    else :
        flag = 1
if flag == 1:
    print(num,'is prime')
else :
    print(num, 'is not prime')