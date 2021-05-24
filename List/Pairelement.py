# Pair element with rear element in matrix row
list1 = []
for i in range(int(input())):
    a  =list(map(int,input().split()))
    list1.append(a)
s = ' using list comprehension '
print(s.center(len(s)+ 20,'*'))
result =[]
for i in list1 :
    result.append([[ele,i[-1]] for ele in i[ :-1]])
print(result)
s = ' using product + loop '
print(s.center(len(s)+ 20,'*'))
from itertools import product
for i in list1 :
    result.append(list(product(i[ : -1] , [i[-1]])))
print(result)