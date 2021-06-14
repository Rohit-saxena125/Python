import collections
def removewithout(s):
    return ''.join(set(s))
def removewith(s):
    return ''.join(collections.OrderedDict.fromkeys(s))
def removeduplicate(s):
    s1 = set(s)
    s1 = ''.join(s1)
    print('without order',s1)
    t = ''
    for i in s:
        if i in t :
            pass
        else:
            t = t+ i
    print('with order ',t)
if __name__ == '__main__':
    str1 = input()
    print(f'without order {removewithout(str1)}\nwith order {removewith(str1)}\n{removeduplicate(str1)}')
