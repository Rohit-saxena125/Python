def list_list_tuple(n):
    lis = []
    for i in range(n):
        a = tuple(map(str,input().split()))
        lis.append([a])
    return lis
def list_input_1d(n):
    list1 = []
    for i in range(n):
        a = int(input())
        list1.append(a)
    return list1
if __name__ == '__main__':
    b = list_list_tuple(5)
    a = list_input_1d(3)
    result = [[(idx,val) for idx in key] for key ,val in zip(b,a)]
    print(result)