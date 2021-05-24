# Adding tuple to a list and vice versa
list1 = []
for i in range(int(input())):
    a = int(input())
    list1.append(a)
print(list1)
t1 = []
for i in range(int(input())):
    a = input()
    t1.append(int(a))
print(tuple(t1))
s = ' using += operator [list + tuple] '
print(s.center(len(s)+20,'*'))
list1 += t1
print(list1)
print(tuple(list1))
s = ' using tuple, datatype conversion [list + tuple] '
print(s.center(len(s)+20,'*'))
result = tuple(list1) +  tuple(t1)
print(result)
s = ' using tuple, datatype conversion [list + tuple] '
print(s.center(len(s)+20,'*'))

result = list1 +  list(t1)
print(result)