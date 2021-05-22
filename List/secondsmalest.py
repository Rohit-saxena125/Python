# find second smallest number in a list
list1 = []
for i in range(int(input())):
    a = int(input())
    list1.append(a)
list1.sort()
print(list1[1])