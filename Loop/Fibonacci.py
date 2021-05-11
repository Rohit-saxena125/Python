'''
First number = 0
second number = 0
Fibonacci = 0 1 1 2 3 5 8 13 21 34 55
'''
First_number ,second_number,limit = eval(input())
for i in range(limit +1):
    sum = First_number + second_number
    First_number = second_number
    second_number = sum
    print(sum ,end=' ')