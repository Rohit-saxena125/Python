# sort python dictionaries by key or value
d = {}
for i in range(int(input())):
    a,b = map(int,input().split())
    d[a] =b
print(d)
for i in sorted(d.keys()):
    print(i,end = ' ')
print('*****************************************')
# sorting keys alphsbetically
for i in sorted(d):
    print((i,d[i]),end = ' ')
print('*****************************************')
# keys and values sorted in alphabetical order
print(sorted(d.items(),key= lambda kv:(kv[1],kv[0])))
print('*****************************************')
# keys and values sorted using value
from collections import OrderedDict
d1 = OrderedDict(sorted(d.items()))
print(d1)
# sort dictionary by the key
