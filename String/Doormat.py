a,b = map(int,input().split())
for i in range(1,a,2):
    print((i*'.|.').center(3*a,'-'))
print(('WELCOME').center(3*a,'-'))
for i in range(a-2,0,-2):
    print((i*'.|.').center(3*a,'-'))