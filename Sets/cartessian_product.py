from itertools import product
A = list(map(int,input().split(' ')))
B = list(map(int,input().split(' ')))
c = list(product(A,B))
for i in c:
    print(i, end = " ")
print('\n')
s = 'Another method'
print(s.center(50,'*'))
c = [(x,y) for x in A for y in B]
print(c)