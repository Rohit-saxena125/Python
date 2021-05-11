# display pattern
'''
1
12
123
1234
12345
123456
'''
num = 1
x = num
for i in range(1,int(input()),1):
    num += 1
    for j in range(1,num,1):
        print(j,end=' ')
        x = num +1
    print()