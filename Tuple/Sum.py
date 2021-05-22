# find sum of tupe
list1 = []
for i in range(int(input())):
    a = int(input())
    list1.append(a)
t = tuple(list1)
print(t)
print(sum(list(t)))