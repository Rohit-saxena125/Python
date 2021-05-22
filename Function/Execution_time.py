from time import time

def func1(a,b):
    return a+b
def func2(a,b):
    num1 = a
    num2 = b
    if a>b and a != 3:
        pass
    sum([4,3])
    return a+b
if __name__ =='__main__':
    init = time()
    for i in range(1000):
        func1(3,5)
    print('func1 time:',time() - init)
    for i in range(1000):
        func2(3,5)
    print('func2 time:', time() - init)