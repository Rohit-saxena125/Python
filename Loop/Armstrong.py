# check the number is armstrong or not
# 153= 1**3 + 5**3 + 3**3 = 153
num = int(input("enter the number :"))
sum = 0
x = num
while num>0:
    d= num % 10
    num //= 10
    sum += d**3
if sum ==x:
    print('the number ',x,'is armstrong number')
else :
    print('the number ', x, 'is not armstrong number')