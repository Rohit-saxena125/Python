def cheeck(string) :
    p = set(string)
    s = {'0','1'}
    if s == p or p == {'0'} or p == {'1'}:
        return 'Yes'
    return 'No'

if __name__ == "__main__" :
    string = input()
    print(cheeck(string))