# count unique value in a list
l = []
for i in range(int(input())):
    a = input()
    l.append(int(a))
s = ' traversing '
print(s.center(len(s)+20,'*'))
list1 = []
count = 0
for i in l:
    if i not in list1:
        count += 1
        list1.append(i)
print(count)
s = ' collections counter '
print(s.center(len(s)+20,'*'))
from collections import Counter
items = Counter(l).keys()
print(len(items))
s = ' using sets '
print(s.center(len(s)+20,'*'))
set1 = set(l)
print(len(set1))