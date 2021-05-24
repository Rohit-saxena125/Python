# remove empty list in a list
list1 = []
for i in range(int(input())):
    a = input()
    list1.append(a)
list1 = [ele for ele in list1 if ele != '[]']
print(list1)