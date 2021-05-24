import numpy
def arrays(arr):
    c = []
    for i in arr[ : :-1]:
        c.append(i)
    b = numpy.array(c,float)
    return b
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)