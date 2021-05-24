# create a list of tuple from given list
t = []
for i in range(int(input())):
    a = int(input())
    t.append(a)
result = [(i,i**2,i**3) for i in t]
print(result)