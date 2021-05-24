# select random value from list of lists
s = ' using chain.from_iterable() + random.choice() '
print(s.center(len(s)+20,'*'))
from itertools import chain
import random

list1 = []
for i in range(int(input())):
    a  =list(map(int,input().split()))
    list1.append(a)
result = random.choice(list(chain.from_iterable(list1)))
print(result)
s = ' random.choice() '
print(s.center(len(s)+20,'*'))
r_no = 1
result = random.choice(list1[r_no])
print(result)