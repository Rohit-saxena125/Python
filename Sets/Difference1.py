def list_input_1d(n):
    list1 = []
    for i in range(n):
        a = int(input())
        list1.append(a)
    return list1
def lost_element(a,b):
    if len(a) > len(b):
        print(list(a.difference(b)))
    else :
        print(list(b.difference(a)))
a = set(list_input_1d(int(input())))
b = set(list_input_1d(int(input())))
c = a.difference(b)
d = lost_element(a,b)
print(list(c))
