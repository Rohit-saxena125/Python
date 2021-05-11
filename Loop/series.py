# x + x**2/2! + ...................................n
n = int(input("Enter the number:"))
i=0
while i<n:
    i += 1
    if i==1:
        print('x',end=' + ')
    else :
        print('x**',i,'/',i,'!',end=' + ')
print('\b\b')