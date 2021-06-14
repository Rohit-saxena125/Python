def check(result):
    set3 = set([ch for ch in result if ord(ch) >= ord("a") and ord(ch) <= ord("z")])
    if len(set3) == len(set(set3)) :
        return 'Yes'
    return 'No'
if __name__ == '__main__':
    print(check(input()))