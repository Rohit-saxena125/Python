# find the size of set in bytes
s1 = set()
for i in range(int(input())):
    a = int(input())
    s1.add(a)
print(s1)
s2 = set()
for i in range(int(input())):
    a = input()
    s2.add(a)
print(s2)
s = ' using getsizeof() '
print(s.center(len(s)+20,'*'))
import sys
print(sys.getsizeof(s1),'bytes')
print(sys.getsizeof(s2),'bytes')
s = ' using inbuilt __sizeof__() '
print(s.center(len(s)+20,'*'))
print(s1.__sizeof__(),'bytes')
print(s2.__sizeof__(),'bytes')