# find Remove element from set

set1 =set ()
for i in range(int(input())):
    a = int(input())
    set1.add(a)
for i in range(len(set1)):
    set1.pop()
print(set1)