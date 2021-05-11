# 1 + x + x**2 + ...................................n
n = int(input("Enter the number:"))
i=0
print('1',end=' + ')
while i<n:
    i += 1
    if i==1:
        print('x',end=' + ')
    else :
        print('x**',i,end=' + ')
print('\b\b')