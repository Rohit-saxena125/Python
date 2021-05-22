# find sum and average of list
n = int(input())
l = []
for i in range(n):
    a = int(input())
    l.append(a)
print(sum(l),sum(l)/n)