# removing multiple element in a list
list1 = []
for i in range(int(input())):
    a = int(input())
    list1.append(a)
print(list(set(list1)))