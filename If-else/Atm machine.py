a ,b = map(float,input().split(' '))
if a % 5 == 0:
    if a>b:
        print(format(b,".2f"))
    else:
        x = b - a -0.50
        print(format(x,".2f"))
elif a % 5 != 0 :
    print(format(b,".2f"))
elif a>b:
    print(format(b,".2f"))