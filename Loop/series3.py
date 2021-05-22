# sum of alternate sign of number
num = int(input('Enter the number :'))
sum = 0
sum1 = 0
for i in range(1, num+1):
    if i % 2 ==0:
        sum1 += -i
    else:
        sum += i
print('the sum of series is :',sum+sum1)