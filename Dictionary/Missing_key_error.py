# Handling missing key in python dictionaries
d = {}
for i in range(int(input())):
    a,b = map(str,input().split())
    d[a] =b
c = input('Enter finding keys :')
s = ' using get() '
print(s.center(len(s)+20,'*'))
print(d.get(c,None))
s = ' using setdefault() '
print(s.center(len(s)+20,'*'))
d.setdefault(c,None)
print(d[c])
s = ' using defaultdict() '
print(s.center(len(s)+20,'*'))
import collections
d = collections.defaultdict(lambda : 'Key not found')
print(d[c])
