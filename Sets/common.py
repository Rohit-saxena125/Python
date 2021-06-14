def list_input_1d(n):
    list1 = []
    for i in range(n):
        a = int(input())
        list1.append(a)
    return list1
def comman_element(a,b):
    result = False
    for i in a:
        for j in b:
            if i == j :
                result = True
                return result
    return result
def comman_element1(a,b):
    a1 = set(a)
    b1 = set(b)
    if a1 & b1 :
        return True
    else:
        return False
def comman_element2(a,b):
    a1 = set(a)
    b1 = set(b)
    if len(a1.intersection(b1)) > 0 :
        return True
    return False
def intersect1(a,b,c):
    set1 = set(a).intersection(set(b))
    result = set1.intersection(set(c))
    return list(result)
if __name__ == "__main__":
    a = list_input_1d(int(input()))
    b = list_input_1d(int(input()))
    c = list_input_1d(int(input()))
    print(comman_element(a, b))
    print(comman_element2(a, b))
    print(comman_element1(a, b))
    print(intersect1(a,b,c))