n = int(input())
d = {}
for i in range(n):
    name,number = map(str,input().split())
    d[name] = int(number)
print(d)
for i in d:
    name = input()
    if name in d:
        print(name,'=', d[name])
    else :
        print('Not found')