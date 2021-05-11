# display tables
a = int(input('Enter the number :'))
for i in range(1,11,1):
    for j in range(1,a+1,1):
        print(format(i*j,"4d"),end=' ')
    print()