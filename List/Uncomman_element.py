# find uncoman element in a list of list
s = ' native method '
print(s.center(len(s)+20,'*'))
list1 = []
list2 = []
result = []
n = int(input())
print('for list1 enter element :\n')
for i in range(n):
    a  =list(map(int,input().split()))
    list1.append(a)
print('for list2 enter element :\n')
for i in range(n):
    b  =list(map(int,input().split()))
    list2.append(b)
for i in list1 :
    if i not in list2:
        result.append(i)
for i in list2 :
    if i not in list1:
        result.append(i)
print(result)
s = ' using set() + map() and ^ '
print(s.center(len(s)+20,'*'))
result_set = set(map(tuple,list1)) ^ set(map(tuple,list2))
result = list(map(list,result_set))
print(result_set)
print(result)