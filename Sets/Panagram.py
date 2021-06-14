from string import ascii_lowercase as asc
def check(s):
    return set(asc) - set(s.lower()) == set([])
if __name__ == '__main__':
    if check(input()) :
        print('The string is a pangram')
    else:
        print('The string is not a pangram')