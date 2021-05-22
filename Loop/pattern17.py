'''
1
121
12321
1234321
123454321
'''
b = int(input())
for i in range(0, b , 1):
    for j in range(1, i+1, 1):
        print(j, end='')
    for j in range(i+1, 0, -1):
        print(j, end='')
    print('\r')