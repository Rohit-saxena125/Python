# remove tuple in a list
def tuple_input_2d(n):
    list1 = []
    for i in range(n):
        a = input().split()
        list1.append(tuple(a))
    return tuple(list1)
a = list(tuple_input_2d(int(input())))
l = []
for i in a:
    if i == ():
        pass
    else:
        l.append(i)
print(l)