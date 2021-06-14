def dictionary_input_1d(n):
    d1 = {}
    for i in range(n):
        a = input().split()
        d1[a[0]] = eval(a[1])
    return d1
    """ This is used for 1 dimensional dictionary enter from user"""
#first method
def merge1(dict1,dict2):
    """Using update method merge dictionary"""
    return dict2.update(dict1)
#second method
def merge2(dict1,dict2):
    result = {**dict1 , **dict2}
    return result
def merge3(dict1,dict2):
    result = dict1 | dict2
    return result

if __name__ == "__main__":
    dict1 =dictionary_input_1d(int(input()))
    dict2 =dictionary_input_1d(int(input()))
    print(merge1(dict1, dict2))
    print(dict2)
    print(merge2(dict1, dict2))
    print(merge3(dict1, dict2))