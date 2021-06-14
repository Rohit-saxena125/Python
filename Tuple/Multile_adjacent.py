def tuple_input_1d(n):
    list1 = []
    for i in range(n):
        a = eval(input())
        list1.append(a)
    return tuple(list1)
if __name__ == '__main__':
    a = tuple_input_1d(5)
    result = tuple( i * j for i, j in zip(a,a[1:])) # tuple(map(lambda i, j : i * j , a[1:],a[:-1]
    print(result)