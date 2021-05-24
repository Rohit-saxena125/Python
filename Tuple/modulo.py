# modulo of tuple element
t = []
for i in range(int(input())):
    a = int(input())
    t.append(a)
print(tuple(t))
t1 = []
for i in range(int(input())):
    a = int(input())
    t1.append(a)
print(tuple(t1))
s = ' using zip() + generator '
print(s.center(len(s)+20,'*'))
result = [ i % j for i,j in zip(t,t1)]
print(result)
s = ' using map() + mod '
print(s.center(len(s)+20,'*'))
from operator import mod
result = tuple(map(mod,t,t1))
print(result)