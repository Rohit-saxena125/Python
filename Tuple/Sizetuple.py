# find the size of tuple in bytes
t = []
for i in range(int(input())):
    a = int(input())
    t.append(a)
print(tuple(t))
t1 = []
for i in range(int(input())):
    a = input()
    t1.append(a)
print(tuple(t1))
s = ' getsizeof() '
print(s.center(len(s)+20,'*'))
import sys
print(str(sys.getsizeof(t))+'bytes')
print(str(sys.getsizeof(t1))+'bytes')
s = ' using inbuilt __sizeof__() method '
print(s.center(len(s)+20,'*'))
print(str(t.__sizeof__())+'bytes')
print(str(t1.__sizeof__())+'bytes')