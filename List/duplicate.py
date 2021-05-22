# find duplicate number in a list
def duplicate(x):
    size = len(x)
    duplicate1 =[]
    for i in range(size):
        k = i + 1
        for j in range (k,size):
            if x[i] == x[j] and x[i] not in duplicate1 :
                duplicate1.append(x[i])
    return duplicate1
list1 = []
for i in range(int(input())):
    a = int(input())
    list1.append(a)
print(duplicate(list1))