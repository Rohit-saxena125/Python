'''
1
1 2
1 2 3
1 2 3 4
1 2 3
1 2
1
'''
num = 1
b = int(input("enter the number of lines :"))
x = num
for i in range (1,b,1):
    num += 1
    for j in range (1,num,1):
        print(j,end=' ')
        x = num + 1
    print()
num = b
x = num
for i in range(1,b,1):
    num -= 1
    for j in range (1,num,1):
        print(j,end=' ')
        x = num - 1
    print()