# extract element with frequency greater than k
list1 = []
for i in range(int(input())):
    a = int(input())
    list1.append(a)
k = int(input())
s = ' using loop + count() '
print(s.center(len(s)+20,'*'))
result = []
for i in list1:
    freq = list1.count(i)
    if freq > k and i not in result:
        result.append(i)
print(result)
s = ' using list comprehension + counter() '
print(s.center(len(s)+20,'*'))
from collections import Counter
result = [ ele for ele,cnt in Counter(list1).items() if cnt> k ]
print(result)