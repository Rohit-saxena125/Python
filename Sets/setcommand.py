n = int(input())
s = set(map(int, input().split()))
command = int(input())
for j in range(command):
    a = input()
    c = a.split()
    if c[0] == 'discard':
        s.discard(int(c[1]))
    elif c[0] == 'remove':
        s.remove(int(c[1]))
    else :
        s.pop()
print(sum(list(s)))