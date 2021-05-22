'''
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''
n = int(input())
b = []
list = ["insert", "print", "remove", "append", "sort", "pop", "reverse"]
for j in range(n):
    a = input()
    c = a.split()
    if c[0] == list[0]:
        b.insert(int(c[1]), int(c[2]))
    elif c[0] == list[1]:
        print(b)
        continue
    elif c[0] == list[2]:
        b.remove(int(c[1]))
    elif c[0] == list[3]:
        b.append(int(c[1]))
    elif c[0] == list[4]:
        b.sort()
    elif c[0] == list[5]:
        b.pop()
    elif c[0] == list[6]:
        b.reverse()
    else:
        exit()
