# Write a program to check the sum of number which is not divisible by 2 or 3 or 5
sum = 0
for i in range(int(input()),int(input())+1):
    if i % 2 ==0 or i % 3 ==0 or i % 5 ==0:
        continue
    else :
        sum +=i
print("sum of numbers =",sum)