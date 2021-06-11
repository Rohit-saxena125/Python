n = int(input())

for i in range(n):
    a = input()
    b = str()
    c = str()
    for j in range(0,len(a)):
        if j%2==0:
            b = b + a[j]
        else :
            c = c+a[j]
    print(str(b)+' '+str(c))
    