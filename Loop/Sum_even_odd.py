# sum of even and odd number seprate
sum_even = 0
sum_odd = 0
for i in range(int(input()),int(input())+1):
    if i % 2 ==0:
        sum_even +=i
    else :
        sum_odd += i
print('The sum of odd is:',sum_odd,'\nThe sum of even is:',sum_even)