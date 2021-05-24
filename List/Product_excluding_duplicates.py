# list product excluding duplicates
def prod(value):
    res = 1
    for i in value :
        res *= i
    return res
list1 = []
for i in range(int(input())):
    a = int(input())
    list1.append(a)
s = ' using native '
print(s.center(len(s)+20,'*'))
result = []
for i in list1:
    if i not in result :
        result.append(i)
res = prod(result)
print(res)
s = ' using list comprehension '
print(s.center(len(s)+20,'*'))
result = []
[result.append(i) for i in list1 if i not in result]
res = prod(result)
print(res)