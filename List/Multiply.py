# mutipling all element in a list
def multiply(list2):
    result = 1
    for i in list2:
        result = result * i
    return result
list1 = []
for i in range(int(input())):
    a = int(input())
    list1.append(a)
print(multiply(list1))
s = 'Another method'
print(s.center(50,'*'))
import numpy
list1 = []
for i in range(int(input())):
    a = int(input())
    list1.append(a)
result = numpy.prod(list1)
print(result)