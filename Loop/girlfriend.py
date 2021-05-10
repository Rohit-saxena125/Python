# minimunm ways to girlfriend house
a =int(input())
b=0
c=0
if a<=5:
    b+=1
else:
    d=5
    while c!=a:
        c+=d
        d=a-c
        if d>5:
            d=5
        b+=1
print(b)
