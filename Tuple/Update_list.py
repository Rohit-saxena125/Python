def list_list_tuple(n):
    lis = []
    for i in range(n):
        a = tuple(map(int,input().split()))
        lis.append(a)
    return lis
if __name__ == '__main__':
    a = list_list_tuple(3)
    add_ele = int(input())
    result = [tuple(j + add_ele for j in sub) for sub in a] #[tuple(map(lambda ele : ele +add_ele,sub)) for sub in a]
    print(result)