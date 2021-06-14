# convert dictionary into list and list into dictionary
def list_dict_2d(a):
    """ This is used for 1 dimensional list-dictionary enter from user"""
    key = a.keys()
    value = zip(*[a[i] for i in key])
    list1 = [ dict(zip(key,j)) for j in value]
    return list1

def dictionary_input_1d(n):
    d1 = {}
    for i in range(n):
        a = input().split()
        d1[a[0]] = list(map(int,a[1: : 1]))
    return d1
    """ This is used for 1 dimensional dictionary enter from user"""
if __name__ == '__main__':
    a = dictionary_input_1d(2)
    print(a)
    b = list_dict_2d(a)
    print(b)