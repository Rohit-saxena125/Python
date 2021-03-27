k = int(input('enter the number of line:'))
n=2*k-2
for i in range (k) :
    for j in range (n):
        print(' ')
    k -=2
    for j in range(0,i+1):
        print('*',end='')
    print() 
