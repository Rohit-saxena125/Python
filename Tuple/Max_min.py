# find maximum and minimum elements in tuple
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
print(max(t),min(t),max(t1),min(t1))
s = ' using sorted + loop '
print(s.center(len(s)+20,'*'))
# find maximum and minimum K elements in tuple
k = int(input('Enter the value of k:'))
result = []
t = list(t)
t2 = sorted(t)
for i ,val in enumerate(t2):
    if i < k or i >= len(t2) -k :
        result.append(val)
print(tuple(result))
s = ' using list slicing + sorted '
print(s.center(len(s)+20,'*'))
t1 = list(t1)
t2 = sorted(t1)
result = tuple(t2[ :k] + t2[-k: ])
print(result)