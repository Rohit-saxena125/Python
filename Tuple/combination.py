def tuple_input_1d(n):
    list1 = []
    for i in range(n):
        a = int(input())
        list1.append(a)
    return tuple(list1)
if __name__ == '__main__':
    t1 = tuple_input_1d(int(input()))
    t2 = tuple_input_1d(int(input()))
    result = [(a,b) for a in t1 for b in t2]
    result = result + [(b,a) for a in t1 for b in t2]
    print(result)
    '''
    import itertools
    result = list(itertools.chain(itertools.product(t1,t2),itertools.product(t2,t1)))
    print(result)
    '''