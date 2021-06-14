def tuple_input_1d(n):
    list1 = []
    for i in range(n):
        a = tuple(map(int,input().split()))
        list1.append(a)
    return list1
if __name__ == '__main__':
    a = tuple_input_1d(5)
    print(a)
    result = []
    for i in a :
        if result and result[-1][0] == i[0]:
            result[-1].extend(i[1:])
        else :
            result.append([ele for ele in i])
    result = list(map(tuple,result))
    print(result)
'''
    import collections
    mapp = collections.defaultdict(list)
    for key,val in a:
        mapp[key].append(val)
    result = [(key, *val) for key ,val in mapp.items()]
    print(result)
   '''